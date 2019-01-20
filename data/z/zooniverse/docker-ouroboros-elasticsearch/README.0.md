h1. ElasticSearch

h2. A Distributed RESTful Search Engine

h3. "http://www.elasticsearch.org":http://www.elasticsearch.org

ElasticSearch is a distributed RESTful search engine built for the cloud. Features include:

* Distributed and Highly Available Search Engine.
** Each index is fully sharded with a configurable number of shards.
** Each shard can have one or more replicas.
** Read / Search operations performed on either one of the replica shard.
* Multi Tenant with Multi Types.
** Support for more than one index.
** Support for more than one type per index.
** Index level configuration (number of shards, index storage, ...).
* Various set of APIs
** HTTP RESTful API
** Native Java API.
** All APIs perform automatic node operation rerouting.
* Document oriented
** No need for upfront schema definition.
** Schema can be defined per type for customization of the indexing process.
* Reliable, Asynchronous Write Behind for long term persistency.
* (Near) Real Time Search.
* Built on top of Lucene
** Each shard is a fully functional Lucene index
** All the power of Lucene easily exposed through simple configuration / plugins.
* Per operation consistency
** Single document level operations are atomic, consistent, isolated and durable.
* Open Source under Apache 2 License.

h2. Getting Started

First of all, DON'T PANIC. It will take 5 minutes to get the gist of what ElasticSearch is all about.

h3. Installation

* "Download":http://www.elasticsearch.org/download and unzip the ElasticSearch official distribution.
* Run @bin/elasticsearch -f@ on unix, or @bin/elasticsearch.bat@ on windows.
* Run @curl -X GET http://localhost:9200/@.
* Start more servers ...

h3. Indexing

Lets try and index some twitter like information. First, lets create a twitter user, and add some tweets (the @twitter@ index will be created automatically):

<pre>
curl -XPUT 'http://localhost:9200/twitter/user/kimchy' -d '{ "name" : "Shay Banon" }'

curl -XPUT 'http://localhost:9200/twitter/tweet/1' -d '
{ 
    "user": "kimchy", 
    "postDate": "2009-11-15T13:12:00", 
    "message": "Trying out Elastic Search, so far so good?" 
}'

curl -XPUT 'http://localhost:9200/twitter/tweet/2' -d '
{ 
    "user": "kimchy", 
    "postDate": "2009-11-15T14:12:12", 
    "message": "Another tweet, will it be indexed?" 
}'
</pre>

Now, lets see if the information was added by GETting it:

<pre>
curl -XGET 'http://localhost:9200/twitter/user/kimchy?pretty=true'
curl -XGET 'http://localhost:9200/twitter/tweet/1?pretty=true'
curl -XGET 'http://localhost:9200/twitter/tweet/2?pretty=true'
</pre>

h3. Searching

Mmm search..., shouldn't it be elastic? 
Lets find all the tweets that @kimchy@ posted:

<pre>
curl -XGET 'http://localhost:9200/twitter/tweet/_search?q=user:kimchy&pretty=true'
</pre>

We can also use the JSON query language ElasticSearch provides instead of a query string:

<pre>
curl -XGET 'http://localhost:9200/twitter/tweet/_search?pretty=true' -d '
{ 
    "query" : { 
        "text" : { "user": "kimchy" }
    } 
}'
</pre>

Just for kicks, lets get all the documents stored (we should see the user as well):

<pre>
curl -XGET 'http://localhost:9200/twitter/_search?pretty=true' -d '
{ 
    "query" : { 
        "matchAll" : {} 
    } 
}'
</pre>

We can also do range search (the @postDate@ was automatically identified as date)

<pre>
curl -XGET 'http://localhost:9200/twitter/_search?pretty=true' -d '
{ 
    "query" : { 
        "range" : { 
            "postDate" : { "from" : "2009-11-15T13:00:00", "to" : "2009-11-15T14:00:00" } 
        } 
    } 
}'
</pre>

There are many more options to perform search, after all, its a search product no? All the familiar Lucene queries are available through the JSON query language, or through the query parser.

h3. Multi Tenant - Indices and Types

Maan, that twitter index might get big (in this case, index size == valuation). Lets see if we can structure our twitter system a bit differently in order to support such large amount of data.

ElasticSearch support multiple indices, as well as multiple types per index. In the previous example we used an index called @twitter@, with two types, @user@ and @tweet@.

Another way to define our simple twitter system is to have a different index per user (though note that an index has an overhead). Here is the indexing curl's in this case:

<pre>
curl -XPUT 'http://localhost:9200/kimchy/info/1' -d '{ "name" : "Shay Banon" }'

curl -XPUT 'http://localhost:9200/kimchy/tweet/1' -d '
{ 
    "user": "kimchy", 
    "postDate": "2009-11-15T13:12:00", 
    "message": "Trying out Elastic Search, so far so good?" 
}'

curl -XPUT 'http://localhost:9200/kimchy/tweet/2' -d '
{ 
    "user": "kimchy", 
    "postDate": "2009-11-15T14:12:12", 
    "message": "Another tweet, will it be indexed?" 
}'
</pre>

The above index information into the @kimchy@ index, with two types, @info@ and @tweet@. Each user will get his own special index.

Complete control on the index level is allowed. As an example, in the above case, we would want to change from the default 5 shards with 1 replica per index, to only 1 shard with 1 replica per index (== per twitter user). Here is how this can be done (the configuration can be in yaml as well):

<pre>
curl -XPUT http://localhost:9200/another_user/ -d '
{ 
    "index" : { 
        "numberOfShards" : 1, 
        "numberOfReplicas" : 1 
    } 
}'
</pre>

