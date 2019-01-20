# HBase
HBase is an implementation of Google's Bigtable. It is built on top of Zookeeper, Hadoop and HDFS. Because of the strong relationship with Hadoop we will run HBase as it is most commonly used; together with Zookeeper and Hadoop.

## Table of Contents
* [Resources](#resources)
* [Before we start](#before-we-start)
    * [Create network](#create-network)
    * [Start Zookeeper+Hadoop+HBase+Hue](#start-zk-hdp-hbase-hue)
    * [Check logs](#check-logs)
    * [Check ps](#check-ps)
    * [Check stats](#check-stats)
    * [Run HBase shell](#run-hbase-shell)
    * [Browse HUE](#browse-hue)
    * [Browse HDFS](#browse-hdfs)
* [Exercises](#exercises)
    * [Getting used to the HBase shell](#getting-used-to-the-hbase-shell)
    * [Working with versions](#working-with-versions)
    * [Filtering](#filtering)
    * [Streaming media into HBase](#streaming-media-into-hbase)
    * [Regions and partitioning](#regions-and-partitioning)

## <a name="resource"></a>Resources
* HBase - [http://hbase.apache.org](http://hbase.apache.org)
* Hadoop - [http://hadoop.apache.org](http://hadoop.apache.org)
* HDFS - [https://wiki.apache.org/hadoop/HDFS](https://wiki.apache.org/hadoop/HDFS)
* Zookeeper - [http://zookeeper.apache.org](http://zookeeper.apache.org)
* Hue - [http://gethue.com](http://gethue.com)

## <a name="before-we-start"></a>Before we start
Before we start make sure you have cloned the repository to a directory of choice.
```
$ git clone http://github.com/cygni/cygni-competence-7-databases
```
### <a name="create-network"></a>Create network
```
$ docker network create --driver=bridge vnet
ba4b3a73006145d3b5346b19c019351b0d33bd228ed20f2da50f0193507b1b02
$ docker network ls
```
__Sample output:__
```
NETWORK ID     NAM      DRIVER      SCOPE
ba4b3a730061   vnet     bridge      local
```
### <a name="start-zk-hdp-hbase-hue"></a>Start Zookeeper+Hadoop+HBase+Hue
```
$ docker-compose up -d --build
```
__Sample output:__
```
Pulling zookeeper (wurstmeister/zookeeper:latest)...
latest: Pulling from wurstmeister/zookeeper
a3ed95caeb02: Pull complete
ef38b711a50f: Downloading [===============================>                   ] 42.71 MB/67.5 MB
e057c74597c7: Download complete
666c214f6385: Download complete
c3d6a96f1ffc: Download complete
3fe26a83e0ca: Download complete
3d3a7dd3a3b1: Downloading [==========>                                        ] 23.25 MB/109.9 MB
f8cc938abe5f: Download complete
9978b75f7a58: Download complete
4d4dbcc8f8cc: Download complete
6e2141080cee: Download complete
7b01624d9a37: Download complete
438e659516b8: Waiting
...
...
Building hadoop
Step 1/8 : FROM sequenceiq/hadoop-docker:2.7.1
 ---> 42efa33d1fa3
...
...
Creating zookeeper
Creating hadoop
Creating hbase
Creating hue
```

### <a name="check-logs"></a>Check logs
```
$ docker-compose logs -f
```
### <a name="check-ps"></a>Check ps
```
$ docker-compose ps
```
__Sample output:__
```
     Name                            Command                           State                     Ports                      
------------------------------------------------------------------------------------------------------------------------
hadoop                        /etc/bootstrap.sh -d                      Up                0.0.0.0:9000->9000/tcp                          
hbase                         /bin/sh -c "/usr/local/hba ...            Up                0.0.0.0:9090->9090/tcp  
hue                           ./build/env/bin/hue runser ...            Up                0.0.0.0:8888->8888/tcp                          
zookeeper                     /bin/sh -c /usr/sbin/sshd  ...            Up                0.0.0.0:2181->2181/tcp       
```

### <a name="check-stats"></a>Check stats
```
$  docker ps --format {{.Names}} | xargs docker stats
```
__Sample output:__
```
CONTAINER   CPU %    MEM USAGE / LIMIT       MEM %     NET I/O             BLOCK I/O           PIDS
hue         2.47%    148.5 MiB / 1.952 GiB   7.43%     3.44 MB / 41.8 MB   97.2 MB / 29 MB     3
hbase       0.62%    336.4 MiB / 1.952 GiB   16.83%    737 kB / 866 kB     167 MB / 147 kB     60
hadoop      4.43%    944.6 MiB / 1.952 GiB   47.25%    778 kB / 1.02 MB    176 MB / 6.52 MB    409
zookeeper   0.21%    75.96 MiB / 1.952 GiB   3.80%     405 kB / 330 kB     39 MB / 340 kB      21
```
### <a name="run-hbase-shell"></a>Run HBase shell
Verify you can access hbase shell by running the following command:
```
$ docker exec -it hbase bash -c "hbase shell"
```
__Sample output:__
```
Version 1.2.4, r67592f3d062743907f8c5ae00dbbe1ae4f69e5af, Tue Oct 25 18:10:20 CDT 2016

hbase(main):001:0> 
```
Type _exit_ to leave hbase shell.

### <a name="browse-hue"></a>Browse HUE
Verify you can visit [http://localhost:8888/hbase](http://localhost:8888/hbase)

__IMPORTANT!__ When prompted for username/password then enter:

username: __hue__
password: __hue__

![alt text][hue-first-page]

![alt text][hue-hbase-page]

### <a name="browse-hdfs"></a>Browse HDFS
Verify you can visit [http://localhost:50070/explorer.html](http://localhost:50070/explorer.html)

![alt text][hadooop-hdfs-explorer-page]

## <a name="excercises"></a>Exercises
### <a name="getting-used-to-the-hbase-shell"></a>Getting used to the HBase shell
You can find good information regarding data modelling in HBase at [https://hbase.apache.org/book.html#datamodel](https://hbase.apache.org/book.html#datamodel)

1. Trying out various commands on tables, rows and columns.

    Open HBase shell by running
    ```
    docker exec -it hbase bash -c "hbase shell"
    ```

    Create __table__ _test_ with __column family__ _cf_ 
    ```
    > create 'test', 'cf'
    > alter 'test', NAME => 'cf', VERSIONS => 5
    ```
    __List__ table test
    ```
    > list 'test'
    ```
    __Put__ some values to the table and column 
    ```
    > put 'test', 'row1', 'cf:a', 'value1'
    > put 'test', 'row1', 'cf:a', 'some new value'
    > put 'test', 'row2', 'cf:b', 'value2'
    > put 'test', 'row3', 'cf:c', 'value3'
    ```
    __Scan__ table _test_
    ```
    > scan 'test'
    ```
    __Get__ row from table _test_ based on row key 
    ```
    > get 'test', 'row1'
    ```

2. Figure out how to use the shell to do the following:
    * Delete individual column values within a row
    * Delete an entire row
    * Get multiple versions on column
    
3. Cleanup

    __Disable__ table _test_ 
    ```
    > disable 'test'
    ```
    __Drop__ table _test_ 
    ```
    > drop 'test'
    ```
### <a name="working-with-versions"></a>Working with versions
1. Create table and alter column 'cf' for how to handle versions
    ```
    create 'mytable', 'cf'
    alter 'mytable', NAME => 'cf', VERSIONS => 5
    alter 'mytable', NAME => 'cf', MIN_VERSIONS => 2
    alter 'mytable', NAME => 'cf', TTL => 15
    ```
2. Add some values to the column family on the very same row key
    ```
    put 'mytable', 'some fancy key', 'cf:a', 'old value'
    put 'mytable', 'some fancy key', 'cf:a', 'newer value'
    put 'mytable', 'some fancy key', 'cf:a', 'even newer value'
    put 'mytable', 'some fancy key', 'cf:a', 'newest value'
    ```
3. Fetch values from column family a couple of times and watch old version be deleted. E.g.
    ```
    get 'mytable', 'some fancy key', {TIMERANGE => [0, 1690618847570], VERSIONS => 10}
    ```
    
### <a name="filtering"></a>Filtering
__HINT:__ Use command _show_filters_ to list all available filters within HBase shell.

When reading data from HBase using Get or Scan operations, you can use custom filters to return a subset of results to the client. While this does not reduce server-side IO, it does reduce network bandwidth and reduces the amount of data the client needs to process. Filters are generally used using the Java API, but can be used from HBase Shell for testing and debugging purposes.

#### Logical Operators, Comparison Operators and Comparators
Filters can be combined together with logical operators. Some filters take a combination of comparison operators and comparators. Following is the list of each.

__Logical Operators__

* AND - the key-value must pass both the filters to be included in the results.
* OR - the key-value must pass at least one of the filters to be included in the results.
* SKIP - for a particular row, if any of the key-values do not pass the filter condition, the entire row is skipped.
* WHILE - For a particular row, it continues to emit key-values until a key-value is reached that fails the filter condition.
* Compound Filters - Using these operators, a hierarchy of filters can be created. For example:
    ```
    (Filter1 AND Filter2)OR(Filter3 AND Filter4)
    ```
__Comparison Operators__

* LESS (<)
* LESS_OR_EQUAL (<=)
* EQUAL (=)
* NOT_EQUAL (!=)
* GREATER_OR_EQUAL (>=)
* GREATER (>)
* NO_OP (no operation)

__Comparators__

* BinaryComparator - lexicographically compares against the specified byte array using the Bytes.compareTo(byte[], byte[]) method.
* BinaryPrefixComparator - lexicographically compares against a specified byte array. It only compares up to the length of this byte array.
* RegexStringComparator - compares against the specified byte array using the given regular expression. Only EQUAL and NOT_EQUAL comparisons are valid with this comparator.
* SubStringComparator - tests whether or not the given substring appears in a specified byte array. The comparison is case insensitive. Only EQUAL and NOT_EQUAL comparisons are valid with this comparator.

__Examples__ 
```
Example1: >, 'binary:abc' will match everything that is lexicographically greater than "abc"
Example2: =, 'binaryprefix:abc' will match everything whose first 3 characters are lexicographically equal to "abc"
Example3: !=, 'regexstring:ab*yz' will match everything that doesn't begin with "ab" and ends with "yz"
Example4: =, 'substring:abc123' will match everything that begins with the substring "abc123"
```

__HBase shell sample__
```
> scan 'wiki', {RAW => true, LIMIT => 2, FILTER => "SingleColumnValueFilter('revision','author',=,'binary:LlywelynII')"}
```

### <a name="streaming-media-into-hbase"></a>Streaming media into HBase   
1. Create table 'wiki'
    ```
    $ docker exec -it hbase bash -c "hbase shell"
    > create 'wiki', 'text'
    ```
2. Alter the table
    ```
    > alter 'wiki', { NAME => 'text', VERSIONS => org.apache.hadoop.hbase.HConstants::ALL_VERSIONS }
    > alter 'wiki', { NAME => 'revision', VERSIONS => org.apache.hadoop.hbase.HConstants::ALL_VERSIONS }
    ```
3. Exit shell
    ```
    > exit
    ```    
4. Download, extract and feed HBase with wikipedia data via the following command:
    ```jruby
    docker exec -it hbase bash -c "curl https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2 | bzcat | hbase shell /usr/local/code/import_from_wikipedia.rb"
    ```
    You should see output like this eventually:
    ```
    500 records inserted (Ashmore and Cartier Islands)
    1000 records inserted (Annealing)
    1500 records inserted (Ajanta Caves)
    ...
    ```
    You probably want to shut it down after a while. Just press Ctrl+C
    
5. Search all wiki articles written by some author (column=revision:author) 
    
    __Hint 1:__ List all available filters in hbase shell by typing _show_filters_
    __Hint 2:__ scan 'table', {RAW => true ... } fetches all columns for matching row

6. After stopping the script above visit [http://localhost:8888/filebrowser/#/hbase/data/default/wiki](http://localhost:8888/filebrowser/#/hbase/data/default/wiki)
   
    The long-named subdirectories you see represents individual regions.
    
### <a name="regions-and-partitioning"></a>Regions and partitioning   
In HBase, rows are kept in order, sorted by the row key. A region is a chunk of rows, identified by the starting key (inclusive) and the ending key (exclusive).

Regions never overlap, and each is assigned to a specific region server in the cluster. In our setup, there is only one region server, which will always be responsible for all regions.

1. Split regions manually on table 'wiki'
    ```
    $ docker exec -it hbase bash -c "hbase shell"
    > split 'wiki'
    ```
    Verify number of regions increased in Hue as expected.

2. Get info from meta-table regarding which region server is responsible.
    ```
    scan 'hbase:meta', {COLUMNS => [ 'info:server', 'info:regioninfo' ] }
    ```
    
3. But also the hbase:meta table is split into regions and spread across the cluster. Discuss with your neighbor: _How do the region servers know which regions they're responsible for serving?_

[hue-first-page]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/hbase/hue-first-page.png?raw=true "Hue First Page"
[hue-hbase-page]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/hbase/hue-hbase-page.png?raw=true "Hue Hbase Page"
[hadooop-hdfs-explorer-page]: https://github.com/cygni/cygni-competence-7-databases/blob/screenshots/hbase/hadoop-hdfs-explorer-page.png?raw=true "Hue Hbase Page"
