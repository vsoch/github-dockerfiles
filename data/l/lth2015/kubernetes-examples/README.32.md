Use Kafka cluster in Kubernetes cluster
================

### Why use Pod not Replicationcontroller?
----
##### Kafka通过BROKER_ID来识别自身，在注册到zookeeper中时，注册的名字默认为容器的主机名，如果用rc的话，pod的名称是带上一定的前缀随机生成的，
##### 容器中其他节点不能通过这个随机生成的hostname来寻址，解决方案是：在容器启动时，将容器的eth0的ip作为kafka注册到zookeeper集群中的主机名，
##### 这样，其它kafka节点和覆盖网络内部的组件就可以访问kafka，并能写入数据。
---- 
##### 在这样做之前，kafka集群可以创建topic，也可显示、列出topic，producer不能写入，原因是kafka的配置中(server.properties)中要配置host.name和advertised.port,问题类似[Kafka Producer Can't Fetch Metadata Problem](stackoverflow.com/questions/30606447/kafka-consumer-fetching-metadata-for-topics-failed)
##### 由于brokerid等都是在容器创建后、kafka启动前用入口脚本替换相应的配置，还有ceph存储写入的问题，所以我们使用同一的RC，对于Pod我们也可以设置自动重启，所以，对已一个的Pod，RC和Pod从这点说没有什么区别
##### Pod的metadata的name就是pod容器运行后的hostname

##### Edit kafka-pods/kafka-1-pod.json
```json
{
  "spec": {
    "volumes": [
      {
        "rbd": {
          "readOnly": false,
          "fsType": "xfs",
          "secretRef": {
            "name": "ceph-secret"
          },
          "user": "admin",
          "image": "kafka-1",
          "pool": "rbd",
          "monitors": [
            "10.149.149.3:6789"
          ]
        },
        "name": "kafka-1"
      }
    ],
    "restartPolicy": "Always",
    "containers": [
      {
        "volumeMounts": [
          {
            "name": "kafka-1",
            "mountPath": "/tmp/kafka-logs"
          }
        ],
        "resources": {
          "limits": {
            "memory": "20480M",
            "cpu": "20"
          },
          "requests": {
            "memory": "8192M",
            "cpu": "10"
          }
        },
        "args": [
          "sed -i -- 's/broker.id=0/broker.id=1/g' /home/kafka/config/server.properties &&  IP=`ifconfig eth0 |  grep 'inet addr:' | awk -F ':' '{print $2}' | awk '{print $1}'` && echo $IP &&  sed -i -- \"s/host.name=KAFKA/host.name=$IP/g\" /home/kafka/config/server.properties && sed -i -- 's/advertised.port=KAFKA/advertised.port=9092/g' /home/kafka/config/server.properties && sed -i -- 's/num.network.threads=3/num.network.threads=10/g' /home/kafka/config/server.properties && sed -i -- 's/num.io.threads=8/num.io.threads=20/g' /home/kafka/config/server.properties && sed -i -- 's/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper-1:2181,zookeeper-2:2181,zookeeper-3:2181,zookeeper-4:2181,zookeeper-5:2181/g' /home//kafka/config/server.properties && /home/kafka/bin/kafka-server-start.sh /home/kafka/config/server.properties "
        ],
        "command": [
          "/bin/sh",
          "-c"
        ],
        "ports": [
          {
            "containerPort": 9092
          }
        ],
        "image": "registry.docker:5000/company/kafka:2.11-0.9.0",
        "name": "kafka-1"
      }
    ]
  },
  "metadata": {
    "name": "kafka-1",
    "labels": {
      "component": "kafka",
      "role": "kafka-1"
    }
  },
  "kind": "Pod",
  "apiVersion": "v1"
}
```
[Download]("kafka-pods/kafka-1-pod.json")

---------
##### Create kafka-1-pod.json
```bash
kubectl create -f kafka-1-pod.json
```
Kafka Manager
=============

