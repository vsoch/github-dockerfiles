# Mongo

Preparations and examples we'll be using through the workshop.


##Preparations

Build and run our mongo docker image. Beside mongodb (3.4.2) it has some data we will import.

    docker build -t cygni/mongo .
    docker run --name my-mongo -d cygni/mongo

After doing this in subsequent sessions just run `docker start my-mongo` to restart the container.
   
Load data. This executes `mongoimport` in a shell in the running container:

    docker exec -it my-mongo bash -c 'mongoimport --db test --collection restaurants --drop --file /my-data/restaurants.json'

We can now use the mongo shell within the container:
  
    docker exec -it my-mongo mongo

    
##Basic CRUD
    
1.Change db and insert some documents:
    
        use mydb
    
        db.mycollection.insert(
            { x : 1 }
        )
    
        db.mycollection.insert(
            [ { x : 3 },
              { y : "hello" },
              { x : 5, y : 6 }
             ]
        )


2.Read all documents:

        db.mycollection.find()
        
3.Read document by matching on a field:

        db.mycollection.find(
            { x : 5 }
        )
        
 (Later we'll work with more advanced queries.)

4.Replace a document (keep the _id):

        db.mycollection.update(
            { x : 5 },
            { z : 1}
        )
        
        db.mycollection.find()
        
5.Set a field:       

        db.mycollection.update(
            { z : 1 },
            { $set : { x : 5 } }
        )
        
        db.mycollection.find()
        
6.Increment a field:

        db.mycollection.update(
            { z : 1 },
            { $inc : { x : 2 } }
        )
                
        db.mycollection.find()
        
7.Remove a document:
        
        db.mycollection.remove(
            { y : "hello" }
        )
        
        db.mycollection.find()
        
8.Remove all documents:

        db.mycollection.remove({})
        
        db.mycollection.find()
        
## More advanced queries

We'll be using the data we imported when setting up our database.

9.Change db and read a document:

        use test
    
        db.restaurants.findOne()
    
10.Find by exact match on field (as in 3):
    
        db.restaurants.find(
            { name : "Wendy'S" }
        )
    
11.Same query but retrieve only _id and name:
    
        db.restaurants.find(
            { name : "Wendy'S" }, 
            { name : 1 }
        )
        
12.Remove _id:
    
        db.restaurants.find(
            { name : "Wendy'S" },
            { _id : 0, name : 1 }
        )
        
13.Match several fields (implicit 'and'):
    
        db.restaurants.find(
            { name : "Wendy'S",
             borough : "Bronx"
            },
            { _id : 0, name : 1, borough : 1 }
        )

14.Match using regular expressions:
    
        db.restaurants.find(
            { name : /^W/i },
            { _id : 0, name : 1 }
        )
        
15.'Or':
    
        db.restaurants.find(
            { $or : [ { name : "Wendy'S" }, { borough : "Bronx" } ] },
            { _id : 0, name : 1, borough : 1 }
        )
    
16.Nested documents:
    
        db.restaurants.find(
            { 'address.zipcode' :  /^111/ },
            { _id : 0, name : 1, 'address.zipcode' : 1 }
        )
    
17.Arrays:
    
        db.restaurants.find(
            { 'grades.score' : { $gte : 90 } },
            { _id : 0, name : 1, grades : 1 }
        )
    
18.And & or:
    
        db.restaurants.find(
            { $or: [ { cuisine : "Hotdogs" }, { cuisine : "Hamburgers" } ],
              borough :  "Queens"  
            },
            { _id : 0, name : 1, cuisine : 1 }
        )
    
19.The same but using '$in':
    
        db.restaurants.find(
            { cuisine : { $in : ["Hotdogs", "Hamburgers" ] },
             borough :  "Queens"  
            },
            { _id : 0, name : 1, cuisine : 1 }
        )
        
20.Explicit 'and':

         db.restaurants.find(
                     { 
                        $and: [{'grades.score' : { $lte : 10 }}, {'grades.score' : { $gte : 90 }} ]
                     },
                     { _id : 0, name : 1, grades : 1 }  
                 )
    
20.5.Element that completely matches criteria:

        db.restaurants.find(
            { grades : 
                { $elemMatch : { $and: [{score : { $lte : 10 }}, {score : { $gte : 90 }} ] } 
                } 
            },
            { _id : 0, name : 1, grades : 1 }  
        )
    
        db.restaurants.find(
            { grades : 
                { $elemMatch : { score : { $gte: 90 }, 
                                 date: { $gte: ISODate("2014-01-01") } } } 
            },
            { _id : 0, name : 1, grades : 1 }  
        )
        
### Querying Exercises  
1. Find name and street of all bakeries in Queens with a score (in any year) between 25 and 75. 
2. Find name of all restaurants which were not graded in 2012. 

[Query operators](https://docs.mongodb.com/manual/reference/operator/query/)
    


        
## Indexes (aka Indices)

21.Analyse execution of a query:

        db.restaurants.find(
            { name : /^W/ }
        ).explain("executionStats")
        
22.Create an index on name:
    
        db.restaurants.createIndex({ name : 1 })
        
23.Analyse again as in 21. Boom.

## Aggregation (i.e. queries + processing)
 
 There's 3 ways to do it. Simple, pipelines and mapReduce.

### Simple aggregation

24.Count all:

        db.restaurants.count()
        
25.Count after filtering:
    
        db.restaurants.count( { name : "White Castle"} )
    
26.Distinct field values on all documents:

        db.restaurants.distinct('cuisine')

27.Distinct filed values after filtering:
    
        db.restaurants.distinct('name', { cuisine : 'Japanese' })
        
### Aggregation pipelines        
    
28.Number of restaurants of each "cuisine" in the Bronx:

        db.restaurants.aggregate(
            { $match : { borough : "Bronx" } },
            { $group : { _id : "$cuisine", count: { $sum : 1 } } },
            { $sort : { count : -1} } 
        )
        
29.Distribution of scores (of last "grade") of american-cuisine restaurants in Manhattan:

        db.restaurants.aggregate(
            { $match : { borough: "Manhattan", cuisine: "American" } },
            { $project: { name: 1, grades: 1} },
            { $unwind: { path: "$grades", preserveNullAndEmptyArrays: true }},
            { $project: { name: 1, grade: "$grades" } },
            { $sort: { 'grade.date': -1, 'grade.score': -1 } },
            { $group: { _id: {id: "$_id", name: "$name"} , lastScore: { $first: "$grade.score" } } },
            { $bucket: { groupBy: "$lastScore", boundaries: [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], default: "not scored" }}
        )

30.Same as before but also list top 5 by last score:

        db.restaurants.aggregate(
            { $match : { borough: "Manhattan", cuisine: "American" } },
            { $project: { name: 1, grades: 1} },
            { $unwind: { path: "$grades", preserveNullAndEmptyArrays: true }},
            { $project: { name: 1, grade: "$grades" } },
            { $sort: { 'grade.date': -1, 'grade.score': -1 } },
            { $group: { _id: {id: "$_id", name: "$name"} , lastScore: { $first: "$grade.score" } } },
            { $facet: {
                "scoreDistribution": [ 
                    { $bucket: { groupBy: "$lastScore", boundaries: [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], default: "not scored" }} 
                ],
                "topFive": [ 
                    { $sort: { lastScore: -1 } }, 
                    { $limit: 5 },
                    { $project: { name: "$_id.name", _id:0, lastScore: 1}} 
                ]
            }   }
        )
        
#### Pipeline exercise
Find out the number of Turkish restaurants per borough and the name of the best one in 2011 per borough.

[Aggregation pipeline operators docs](https://docs.mongodb.com/manual/reference/operator/aggregation/)
        
31.The pipeline gets optimized. In this case the stages get rearranged:
        
        db.restaurants.aggregate(
            [
                { $sort: { 'addres.zipcode': 1 } },
                { $match: { 'address.zipcode' : /^110/ } }
            ], 
            { explain : true }
        )
           
32.All three stages get fused into one, thanks to optimization and index:

        db.restaurants.aggregate(
            [
                { $match: { name : /^B/ } },
                { $sort: { name : 1 } },
                { $limit: 20 }
            ], 
            { explain : true }
        )

33.Compare previous to this. Some optimization but not as thorough:

         db.restaurants.aggregate(
            [
                { $match: { cuisine : /^B/ } },
                { $sort: { cuisine : 1 } },
                { $limit: 20 }
            ], 
            { explain : true }
         )
                  


### mapReduce

34.Number of restaurants of each "cuisine" in the Bronx (same as 28):
    
        db.restaurants.mapReduce(
            function() { emit(this.cuisine,  1 ); },
            function(cuisine, counts) { return Array.sum(counts) },
            {
                query : { borough : "Bronx" },
                out : "mr_results"
            }
        )
        
35.Distribution of scores (of last "grade") of american-cuisine restaurants in Manhattan (same as 29):

        db.restaurants.mapReduce(
            function() { 
                var bucket = "not scored";
                if (this.grades && this.grades.length > 0) {
                    var latestScore = this.grades.sort((g1, g2) => g2.date.getTime() - g1.date.getTime())[0].score;
                    if (latestScore !== null) {
                        bucket = 10 * Math.floor(latestScore / 10);
                    }
                }
                emit(bucket, 1);
            },
            function(name, scores) {
                return Array.sum(scores)
            },
            {
                query: { borough: "Manhattan", cuisine: "American" },
                out: "mr_results"
            }
        )

#### mapReduce exercise

Find out the number of Turkish restaurants per borough and the name of the best one in 2011 per borough. (Same as in pipeline) 

[mapReduce docs](https://docs.mongodb.com/manual/reference/command/mapReduce/#dbcmd.mapReduce)

### Replication and sharding

We'll create a cluster with 2 shards in which each shard is a replica set. 
In total there will be 6 data-bearing nodes, 3 config nodes and 1 router node.

36.Create network
        
        docker network create -d bridge mongo-cluster
   
37.Run and init config replica set

        docker run --name mongoconf0 -d --network=mongo-cluster cygni/mongo --configsvr --replSet "rsconf" --port 27017
        docker run --name mongoconf1 -d --network=mongo-cluster cygni/mongo --configsvr --replSet "rsconf" --port 27017
        docker run --name mongoconf2 -d --network=mongo-cluster cygni/mongo --configsvr --replSet "rsconf" --port 27017
        
        docker exec -it mongoconf0 mongo
        
        rs.initiate( {
           _id : "rsconf",
           configsvr: true,
           members: [
            { _id : 0, host : "mongoconf0" },
            { _id : 1, host : "mongoconf1" },
            { _id : 2, host : "mongoconf2" }
           ]
        })
        
38.Run and init data-bearing replica sets

        docker run --name mongo00 -d --network=mongo-cluster cygni/mongo --shardsvr --replSet "rs0" --port 27017
        docker run --name mongo01 -d --network=mongo-cluster cygni/mongo --shardsvr --replSet "rs0" --port 27017
        docker run --name mongo02 -d --network=mongo-cluster cygni/mongo --shardsvr --replSet "rs0" --port 27017
        
        docker exec -it mongo00 mongo
        
        rs.initiate( {
           _id : "rs0",
           members: [
            { _id : 0, host : "mongo00" },
            { _id : 1, host : "mongo01" },
            { _id : 2, host : "mongo02" }
           ]
        })
        
        
        docker run --name mongo10 -d --network=mongo-cluster cygni/mongo --shardsvr --replSet "rs1" --port 27017
        docker run --name mongo11 -d --network=mongo-cluster cygni/mongo --shardsvr --replSet "rs1" --port 27017
        docker run --name mongo12 -d --network=mongo-cluster cygni/mongo --shardsvr --replSet "rs1" --port 27017
        
        
        docker exec -it mongo10 mongo
        
        rs.initiate( {
           _id : "rs1",
           members: [
            { _id : 0, host : "mongo10" },
            { _id : 1, host : "mongo11" },
            { _id : 2, host : "mongo12" }
           ]
        })
        
39.Run router and register shards

        docker run --name mongos -d --network=mongo-cluster cygni/mongo mongos --port 27017 --configdb "rsconf"/mongoconf0:27017
        
        docker exec -it mongos mongo
        
        sh.addShard("rs0/mongo00")
        sh.addShard("rs1/mongo10")
        
40.Configure sharding for the collection

        sh.enableSharding("test")
        
        sh.shardCollection("test.restaurants", { name: "hashed" })
     
41.Upload data (from another terminal)
    
        docker exec -it mongos bash -c 'mongoimport --db test --collection restaurants --file /my-data/restaurants.json'
    
42.Run aggregation queries from router (mongos)

        db.restaurants.aggregate(
                    { $match : { borough: "Manhattan", cuisine: "American" } },
                    { $project: { name: 1, grades: 1} },
                    { $unwind: { path: "$grades", preserveNullAndEmptyArrays: true }},
                    { $project: { name: 1, grade: "$grades" } },
                    { $sort: { 'grade.date': -1, 'grade.score': -1 } },
                    { $group: { _id: {id: "$_id", name: "$name"} , lastScore: { $first: "$grade.score" } } },
                    { $facet: {
                        "scoreDistribution": [ 
                            { $bucket: { groupBy: "$lastScore", boundaries: [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], default: "not scored" }} 
                        ],
                        "topFive": [ 
                            { $sort: { lastScore: -1 } }, 
                            { $limit: 5 },
                            { $project: { name: "$_id.name", _id:0, lastScore: 1}} 
                        ]
                    }   }
                )
                
        db.restaurants.aggregate(
                    { $match : { borough: "Manhattan", cuisine: "American" } },
                    { $project: { name: 1, grades: 1} },
                    { $unwind: { path: "$grades", preserveNullAndEmptyArrays: true }},
                    { $project: { name: 1, grade: "$grades" } },
                    { $sort: { 'grade.date': -1, 'grade.score': -1 } },
                    { $group: { _id: {id: "$_id", name: "$name"} , lastScore: { $first: "$grade.score" } } },
                    { $facet: {
                        "scoreDistribution": [ 
                            { $bucket: { groupBy: "$lastScore", boundaries: [-10, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], default: "not scored" }} 
                        ],
                        "topFive": [ 
                            { $sort: { lastScore: -1 } }, 
                            { $limit: 5 },
                            { $project: { name: "$_id.name", _id:0, lastScore: 1}} 
                        ]
                    }   }
                )
                
43.Take down some nodes and see what happens