Search (and similar operations) are multi index aware. This means that we can easily search on more than one
index (twitter user), for example:

<pre>
curl -XGET 'http://localhost:9200/kimchy,another_user/_search?pretty=true' -d '
{ 
    "query" : { 
        "matchAll" : {} 
    } 
}'
</pre>

Or on all the indices:

<pre>
curl -XGET 'http://localhost:9200/_search?pretty=true' -d '
{ 
    "query" : { 
        "matchAll" : {} 
    } 
}'
</pre>

{One liner teaser}: And the cool part about that? You can easily search on multiple twitter users (indices), with different boost levels per user (index), making social search so much simpler (results from my friends rank higher than results from my friends friends).

h3. Distributed, Highly Available

Lets face it, things will fail....

ElasticSearch is a highly available and distributed search engine. Each index is broken down into shards, and each shard can have one or more replica. By default, an index is created with 5 shards and 1 replica per shard (5/1). There are many topologies that can be used, including 1/10 (improve search performance), or 20/1 (improve indexing performance, with search executed in a map reduce fashion across shards).

In order to play with Elastic Search distributed nature, simply bring more nodes up and shut down nodes. The system will continue to serve requests (make sure you use the correct http port) with the latest data indexed.

h3. Where to go from here?

We have just covered a very small portion of what ElasticSearch is all about. For more information, please refer to: .

h3. Building from Source

ElasticSearch uses "Maven":http://maven.apache.org for its build system.

In order to create a distribution, simply run the @mvn package -DskipTests@ command in the cloned directory.

The distribution will be created under @target/releases@.

h1. License

<pre>
This software is licensed under the Apache 2 license, quoted below.

Copyright 2009-2012 Shay Banon and ElasticSearch <http://www.elasticsearch.org>

Licensed under the Apache License, Version 2.0 (the "License"); you may not
use this file except in compliance with the License. You may obtain a copy of
the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations under
the License.
</pre>ElasticSearch Paramedic
=======================

Paramedic is a simple yet sexy tool to monitor and inspect [ElasticSearch](http://elasticsearch.org) clusters.

It displays real-time statistics and information about your nodes and indices,
as well as shard allocation within the cluster.

The application is written in JavaScript, using the [Ember.js](http://emberjs.com/) framework for sanity
and the [Cubism.js](http://square.github.com/cubism/) library for visuals. While the project is
_useful_, the codebase, with most logic in controllers, lacking proper component separation and test suite,
can't be considered mature enough, yet.

For basic overview, see a screenshot below.

![ElasticSearch Paramedic Screenshot](/karmi/elasticsearch-paramedic/raw/master/elasticsearch-paramedic-screenshot.png)


Installation
------------

The easiest way to check out the application is to open it in a modern browser:
**<http://karmi.github.com/elasticsearch-paramedic>**.

If you have ElasticSearch running on `http://localhost:9200`, you should see the stats for your cluster.

You can also download or clone this repository and open the `index.html` file in your browser:

    git clone git://github.com/karmi/elasticsearch-paramedic.git && cd elasticsearch-paramedic
    open index.html

The easiest way to use Paramedic in production is to install it as an ElasticSearch plugin:

    plugin -install karmi/elasticsearch-paramedic

If your cluster is publicly accessible (authenticated with firewall rules or HTTP Authentication via proxy),
open it in your browser:

    open http://localhost:9200/_plugin/paramedic/index.html


Overview
--------

The application displays basic information about your cluster: cluster name, health, number of nodes and shards,
etc., using the [Cluster Health](http://www.elasticsearch.org/guide/reference/api/admin-cluster-health.html) API.

The “Stats” chart displays key metrics from the
[Nodes Stats](http://www.elasticsearch.org/guide/reference/api/admin-cluster-nodes-stats.html) API,
updated every second.

The “Nodes” part displays the most important information about the cluster nodes (used disk space and memory,
number of nodes, machine load and ElasticSearch CPU consumption, etc.), using the
[Nodes Info](http://www.elasticsearch.org/guide/reference/api/admin-cluster-nodes-info.html) and
[Nodes Stats](http://www.elasticsearch.org/guide/reference/api/admin-cluster-nodes-stats.html) APIs.

The “Indices” part displays basic information about the indices: number of primary shards, number of replicas,
basic index statistics, using the
[Cluster State](http://www.elasticsearch.org/guide/reference/api/admin-cluster-state.html),
[Indices Status](http://www.elasticsearch.org/guide/reference/api/admin-indices-status.html) and
[Indices Stats](http://www.elasticsearch.org/guide/reference/api/admin-indices-stats.html) APIs.
Primary shards are displayed in _blue_, allocated replicas in _green_, unassigned replicas in _yellow_,
and unassigned (missing) primary shards in _red_.

To display shard allocation across the nodes, use the “Show Details” button. All information is updated periodically,
which allows you to see node and index statistics, shard initialization or relocation, etc. in real time.

Note, that a considerable number of Ajax calls is being performed, and launching the application
for large clusters, with large number of nodes and indices/shards, may leave your
browser unresponsive, or crash your machine. Try increasing the polling interval and hiding the charts
if you experience performance problems.

The application performance has been successfuly tested for clusters with around five nodes and sixty shards.


Similar Applications
--------------------

You are encouraged to try similar existing tools for ElasticSearch:

* [BigDesk](http://github.com/lukas-vlcek/bigdesk)
* [elasticsearch-head](http://github.com/mobz/elasticsearch-head)
* [Sematext SPM](http://sematext.com/spm)
* [Munin Plugins](https://gist.github.com/2159398)

-----

[Karel Minarik](http://karmi.cz)
