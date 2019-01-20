```
# download hadoop conf before building
docker build -t hdp-spark2-client .

# submit spark job
docker run --rm --volume /usr/local/spark2/examples/:/jars --network host hdp-spark2-client spark-submit --master yarn --class org.apache.spark.examples.SparkPi /jars/spark-examples*

# hadoop hdfs client
docker run --rm --volume hadoop fs -ls /
```
