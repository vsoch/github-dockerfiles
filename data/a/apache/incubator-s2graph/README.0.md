# S2Graph Documentation

## Dependencies
  [Python](https://www.python.org/)
  
  [Sphinx](http://www.sphinx-doc.org/en/master/)

  [Read the Docs Sphinx Theme](https://sphinx-rtd-theme.readthedocs.io/en/latest/index.html)

I used [`pip`](https://pip.pypa.io/en/stable/installing/) to install Python module.
I used [`virtualenv`](https://virtualenv.pypa.io/en/latest/) to isolate the Python environment.

> Depending on your environment, the tools(pip, virtualenv) may not be required

## Quickstart

All work is done under the `s2graph/doc` folder.

```
cd doc
```

### Creating a virtualenv environment for documnet build

If `pip` is not installed, you need to install it first by referring to the link: https://pip.pypa.io/en/stable/installing/

```
pip install virtualenv

virtualenv -p python s2graph_doc
source s2graph_doc/bin/activate
```

### install sphinx and theme
```
pip install Sphinx
pip install sphinx_rtd_theme 
```

### Building
```
make html
```

### Viewing
```
# python 2
pushd build/html && python -m SimpleHTTPServer 3000 

# python 3
pushd build/html && python -m http.server 3000 
```

### Screenshot

<img src="https://user-images.githubusercontent.com/1182522/48395569-04995d00-e75b-11e8-87b8-2f28662ef3ca.png">
<!---
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
--->

  
# S2Jobs

S2Jobs is a collection of spark programs which can be used to support `online transaction processing(OLAP)` on S2Graph.

There are currently two ways to run `OLAP` on S2Graph.


----------


## 1. HBase Snapshots

HBase provides excellent support for creating table [snapshot](http://hbase.apache.org/0.94/book/ops.snapshots.html)

S2Jobs provide `S2GraphSource` class which can create `Spark DataFrame` from `S2Edge/S2Vertex` stored in HBase Snapshot.

Instead of providing graph algorithms such as `PageRank` by itself, S2Graph let users connect graph stored in S2Graph to their favorite analytics platform, for example [**`Apache Spark`**](https://spark.apache.org/). 

Once user finished processing, S2Jobs provide `S2GraphSink` to connect analyzed data into S2Graph back.


![screen shot 2018-04-06 at 2 22 28 pm](https://user-images.githubusercontent.com/1264825/38404575-0158844e-39a6-11e8-935f-0a7d971b068b.png)

This architecture seems complicated at the first glace, but note that this approach has lots of advantages on performance and stability on `OLTP` cluster especially comparing to using HBase client API `Scan`.
 
Here is result `DataFrame` schema for `S2Vertex` and `S2Edge`. 

```
S2Vertex
root
 |-- timestamp: long (nullable = false)
 |-- operation: string (nullable = false)
 |-- elem: string (nullable = false)
 |-- id: string (nullable = false)
 |-- service: string (nullable = false)
 |-- column: string (nullable = false)
 |-- props: string (nullable = false)

S2Edge
root
 |-- timestamp: long (nullable = false)
 |-- operation: string (nullable = false)
 |-- elem: string (nullable = false)
 |-- from: string (nullable = false)
 |-- to: string (nullable = false)
 |-- label: string (nullable = false)
 |-- props: string (nullable = false)
 |-- direction: string (nullable = true)
```

To run graph algorithm, transform above `DataFrame` into [GraphFrames](https://graphframes.github.io/index.html), then run provided functionality on `GraphFrames`. 

Lastly, `S2GraphSource` and `S2GraphSink`  open two interface `GraphElementReadable` and `GraphElementWritable` for users who want to serialize/deserialize custom graph from/to S2Graph. 

For example, one can simply implement `RDFTsvFormatReader` to convert each triple on RDF file to `S2Edge/S2Vertex` then use it in `S2GraphSource`'s `toDF` method to create `DataFrame` from RDF. 

This comes very handily when there are many different data sources with different formats to migrate into S2Graph.


## 2. `WAL` log on Kafka

By default, S2Graph publish all incoming data into Kafka, and users subscribe this for **incremental processing**. 

S2jobs provide programs to process `stream` for incremental processing, using [Spark  Structured Streaming](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html), which provide a great way to express streaming computation the same way as a batch computation. 

The `Job` in S2Jobs abstract one spark and `Job` consist of multiple `Task`s. Think `Job` as very simple `workflow` and there are `Source`, `Process`, `Sink` subclass that implement `Task` interface. 

----------
### 2.1. Job Description

**Tasks** and **workflow** can be described in **Job** description, and dependencies between tasks are defined by the name of the task specified in the inputs field

>Note that these works were influenced by [airstream of Airbnb](https://www.slideshare.net/databricks/building-data-product-based-on-apache-spark-at-airbnb-with-jingwei-lu-and-liyin-tang).

#### Json Spec

```js
{
    "name": "JOB_NAME",
    "source": [
        {
            "name": "TASK_NAME",
            "inputs": [],
            "type": "SOURCE_TYPE",
            "options": {
                "KEY" : "VALUE"
            }
        }
    ],
    "process": [
        {
            "name": "TASK_NAME",
            "inputs": ["INPUT_TASK_NAME"],
            "type": "PROCESS_TYPE",
            "options": {
                "KEY" : "VALUE"
            }
        }
    ],
    "sink": [
        {
            "name": "TASK_NAME",
            "inputs": ["INPUT_TASK_NAME"],
            "type": "SINK_TYPE",
            "options": {
                "KEY" : "VALUE"
            }
        }
    ]
}

```
----------

### 2.2. Current supported `Task`s.

#### Source

- KafkaSource: Built-in from Spark.

##### Data Schema for Kafka

When using Kafka as data source consumer needs to parse it and later on interpret it, because of Kafka has no schema.

When reading data from Kafka with structure streaming, the Dataframe has the following schema.

```
Column    Type
key        binary
value    binary
topic    string
partition    int
offset    long
timestamp    long
timestampType    int

```

In the case of JSON format, data schema can be supported in config.  
You can create a schema by giving a string representing the struct type as JSON as shown below.

```
{
  "type": "struct",
  "fields": [
    {
      "name": "timestamp",
      "type": "long",
      "nullable": false,
      "metadata": {}
    },
    {
      "name": "operation",
      "type": "string",
      "nullable": true,
      "metadata": {}
    },
    {
      "name": "elem",
      "type": "string",
      "nullable": true,
      "metadata": {}
    },
    {
      "name": "from",
      "type": "string",
      "nullable": true,
      "metadata": {}
    },
    {
      "name": "to",
      "type": "string",
      "nullable": true,
      "metadata": {}
    },
    {
      "name": "label",
      "type": "string",
      "nullable": true,
      "metadata": {}
    },
    {
      "name": "service",
      "type": "string",
      "nullable": true,
      "metadata": {}
    },
    {
      "name": "props",
      "type": "string",
      "nullable": true,
      "metadata": {}
    }
  ]
}

```

- FileSource: Built-in from Spark.
- HiveSource: Built-in from Spark.
- S2GraphSource 
	- HBaseSnapshot read, then create DataFrame. See HBaseSnapshot in this document.
	- Example options for `S2GraphSource` are following(reference examples for details).
    
```js
{
	"type": "s2graph",
	"options": {
		"hbase.zookeeper.quorum": "localhost",
		"db.default.driver": "com.mysql.jdbc.Driver",
		"db.default.url": "jdbc:mysql://localhost:3306/graph_dev",
		"db.default.user": "graph",
		"db.default.password": "graph",
		"hbase.rootdir": "/hbase",
		"restore.path": "/tmp/restore_hbase",
		"hbase.table.names": "movielens-snapshot"
	}
}
```


#### Process
-   SqlProcess : process spark sql
-   custom : implement if necessary

#### Sink

- KafkaSink : built-in from Spark.
- FileSink : built-in from Spark.
- HiveSink: buit-in from Spark.
- ESSink : elasticsearch-spark
- **S2GraphSink**    
   -  writeBatchBulkload: build `HFile` directly, then load it using `LoadIncrementalHFiles` from HBase.
   - writeBatchWithMutate: use the `mutateElement` function of the S2graph object.




----------


The very basic pipeline can be illustrated in the following figure.

![screen shot 2018-04-06 at 5 15 00 pm](https://user-images.githubusercontent.com/1264825/38409873-141dcb6c-39be-11e8-99e3-74e3166d8553.png)


# Job Examples

## 1. `WAL` log trasnform (kafka to kafka)

```
{
    "name": "kafkaJob",
    "source": [
        {
            "name": "wal",
            "inputs": [],
            "type": "kafka",
            "options": {
                "kafka.bootstrap.servers" : "localhost:9092",
                "subscribe": "s2graphInJson",
                "maxOffsetsPerTrigger": "10000",
                "format": "json",
                "schema": "{\"type\":\"struct\",\"fields\":[{\"name\":\"timestamp\",\"type\":\"long\",\"nullable\":false,\"metadata\":{}},{\"name\":\"operation\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"elem\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"from\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"to\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"label\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"service\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}},{\"name\":\"props\",\"type\":\"string\",\"nullable\":true,\"metadata\":{}}]}"
            }
        }
    ],
    "process": [
        {
            "name": "transform",
            "inputs": ["wal"],
            "type": "sql",
            "options": {
                "sql": "SELECT timestamp, `from` as userId, to as itemId, label as action FROM wal WHERE label = 'user_action'"
            }
        }
    ],
    "sink": [
        {
            "name": "kafka_sink",
            "inputs": ["transform"],
            "type": "kafka",
            "options": {
                "kafka.bootstrap.servers" : "localhost:9092",
                "topic": "s2graphTransform",
                "format": "json"
            }
        }
    ]
}

```

## 2. `WAL` log transform (HDFS to HDFS)

```
{
    "name": "hdfsJob",
    "source": [
        {
            "name": "wal",
            "inputs": [],
            "type": "file",
            "options": {
                "paths": "/wal",
                "format": "parquet"
            }
        }
    ],
    "process": [
        {
            "name": "transform",
            "inputs": ["wal"],
            "type": "sql",
            "options": {
                "sql": "SELECT timestamp, `from` as userId, to as itemId, label as action FROM wal WHERE label = 'user_action'"
            }
        }
    ],
    "sink": [
        {
            "name": "hdfs_sink",
            "inputs": ["transform"],
            "type": "file",
            "options": {
                "path": "/wal_transform",
                "format": "json"
            }
        }
    ]
}

```

## 3. movielens (File to S2Graph)

You can also run an example job that parses movielens data and writes to S2graph.
The dataset includes user rating and tagging activity from MovieLens(https://movielens.org/), a movie recommendation service. 

```
// move to example folder
$ cd ../example

// run example job 
$ ./run.sh movielens
```

It demonstrate how to build a graph-based data using the publicly available MovieLens dataset on graph database S2Graph,
and provides an environment that makes it easy to use various queries using GraphQL.

----------


## Launch Job

When submitting spark job with assembly jar, use these parameters with the job description file path.  
(currently only support file type)

```
// main class : org.apache.s2graph.s2jobs.JobLauncher
Usage: run [file|db] [options]
         -n, --name <value>      job display name
Command: file [options]          get config from file
         -f, --confFile <file>   configuration file
Command: db [options]            get config from db
         -i, --jobId <jobId>     configuration file
```

For example, you can run your application using spark-submit as shown below.
```
$ sbt 'project s2jobs' assembly
$ ${SPARK_HOME}/bin/spark-submit \
    --class org.apache.s2graph.s2jobs.JobLauncher \
    --master local[2] \
    s2jobs/target/scala-2.11/s2jobs-assembly-0.2.1-SNAPSHOT.jar file -f JOB_DESC.json -n JOB_NAME
```


<!---
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
--->

# S2Graph Tinkerpop3 Implementation(s2graph-gremlin)

Currently tested with tinkerpop 3.2.5 only on gremlin-console.

## Requirement

1. Download latest [Apache Tinkerpop 3.2.5](https://www.apache.org/dyn/closer.lua/tinkerpop/3.2.5/apache-tinkerpop-gremlin-console-3.2.5-bin.zip).
2. set environment variable `GREMLIN_HOME`.
3. create ~/.groovy/grapeConfig.xml file if it does not exist as follow.

```
<ivysettings>
  <settings defaultResolver="downloadGrapes"/>
  <resolvers>
    <chain name="downloadGrapes">
      <filesystem name="cachedGrapes">
        <ivy pattern="${user.home}/.groovy/grapes/[organisation]/[module]/ivy-[revision].xml"/>
        <artifact pattern="${user.home}/.groovy/grapes/[organisation]/[module]/[type]s/[artifact]-[revision].[ext]"/>
      </filesystem>
      <ibiblio name="local" root="file:${user.home}/.m2/repository/" m2compatible="true"/>
      <ibiblio name="codehaus" root="http://repository.codehaus.org/" m2compatible="true"/>
      <ibiblio name="central" root="http://central.maven.org/maven2/" m2compatible="true"/>
      <ibiblio name="jitpack" root="https://jitpack.io" m2compatible="true"/>
      <ibiblio name="java.net2" root="http://download.java.net/maven/2/" m2compatible="true"/>
    </chain>
  </resolvers>
</ivysettings>
```

## Build

following is how to setup this project on m2 repository.

1. `sbt "project s2graph_gremlin" publishM2`: this will create single fat jar under m2 repository.
2. check if `GREMLIN_HOME` is correct.
3. goto `cd s2graph_gremlin/examples`.
4. install s2graph-gremlin plugin, `sh install_plugin.sh`.
5. go to `${GREMLIN_HOME}/bin/gremlin.sh`
5. try `s2graph_modern.groovy` to play with modern graph comes with tinkerpop.
6. try `s2graph_getting_started.groovy` for s2graph specific methods.
 
 <!---  
/*  
 * Licensed to the Apache Software Foundation (ASF) under one  
 * or more contributor license agreements.  See the NOTICE file  
 * distributed with this work for additional information  
 * regarding copyright ownership.  The ASF licenses this file  
 * to you under the Apache License, Version 2.0 (the  
 * "License"); you may not use this file except in compliance  
 * with the License.  You may obtain a copy of the License at  
 *  
 *   http://www.apache.org/licenses/LICENSE-2.0  
 *  
 * Unless required by applicable law or agreed to in writing,  
 * software distributed under the License is distributed on an  
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY  
 * KIND, either express or implied.  See the License for the  
 * specific language governing permissions and limitations  
 * under the License.  
 */  
--->  

# Movie Recommendation with Apache S2Graph(incubating) And Spark MLLib  
  
We will briefly go through the example of building movie recommendation service using the public dataset from Movielens.  
  
There are plenty of materials on the collaborative filtering algorithm and process to build recommendation dataset,   
so we will focus on how to integrate your trained machine learning model with property graph model.  
  
 ---------
 
## The technologies we'll use  
  ### [Apache S2Graph](https://s2graph.apache.org/)
  
The graph database that stores all movielens dataset. Also, S2Graph provide S2GraphQL which is unified REST Interface for not only graph query, but also serving trained model.  
  
### [Apache Spark](https://spark.apache.org/)
  We process movielens dataset with Apache Spark and most importantly, Apache Spark's MLLib is used to build the model by training movielens data.  
  
### [Annoy4s](https://github.com/annoy4s/annoy4s)  
  
After Spark build model by running ALS algorithm, use annoy4s to build the index to find approximate nearest neighbors.  
  
## The architecture  
  
![screen shot 2018-05-15 at 2 05 25 pm](https://user-images.githubusercontent.com/1264825/40040654-1389e7ba-5856-11e8-8823-5ab982a30ffc.png)
    
  
This example will set up local HBase, local Spark, local S2GraphQL server as the environment, and use [graphiql](https://github.com/graphql/graphiql) as the client.  
  
## The abstraction  
  
Followings are the representation of movielens dataset as property graph model.  
  
### 1. Service  
  
Service represent namespace or database for this example. In this example, we will use movielens as service and all schema and data will be under this namespace.   
  
```graphql
mutation{  
  Management{  
    createService(  
      name:"movielens"  
    ){  
      isSuccess  
      message  
      object{  
        id  
        name  
      }  
    }  
  }  
}
 ```  
  
### 2. Vertex Schema  
  
Represent Node in movielens dataset. Each Node can store multiple properties on it if properties are configured on vertex schema.  
Schemas must be registered under service correctly to mutate and query actual vertex/edge from S2Graph.  
  
#### 2.1. Movie  
  
Data is under `movies.csv` file and followings are an example of data.  
  
```  
movieId,title,genres  
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy  
2,Jumanji (1995),Adventure|Children|Fantasy  
3,Grumpier Old Men (1995),Comedy|Romance  
...  
```  
  
Following is mutation defined as S2GraphQL.  
  
```graphql
mutation{  
  Management{  
    createServiceColumn(  
      serviceName:movielens  
      columnName:"Movie"  
      columnType: long  
      props: [  
       {  
          name: "title"  
          dataType: string  
          defaultValue: ""  
          storeInGlobalIndex: true  
        },  
        {  
          name: "genres"  
          dataType: string  
          defaultValue: ""  
          storeInGlobalIndex: true  
        }  
       ]  
    ){  
      isSuccess  
      message  
      object{  
        id  
        name  
      }  
    }  
  }  
}
```  
  
Note that S2Graph use **user provided id**, which is usually primary key in RDBMS, as vertexId.  
S2Graph guarantee the uniqueness of vertexId by using composite of (service, serviceColumn, vertexId).  
  
Also, note that "storeInGlobalIndex" which let S2Graph build the global index on "title" property.  
When the user does not know vertexId in advance and still want to start graph query on vertices that meet certain search criteria, then this global index can be helpful.  
  
#### 2.2 User  
  
In the real world, User vertex can have various property, such as age, gender, occupation, location, etc, but in movielens dataset, userId is only available.  
  
```graphql  
mutation{  
  Management{  
    createServiceColumn(  
      serviceName:movielens  
      columnName:"User"  
      columnType: long  
    ){  
      isSuccess  
      message  
      object{  
        id  
        name  
      }  
    }  
  }  
}
```  
  
### 3. Edge  
  
Once we create vertex schema for Movie and User, it is time to create edge schema to model the relation between User and Movie.  
  
#### 3.1. rated  
  
The data is under `ratings.csv` file and this data represent which user rated which movie.  
  
```  
userId,movieId,rating,timestamp  
1,31,2.5,1260759144  
1,1029,3.0,1260759179  
1,1061,3.0,1260759182  
...  
```  
  
```graphql  
mutation{  
  Management{  
    createLabel(  
      name:"rated"  
      sourceService: {  
        movielens: {  
          columnName: User  
        }  
      }  
      targetService: {  
        movielens: {  
          columnName: Movie  
        }  
      }  
      serviceName: movielens  
      consistencyLevel: strong  
      props:[  
        {  
          name: "score"  
          dataType: double  
          defaultValue: "0.0"  
          storeInGlobalIndex: true  
        }  
      ]  
      indices:{  
        name:"_PK"  
        propNames:["score"]  
      }  
    ) {  
      isSuccess  
      message  
      object{  
        id  
        name  
        props{  
          name  
        }  
      }  
    }  
  }  
}
```  
  
Since S2Graph support vertex-centric index, which is specific to a vertex, we create primary vertex-centric index "_PK" to be sorted by their score.  
  
#### 3.2. tagged  
  
`tags.csv` file contains following data.  
  
```  
userId,movieId,tag,timestamp  
15,339,sandra 'boring' bullock,1138537770  
15,1955,dentist,1193435061  
...  
```  
  
```graphql
mutation{  
  Management{  
    createLabel(  
      name:"tagged"  
      sourceService: {  
        movielens: {  
          columnName: User  
        }  
      }  
      targetService: {  
        movielens: {  
          columnName: Movie  
        }  
      }  
      serviceName: movielens  
      consistencyLevel: weak  
      props:[  
        {  
          name: "tag"  
          dataType: string  
          defaultValue: ""  
          storeInGlobalIndex: true  
        }  
      ]  
    ) {  
      isSuccess  
      message  
      object{  
        id  
        name  
        props{  
          name  
        }  
      }  
    }  
  }  
}
```  
  
#### 3.3. similar_movie  
This represents similar movie relation, which actually not stored in S2Graph, but obtained by asking ALS model.  
Since S2Graph provide pluggable interface how to fetch/mutate from storage, it is possible to provide the custom model implementation.  
[S2GRAPH-206](https://issues.apache.org/jira/projects/S2GRAPH/issues/S2GRAPH-206?filter=allopenissues) issue contains few popular implementations on this interface, such as Annoy, FastText, TensorFlow.  
  
```graphql    
mutation{  
  Management{  
    createLabel(  
      name:"similar_movie"  
      sourceService: {  
        movielens: {  
          columnName: Movie   
        }  
      }  
      targetService: {  
        movielens: {  
          columnName: Movie  
        }  
      }  
      serviceName: movielens  
      consistencyLevel: strong  
      props:[  
        {  
          name: "score"  
          dataType: double  
          defaultValue: "0.0"  
          storeInGlobalIndex: false   
        }  
      ]  
      indices:{  
        name:"_PK"  
        propNames:["score"]  
      }  
    ) {  
      isSuccess  
      message  
      object{  
        id  
        name  
        props{  
          name  
        }  
      }  
    }  
  }  
}
```  
  
Note that there are no actual edges exist in the S2Graph system, but S2Graph knows which model to ask when user query "similar_movie" edges.  
Also note that instead of considering entire ALS model, we use Annoy to support k approximate nearest neighbor search to make prediction fast.   
  
### Schema Summary  
  
![graphql-erd](https://user-images.githubusercontent.com/1264825/40039268-b8dcb9b4-5850-11e8-8c41-7ea651b25e02.png)  
  
--------------
 
## Running this example  

### Setup  
  
1. checkout [apache s2graph master](https://github.com/apache/incubator-s2graph) on local.  
2. install [apache spark](https://spark.apache.org/downloads.html)( >= v2.2.0) on local.  
3. export **SPARK_HOME** to pointing to installed spark.  
4. `cd example; sh run.sh`  
  
### Description  
  
#### 1. Prepare  
  
Prepare all pre-requisites to run this example.   
  
- S2GraphQL server start  
  - package S2Graph.  
  - start standalone hbase.     
  - start s2graphql server on localhost port 8000.  
  - conf located under `target/apache-s2graph-*-incubating-bin/conf/` 
  - s2graphql log located under `target/apache-s2graph-*-incubating-bin/log/`  
  
- S2Jobs jar build  
  - create fat jar using `sbt project/s2jobs assembly`  
  - fat jar located under `s2jobs/target/scala-2.11/`   

- check SPARK_HOME is setup correctly  
  
  
#### 2. Create Schema  
  
- download movielens dataset(ml-latest-small.zip) under `example/movielens/input/`  
- create all schema that explained above by sending mutation request to s2graphql server.  
  
#### 3. Import Data  
  
- load movielens data as vertices and edges into S2Graph.  
- train ALS model on `ratings.csv`.  
- build annoy index from dense matrix `itemFactors` in trained ALS model.    
  
#### 4. Post Process  
  
- Bind trained annoy index from 3 to "similar_movie" edge schema by update "similar_movie".  
  
#### 5. Have fun with GraphQL   
- go to [graphiql](localhost:8000) and start traversing movielens graph.  

We provide few example queries that can show how to traverse not only graph data but also serving trained model.  
   
##### 5.1. Item Based Recommendation.  
  
This is the very basic kind of item-based collaborative filtering recommendation.  
Recommendations are **similar movies to movies that each user rated**.  

Note that we ask our model to find k nearest neighbor on the trained model to get similar_movie.  
  
```graphql  
query {  
  movielens {  
    User(id: 1) {  
      rated {  
       Movie {  
          title  
          similar_movie(limit: 5) {  
            Movie {  
              title  
            }  
          }  
        }  
      }  
    }  
  }  
}
```  
  
##### 5.2. Vertex Property Search.   
This shows S2Graph's global index feature, which answer **"movies that contain Toy in their title".**  
Note how intuitive the GraphQL syntax represent graph traversal.  
  
```graphql  
query {  
  movielens {  
    Movie(search: "title: *Toy*", limit: 5) {  
      title  
      tagged(limit: 10) {  
        User {  
          id  
          rated(limit: 5) {  
            Movie {  
              title  
            }  
          }  
        }  
      }  
    }  
  }  
}
```  
  
We can mix **model serving and graph traversal** as follow.  
  
```graphql  
query {  
  movielens {  
    Movie(search: "genres: *Comedy* AND title: *1995*", limit: 5) {  
      title  
      genres  
      similar_movie(limit: 5) {  
        Movie {  
          title  
          genres  
        }  
      }  
    }  
  }  
}
```  
  
Note that we only need the trained model to traverse "similar_movie" relation.   
  
## Summary  
  
We show how to serving not only graph data that is actually stored in the graph database but also data that can be obtained from the pre-trained model.   
  
In general, S2Graph abstract **the pre-trained model as an immutable graph that can produce vertices/edges** for input vertex.  
  
By using this abstraction, there is no distinction between model serving and graph data from client side.<!---
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 * 
 *   http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
--->

# Run S2Graph using Docker

1. Build a docker image of the s2graph in the project's root directory
	- you can build images for each type of API Server
	    ```
	    // s2graphql
	    sbt "project s2graphql" 'set version := "latest"' docker
	    
	    // s2rest_play
	    sbt "project s2rest_play" 'set version := "latest"' docker
	    
	    // s2rest_netty
	    sbt "project s2rest_netty" 'set version := "latest"' docker
	    ```
	    
	- find local image is created correctly by using `docker images`
	
	- (optional) If you need to add extra jars in classpath, use environment variable 'EXTRA_JARS'
	    ```
        docker run --name s2graph -v /LocalJarsDir:/extraJars -e EXTRA_JARS=/extraJars -dit s2graph/s2graphql:latest ...
        ```
	
2. Run MySQL and HBase container first.
	- change directory to dev-support. `cd dev_support`
	- `docker-compose build` 
3. Run graph container
	- `docker-compose up -d`

> S2Graph should be connected with MySQL at initial state. Therefore you have to run MySQL and HBase before running it.

## For OS X

In OS X, the docker container is running on VirtualBox. In order to connect with HBase in the docker container from your local machine. You have to register the IP of the docker-machine into the `/etc/hosts` file.

Within the `docker-compose.yml` file, I had supposed the name of docker-machine as `default`. So, in the `/etc/hosts` file, register the docker-machine name as `default`.

```
ex)
192.168.99.100 default
```

# Run S2Graph on your local machine

In order to develop and test S2Graph. You might be want to run S2Graph as `dev` mode on your local machine. In this case, the following commands are helpful.

- Run only MySQL and HBase

```
# docker-compose up -d graph_mysql
```

- Run s2graph as 'dev' mode

```
# sbt "project s2rest_play" run -Dhost=default
```

- or run test cases

```
# sbt test -Dhost=default
```
<!---
/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
--->
# Suggest to implement GraphQL as standard web interface for S2Graph.

  - To support GraphQL through [Akka HTTP](https://github.com/akka/akka-http) and [Sangria](https://github.com/sangria-graphql). Akka HTTP and Sangria each are an HTTP Server and GraphQL Scala implementation.
  - It is also used [GraphiQL](https://github.com/graphql/graphiql) as a tool for GraphQL queries.

## Working example

![mutation](https://user-images.githubusercontent.com/1182522/35611013-f551f2b6-06a6-11e8-8f48-e39e667a8849.gif)

![query](https://user-images.githubusercontent.com/1182522/35611725-599e1e5a-06a9-11e8-9a52-9e5fd3542c2e.gif)


## Overview
  
  The reason why started supporting GraphQL is the `Label` used by S2Graph has a strong type system, so it will work well with the `schema` provided by GraphQL.
  
  So far, whenever GraphQL schema has been changed, it has been reflected in S2Graph Model (Service, Label... ).

## Setup
  Assume that hbase is running on localhost.  
  If the hbase environment is not set up, you should type the following commands.

```bash
sbt package
target/apache-s2graph-0.2.1-SNAPSHOT-incubating-bin/bin/hbase-standalone.sh start 
```
  
If hbase is running well, run the following command after cloning the project locally.

`GraphiQL` is not directly related to the `GraphQL` implementation, but is recommended for convenient queries.
Because of the license problem, you should download the file through the following command.

```bash
cd s2graphql/src/main/resources/assets
wget https://raw.githubusercontent.com/daewon/sangria-akka-http-example/master/src/main/resources/assets/graphiql.html

```

You can see that the `graphiql.html` file is added to the `s2graphql/src/main/resources/assets` folder as shown below.

```
$ls
graphiql.html
```

Then let's run http server.

```bash
sbt -DschemaCacheTTL=-1 -Dhttp.port=8000 'project s2graphql' '~re-start'
```

When the server is running, connect to `http://localhost:8000`. If it works normally, you can see the following screen.

![2018-01-31 4 39 25](https://user-images.githubusercontent.com/1182522/35610627-5ddd1cd6-06a5-11e8-8f02-446b28df54cb.png)

## API List
  - createService
  - createLabel
  - addEdges
  - addEdge
  - query (You can recursively browse the linked labels from the service and any other labels that are linked from that label)

## Your First Grpah (GraphQL version)

[S2Graph tutorial](https://github.com/apache/incubator-s2graph#your-first-graph)
The following content rewrote `Your first graph` to the GraphQL version.

### Start by connecting to `http://localhost:8000`.

The environment for this examples is Mac OS and Chrome.
You can get help with schema-based `Autocompletion` using the `ctrl + space` key.

If you add a `label` or `service`, etc. you will need to `refresh` (`cmd + r`) your browser because the schema will change dynamically.

#### 1. First, we need a name for the new service.

    The following POST query will create a service named "KakaoFavorites".

Request 
```graphql
mutation {
  Management {
    createService(
      name: "KakaoFavorites"
      compressionAlgorithm: gz      
    ) {
      object {
        name
      }
    }
  }
}
```

Response
```json
{
  "data": {
    "Management": {
      "createService": {
        "object": {
          "name": "KakaoFavorites"
        }
      }
    }
  }
}
```


#### 1.1 And create a `service column`` which is meta information for storing vertex.

    The following POST query will create a service column with the age attribute named "user"

Request
```graphql
mutation {
  Management {
    createServiceColumn(
      serviceName: KakaoFavorites
      columnName: "user"
      columnType: string
      props: {
        name: "age"
        dataType: int
        defaultValue: "0"
        storeInGlobalIndex: true
      }
    ) {
      isSuccess
      object {
        name
        props {
          name
          dataType          
        }
      }
    }
  }
}
```

Response
```json
{
  "data": {
    "Management": {
      "createServiceColumn": {
        "isSuccess": true,
        "object": {
          "name": "user",
          "props": [
            {
              "name": "age",
              "dataType": "int"
            }
          ]
        }
      }
    }
  }
}
```


To make sure the service and service column is created correctly, check out the following.

> Since the schema has changed, GraphiQL must recognize the changed schema. To do this, refresh the browser several times.

Request
```graphql
query {
  Management {
    Services(name:KakaoFavorites) {    
      name
      serviceColumns {
        name
        columnType
        props {
          name
          dataType
        }
      }
    }
  }
}
```

Response
```json
{
  "data": {
    "Management": {
      "Service": {
        "name": "KakaoFavorites",
        "serviceColumns": [
          {
            "name": "user",
            "columnType": "string",
            "props": [
              {
                "name": "age",
                "dataType": "int"
              }
            ]
          }
        ]
      }
    }
  }
}
```

#### 2. Next, we will need some friends.

    In S2Graph, relationships are organized as labels. Create a label called friends using the following createLabel API call:

Request 

```graphql
mutation {
  Management {
    createLabel(
      name: "friends"
      sourceService: {
        KakaoFavorites: {
          columnName: user
        }
      }
      targetService: {
        KakaoFavorites: {
          columnName: user
        }
      }
      consistencyLevel: strong
    ) {
      isSuccess
      message
      object {
        name
        serviceName
        tgtColumnName        
      }
    }
  }
} 
```

Response 
```json
{
  "data": {
    "Management": {
      "createLabel": {
        "isSuccess": true,
        "message": "Mutation successful",
        "object": {
          "name": "friends",
          "serviceName": "KakaoFavorites",
          "tgtColumnName": "user"
        }
      }
    }
  }
}
```

Check if the label has been created correctly
> Since the schema has changed, GraphiQL must recognize the changed schema. To do this, refresh the browser several times.

Request
```graphql
query {
  Management {
    Labels(name: friends) {
      name
      srcColumnName
      tgtColumnName
    }
  }
}
```

Response
```json
{
  "data": {
    "Management": {
      "Label": {
        "name": "friends",
        "srcColumnName": "user",
        "tgtColumnName": "user"
      }
    }
  }
}
```

Now that the label friends is ready, we can store the friendship data. 
Entries of a label are called edges, and you can add edges with edges/insert API:

> Since the schema has changed, GraphiQL must recognize the changed schema. To do this, refresh the browser several times.

Request
```graphql
mutation {
  addEdge(
    friends: [
      {from: "Elmo", to: "Big Bird"},
      {from: "Elmo", to: "Ernie"},    
      {from: "Elmo", to: "Bert"},    
      {from: "Cookie Monster", to: "Grover"},    
      {from: "Cookie Monster", to: "Kermit"},    
      {from: "Cookie Monster", to: "Oscar"},    
    ]
  ) {
    isSuccess    
  }
}
```

Response
```json
{
  "data": {
    "addEdge": [
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      }
    ]
  }
}
```

Query friends of Elmo with getEdges API:

Request

```graphql
query {
  KakaoFavorites {    
    user(id: "Elmo") {
      friends {
        user {
          id
        }
      }
    }
  }
}
```

Response

```json
{
  "data": {
    "KakaoFavorites": [
      {
        "friends": [
          {
            "to": "Bert"
          },
          {
            "to": "Ernie"
          },
          {
            "to": "Big Bird"
          }
        ]
      }
    ]
  }
}
```

Now query friends of Cookie Monster:

Request 

```graphql
query {
  KakaoFavorites {    
    user(id: "Elmo") {      
      friends {        
        user {
          id
        }
      }
    }
  }
}
```

Response

```json
{
  "data": {
    "KakaoFavorites": {
      "user": [
        {
          "friends": [
            {
              "to": {
                "id": "Ernie"
              }
            },
            {
              "to": {
                "id": "Big Bird"
              }
            },
            {
              "to": {
                "id": "Bert"
              }
            }
          ]
        }
      ]
    }
  }
}
```

Before next examples, you should add url to serviceColumn.

Request

```graphql
mutation {
  Management {
    createServiceColumn(
      serviceName: KakaoFavorites
      columnName: "url"
      columnType: string
    ) {
      isSuccess
      object {
        name
      }
    }
  }
}
```

Response

```json
{
  "data": {
    "Management": {
      "createServiceColumn": {
        "isSuccess": true,
        "object": {
          "name": "url"
        }
      }
    }
  }
}
```


#### 3. Users of Kakao Favorites will be able to post URLs of their favorite websites.

Request

```graphql
mutation {
  Management {
    createLabel(
      name: "post"
      sourceService: {
        KakaoFavorites: {
          columnName: user
        }
      }
      targetService: {
        KakaoFavorites: {
          columnName: url
        }
      }
      consistencyLevel: strong
    ) {
      isSuccess
      message
      object {        
        name      
      }
    }
  }
}
```

Response

```json
{
  "data": {
    "Management": {
      "createLabel": {
        "isSuccess": true,
        "message": "Mutation successful",
        "object": {
          "name": "post"
        }
      }
    }
  }
}
```

Now, insert some posts of the users:

> Since the schema has changed, GraphiQL must recognize the changed schema. To do this, refresh the browser several times.


Request

```graphql
mutation {
  addEdge(
    post: [
      { from: "Big Bird", to: "www.kakaocorp.com/en/main" },
      { from: "Big Bird", to: "github.com/kakao/s2graph" },
      { from: "Ernie", to: "groups.google.com/forum/#!forum/s2graph" },
      { from: "Grover", to: "hbase.apache.org/forum/#!forum/s2graph" },
      { from: "Kermit", to: "www.playframework.com"},
      { from: "Oscar", to: "www.scala-lang.org"}
    ]
  ) {
    isSuccess
  }
}
```

Response
```json
{
  "data": {
    "addEdge": [
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      },
      {
        "isSuccess": true
      }
    ]
  }
}
```

#### 4. So far, we have designed a label schema for the labels friends and post, and stored some edges to them.+

    This should be enough for creating the timeline feature! The following two-step query will return the URLs for Elmo's timeline, which are the posts of Elmo's friends:

Request

```graphql
query {
  KakaoFavorites {
    user(id: "Elmo") {
      id
      friends {
        user {
          id
          post {
            url {
              id
            }
          }
        }
      }
    }
  }
}
```

Response
```json
{
  "data": {
    "KakaoFavorites": {
      "user": [
        {
          "id": "Elmo",
          "friends": [
            {
              "user": {
                "id": "Ernie",
                "post": [
                  {
                    "url": {
                      "id": "groups.google.com/forum/#!forum/s2graph"
                    }
                  }
                ]
              }
            },
            {
              "user": {
                "id": "Bert",
                "post": []
              }
            },
            {
              "user": {
                "id": "Big Bird",
                "post": [
                  {
                    "url": {
                      "id": "github.com/kakao/s2graph"
                    }
                  },
                  {
                    "url": {
                      "id": "www.kakaocorp.com/en/main"
                    }
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```

Also try Cookie Monster's timeline:

Request
```graphql
query {
  KakaoFavorites {
    user(id: "Cookie Monster") {
      friends {      
        user {
          id
          post {
            url {
              id
            }
          }
        }
      }
    }
  }
}
```

Response
```json
{
  "data": {
    "KakaoFavorites": {
      "user": [
        {
          "friends": [
            {
              "user": {
                "id": "Oscar",
                "post": [
                  {
                    "url": {
                      "id": "www.scala-lang.org"
                    }
                  }
                ]
              }
            },
            {
              "user": {
                "id": "Kermit",
                "post": [
                  {
                    "url": {
                      "id": "www.playframework.com"
                    }
                  }
                ]
              }
            },
            {
              "user": {
                "id": "Grover",
                "post": [
                  {
                    "url": {
                      "id": "hbase.apache.org/forum/#!forum/s2graph"
                    }
                  }
                ]
              }
            }
          ]
        }
      ]
    }
  }
}
```


![2018-01-31 5 18 46](https://user-images.githubusercontent.com/1182522/35612101-db97e160-06aa-11e8-9286-0dd1ffa15c82.png)

The example above is by no means a full blown social network timeline, but it gives you an idea of how to represent, store and query graph data with S2Graph.