A tool for managing [Apache Kafka](http://kafka.apache.org).

It supports the following :

 - Manage multiple clusters
 - Easy inspection of cluster state (topics, brokers, replica distribution, partition distribution)
 - Run preferred replica election
 - Generate partition assignments with option to select brokers to use
 - Run reassignment of partition (based on generated assignments)
 - Create a topic with optional topic configs (0.8.1.1 has different configs than 0.8.2+)
 - Delete topic (only supported on 0.8.2+ and remember set delete.topic.enable=true in broker config)
 - Topic list now indicates topics marked for deletion (only supported on 0.8.2+)
 - Batch generate partition assignments for multiple topics with option to select brokers to use
 - Batch run reassignment of partition for multiple topics
 - Add partitions to existing topic
 - Update config for existing topic

Cluster Management

![cluster](/img/cluster.png)

***

Topic View

![topic](/img/topic.png)

***

Broker View

![broker](/img/broker.png)

***

Requirements
------------

1. [Kafka 0.8.1.1 or 0.8.2.0](http://kafka.apache.org/downloads.html)
2. [sbt 0.13.x](http://www.scala-sbt.org/download.html)
3. Java 7+

Configuration
-------------

The minimum configuration is the zookeeper hosts which are to be used for kafka manager state.
This can be found in the application.conf file in conf directory.  The same file will be packaged
in the distribution zip file; you may modify settings after unzipping the file on the desired server.

    kafka-manager.zkhosts="my.zookeeper.host.com:2181"

You can specify multiple zookeeper hosts by comma delimiting them, like so:

    kafka-manager.zkhosts="my.zookeeper.host.com:2181,other.zookeeper.host.com:2181"

Alternatively, use the environment variable `ZK_HOSTS` if you don't want to hardcode any values.

    ZK_HOSTS="my.zookeeper.host.com:2181"

Deployment
----------

The command below will create a zip file which can be used to deploy the application.

    sbt clean dist

Please refer to play framework documentation on production deployment.

If java is not in your path, or you need to build against a specific java version,
please use the following (the example assumes oracle java8):

    $ PATH=/usr/local/oracle-java-8/bin:$PATH \
      JAVA_HOME=/usr/local/oracle-java-8 \
      /path/to/sbt -java-home /usr/local/oracle-java-8 dist clean

This ensures that the 'java' and 'javac' binaries in your path are first looked up in the
oracle java8 release. Next, for all downstream tools that only listen to JAVA_HOME, it points
them to the oracle java8 location. Lastly, it tells sbt to use the oracle java8 location as
well.

Starting the service
--------------------

After extracting the produced zipfile, and changing the working directory to it, you can
run the service like this:

    $ bin/kafka-manager

By default, it will choose port 9000. This is overridable, as is the location of the
configuration file. For example:

    $ bin/kafka-manager -Dconfig.file=/path/to/application.conf -Dhttp.port=8080

Again, if java is not in your path, or you need to run against a different version of java,
add the -java-home option as follows:

    $ bin/kafka-manager -java-home /usr/local/oracle-java-8

Packaging
---------

If you'd like to create a Debian or RPM package instead, you can run one of:

    sbt debian:packageBin

    sbt rpm:packageBin

Credits
-------

Logo/favicon used is from [Apache Kafka](http://kafka.apache.org).

Most of the utils code has been adapted to work with [Apache Curator](http://curator.apache.org) from [Apache Kafka](http://kafka.apache.org).


License
-------

Apache Licensed. See accompanying LICENSE file.
Use Zookeeper Cluster in Kubernetes Cluster
=========================

### Pull fabric8/kafka image from docker hub
##### Tag and Push fabric8/kafka to local docker registry
```bash
docker pull fabric8/kafka 
docker tag fabric8/kafka registry.docker.company.com:5000/company/kafka
docker push registry.docker.company.com:5000/company/kafka
```

### Deploy kafka cluster
#### Edit the kafka-cluster-list.yaml
```yaml
kind: "List"
apiVersion: "v1"
id: "kafka"
items: 
  - kind: "Pod"
    apiVersion: "v1"
    metadata: 
      name: "kafka-1"
      labels: 
        name: "kafka"
        server-id: "1"
    spec: 
      containers: 
        - name: "kafka"
          image: "registry.docker.company.com:5000/company/kafka"
          #env: 
          #  - name: "BROKERID"
          #    value: "1"
          ports: 
            - containerPort: 9092
          command: ['/bin/sh', '-c']
          args: ['sed -i -- ''s/broker.id=0/broker.id=1/g'' /home/kafka/kafka/config/server.properties && sed -i -- ''s/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/g'' /home/kafka/kafka/config/server.properties && /home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties ']
  - kind: "Pod"
    apiVersion: "v1"
    metadata: 
      name: "kafka-2"
      labels: 
        name: "kafka"
        server-id: "1"
    spec: 
      containers: 
        - name: "kafka"
          image: "registry.docker.company.com:5000/company/kafka"
          #env: 
          #  - name: "BROKERID"
          #    value: "1"
          ports: 
            - containerPort: 9092
          command: ['/bin/sh', '-c']
          args: ['sed -i -- ''s/broker.id=0/broker.id=2/g'' /home/kafka/kafka/config/server.properties && sed -i -- ''s/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/g'' /home/kafka/kafka/config/server.properties && /home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties ']
  - kind: "Pod"
    apiVersion: "v1"
    metadata: 
      name: "kafka-3"
      labels: 
        name: "kafka"
        server-id: "1"
    spec: 
      containers: 
        - name: "kafka"
          image: "registry.docker.company.com:5000/company/kafka"
          #env: 
          #  - name: "BROKERID"
          #    value: "1"
          ports: 
            - containerPort: 9092
          command: ['/bin/sh', '-c']
          args: ['sed -i -- ''s/broker.id=0/broker.id=3/g'' /home/kafka/kafka/config/server.properties && sed -i -- ''s/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/g'' /home/kafka/kafka/config/server.properties && /home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties ']
  - kind: "Pod"
    apiVersion: "v1"
    metadata: 
      name: "kafka-4"
      labels: 
        name: "kafka"
        server-id: "1"
    spec: 
      containers: 
        - name: "kafka"
          image: "registry.docker.company.com:5000/company/kafka"
          #env: 
          #  - name: "BROKERID"
          #    value: "1"
          ports: 
            - containerPort: 9092
          command: ['/bin/sh', '-c']
          args: ['sed -i -- ''s/broker.id=0/broker.id=4/g'' /home/kafka/kafka/config/server.properties && sed -i -- ''s/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/g'' /home/kafka/kafka/config/server.properties && /home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties ']
  - kind: "Pod"
    apiVersion: "v1"
    metadata: 
      name: "kafka-5"
      labels: 
        name: "kafka"
        server-id: "1"
    spec: 
      containers: 
        - name: "kafka"
          image: "registry.docker.company.com:5000/company/kafka"
          #env: 
          #  - name: "BROKERID"
          #    value: "1"
          ports: 
            - containerPort: 9092
          command: ['/bin/sh', '-c']
          args: ['sed -i -- ''s/broker.id=0/broker.id=5/g'' /home/kafka/kafka/config/server.properties && sed -i -- ''s/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/g'' /home/kafka/kafka/config/server.properties && /home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties ']
  - kind: "Pod"
    apiVersion: "v1"
    metadata: 
      name: "kafka-6"
      labels: 
        name: "kafka"
        server-id: "1"
    spec: 
      containers: 
        - name: "kafka"
          image: "registry.docker.company.com:5000/company/kafka"
          #env: 
          #  - name: "BROKERID"
          #    value: "1"
          ports: 
            - containerPort: 9092
          command: ['/bin/sh', '-c']
          args: ['sed -i -- ''s/broker.id=0/broker.id=6/g'' /home/kafka/kafka/config/server.properties && sed -i -- ''s/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper:2181/g'' /home/kafka/kafka/config/server.properties && /home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties ']
```

### Deploy kafka cluster in Kubernetes Cluster
##### Create Kubernetes List: Service and Pods

```bash
kubectl create -f kafka-cluster-list.yaml

kubectl get pods 
kafka-1             1/1       Running   0          43m
kafka-2             1/1       Running   0          43m
kafka-3             1/1       Running   0          43m
kafka-4             1/1       Running   0          43m
kafka-5             1/1       Running   0          43m
kafka-6             1/1       Running   0          43m
```

### Deploy kafka cluster endpoint in Kubernetes Cluster
##### Create Kubernetes Endpoints: kafka-endpoint.json
```yaml
{
    "kind": "Endpoints",
    "apiVersion": "v1",
    "metadata": {
        "name": "kafka"
    },
    "subsets": [
        {
            "addresses": [
                { "IP": "172.23.87.5" },
                { "IP": "172.23.86.8" },
                { "IP": "172.23.11.5" },
                { "IP": "172.23.20.5" },
                { "IP": "172.23.60.6" },
                { "IP": "172.23.98.6" }
            ],           
            "ports": [
                { "name": "9092", "port": 9092 }
            ]
        }
    ]
}

kubectl create -f kafka-endpoint.json

kubectl get ep
NAME                      ENDPOINTS
kafka                     172.23.11.5:9092,172.23.20.5:9092,172.23.60.6:9092 + 3 more...
```

### Deploye Zookeeper Service in Kubernetes Cluster
##### Create Kubernetes Service: kafka-service.json

```yaml
cat kafka-service.json
{
    "kind": "Service",
    "apiVersion": "v1",
    "metadata": {
        "name": "kafka",
        "labels": {
           "name": "kafka"
        }
    },
    "spec": {
        "ports": [
            {
	    	"name": "9092",
                "protocol": "TCP",
                "port": 9092,
                "targetPort": 9092
            }
        ]
    }
}

kubectl create -f kafka-service.json

kubectl get svc
kafka                     name=kafka                                <none>                                192.168.3.192   9092/TCP
```

-------------------------------------------------------------------------------------------

### Test kafka cluster
##### Use the outbrain/kafkacli 
##### More Info can be acquired at https://github.com/outbrain/kafkacli
##### Get pre-build-binariess: https://github.com/outbrain/kafkacli/releases
##### Also, you can Download it as:
-----------------------------------------------------------------------------------------------------------------------


### Yeah~ It's work~~~~~

### Thanks to @Outbrain @fabric8
