# Project Idea 
My project explores the challenge of containerizing a data engineering pipeline with a database.
To help achieve this challenge, I will be using the [work of Eric Pinkham](https://github.com/ericapinkham/Insight_DE_GUS.git), an Insight Data Engineering
fellow of the 2018B session, and containerize his project.  

# Demo
https://www.youtube.com/watch?v=Mz_iTK0GiQo

Shows working Python front end, Kubernetes dashboard displaying HDFS/Spark on a cluster, CockroachDB dashboard,
Kubernetes Stateful Set of CockroachDB, and the automatic recovery of restarting a failed CockroachDB pod worker.

## Purpose / common use case
In 2013, Docker was created and helped popularized the container technology. Many companies embraced containers,
because they were not only less resource intensive than a virutal machine, but also portable as well. Even though
a few years has passed since Docker was first founded, the push for container adoption is still very strong. In 2017,
the Portworx Container Adoption Survey has found that at least 32% of companies they surveyed spended at least $500k
or more on this technology, which was up 5% from the last time the survey was conducted in 2016. Yet despite this growth,
the same 2017 survey has also found that 38% of companies cite data as the #1 bottleneck towards container adoption, and 
this is where my project comes in.

My project aims to explore the challenge of containerizing a database. 
Because of their portability and efficiency on using system resources, containers are increasingly
being adopted by many companies. But the database is one of the hardest challenges to container 
adoption due to problems like data insecurity and specific hardware requirements required to run it. 
By containerizing a database, developers will be one step closer towards a fully containerized pipeline. 
In addition, by running a database on containers, we get performance benefits which may not be possible 
from running a database using virtualization. 

## Technologies well suited to solve the potential challenges

From Eric's pipeline: Hadoop HDFS, Apache Spark, Cockroach DB, Dash

New Technologies adopted: Docker, Kubernetes, Kops 

## Architecture

Take Eric's work and encompass each aspect of his app (Hadoop HDFS, Apache Spark, Cockroach DB, Dash) inside a Docker container image. Kubernetes will then be used to coordinate the communication between the containers that host different aspects of the application. 

In particular, I have one Kubernetes cluster running Spark and Hadoop HDFS together, another Kubernetes cluster running
CockroachDB, and a simple Docker container to display the web user interface. 

![Dashboard](./picAssets/frontEnd.png)

![cock](./picAssets/cockroachDB.png)

## Overall Setup

To get this project up and running, you will need to create the clusters, configure the cluster for Hadoop HDFS,
configure cluster for CockroachDB, configure the Python Front end set up, create the sbt jar file Spark will use,
configure the SAME cluster HDFS is on to run Spark as well, and then you can see the pipeline in action by 
running the commands within pipeline-commands.txt

[Create Kubernetes cluster](https://github.com/cldevrun/Insight18/tree/master/aws)

[Configure cluster for HDFS](https://github.com/cldevrun/Insight18/tree/master/hadoop)

[Configure cluster for CockroachDB](https://github.com/cldevrun/Insight18/tree/master/cockroachDB)

[Configure the Python Front End](https://github.com/cldevrun/Insight18/tree/master/python/pythonFrontEnd)

[Create the sbt jar file](https://github.com/cldevrun/Insight18/tree/master/src/main/scala/Jobs)

[Configure cluster for HDFS AND SPARK now](https://github.com/cldevrun/Insight18/tree/master/spark)

[Run commands](https://github.com/cldevrun/Insight18/blob/master/pipeline-commands.txt)

# Sources

[Eric Pinkham's data pipeline](https://github.com/ericapinkham/Insight_DE_GUS.git)

[Install Spark on AWS](https://sparkour.urizone.net/recipes/installing-ec2/)

[Maven Repo for Spark Releases](https://mvnrepository.com/artifact/org.apache.spark/spark-core_2.11/2.1.0)

[Overriding Jackson Dependencies incompatibilities](https://stackoverflow.com/questions/43841091/spark2-1-0-incompatible-jackson-versions-2-7-6)

[Python ODBC Docker dependency](https://stackoverflow.com/questions/46405777/connect-docker-python-to-sql-server-with-pyodbc)

[STS:AssumeRole](https://github.com/aws/aws-cli/issues/2279)

[Kubernetes command cheat sheet](https://carlos.mendible.com/2018/03/18/my-kubectl-cheat-sheet/)

[Spark K8s example](https://github.com/kubernetes/examples/tree/master/staging/spark)

[Run Scala Spark shell within master controller](http://blog.madhukaraphatak.com/scaling-spark-with-kubernetes-part-6/)

[K8s services in different namespaces](https://stackoverflow.com/questions/37221483/kubernetes-service-located-in-another-namespace)

[Assigning namespaces to contexts](https://dzone.com/articles/the-why-and-how-of-kubernetes-namespaces)

[Exposing K8s ports](http://alesnosek.com/blog/2017/02/14/accessing-kubernetes-pods-from-outside-of-the-cluster/)

[spark-submit with k8s](https://banzaicloud.com/blog/spark-k8s-internals/)

[2.3.1 Spark Docker image from Google](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/master/manifest/spark-operator.yaml)

[Spark master and driver](https://stackoverflow.com/questions/34722415/understand-spark-cluster-manager-master-and-driver-nodes)

[kops command line options](https://github.com/kubernetes/kops/blob/master/docs/cli/kops_create_cluster.md)

[Spark master out of sync with workers](https://stackoverflow.com/questions/29982559/unable-to-run-sparkpi-on-apache-spark-cluster)

[Spark Resource Allocation](http://site.clairvoyantsoft.com/understanding-resource-allocation-configurations-spark-application/)

[K8s dashboard with kops](https://ramhiser.com/post/2018-05-20-setting-up-a-kubernetes-cluster-on-aws-in-5-minutes/)

[K8s dashboard ui update](https://github.com/kubernetes/dashboard/wiki/Accessing-Dashboard---1.7.X-and-above)

[See K8s cpu/mem graphs in dashboard](https://github.com/kubernetes/dashboard/issues/1867)

[Restart a K8s pod](https://stackoverflow.com/questions/40259178/how-to-retry-image-pull-in-a-kubernetes-pods)
