# Graphite

Docker container that can run Graphite components. It also provides
a means to run BigGraphite's version of carbon-cache that can write
to Cassandra via Graphite's plugin system

# Running locally

The following command will run:
- A 3-node Cassandra cluster
- bg-carbon-cache to collect metrics and push it to Cassandra
- Graphite webapp which can accessessed via `http://localhost:8080`

```bash
docker-compose up -d
```

Once the containers are up and running, you send some random data to
a metric using the plaintext protocol
```bash
for i in `seq 1 100`; do
    echo "local.random.diceroll $((RANDOM)) `date +%s`" \
        | nc -c localhost 2003;
    sleep 5;
done
```

__NOTE:__ It seems to take some time for data in Cassandra to become
available.

You can query from each Cassandra node via the webapp or carbon-cache-a
container. But first check whether schema has been replicated across
nodes:
```bash
docker exec -it webapp cqlsh --cqlversion=3.4.4 cassandra-1 \
    -e "use biggraphite; describe tables;"
docker exec -it webapp cqlsh --cqlversion=3.4.4 cassandra-2 \
    -e "use biggraphite; describe tables;"
docker exec -it webapp cqlsh --cqlversion=3.4.4 cassandra-3 \
    -e "use biggraphite; describe tables;"
```
You might see `<empty>` until all nodes have the replicated.

Once replication is working, you should see the same data across all
nodes:
```bash
docker exec -it webapp cqlsh --cqlversion=3.4.4 cassandra-1 \
    -e "select * from biggraphite.datapoints_1440p_60s_0;"
docker exec -it webapp cqlsh --cqlversion=3.4.4 cassandra-2 \
    -e "select * from biggraphite.datapoints_1440p_60s_0;"
docker exec -it webapp cqlsh --cqlversion=3.4.4 cassandra-3 \
    -e "select * from biggraphite.datapoints_1440p_60s_0;"
```

You should be able to see the data in the Graphite webapp via
`http://localhost:8080`.

# Running in AWS

## Prerequisites

Checkout [cassandra-aws](https://github.com/LoyaltyOne/cassandra-aws).
Your source folder should look something like this. Change the relative
paths below if they are different:

```
path-to-source
       |
       +---------- graphite
       |
       +---------- graphite-config
       |
       +---------- cassandra-aws
```

You should have an S3 bucket configured to store Casssandra configuration
files.

```bash
pushd ../graphite-config
mkdir -p cassandra
cd cassandra
../../truststore-setup cassandra dev-cassandra-graphite
aws s3 sync cassandra-config s3://<s3-bucket-name>/dev-cassandra-graphite
popd
```

You will need the `cluster-ca-certificate.pem` file to test with cqlsh.

## Deploy EFS

Create a configuration file `../graphite-config/dev-efs-params.json`:
```json
{
  "Parameters": {
    "VpcId": "changeme",
    "SubnetIdA": "changeme",
    "SubnetIdB": "changeme",
    "SubnetIdC": "changeme"
  }
}
```

```bash
./deploy-efs efs-graphite ../graphite-config/dev-efs-params.json
```

## Deploy Cassandra

Create a configuration file `../graphite-config/dev-cassandra-params.json`.
Note that the hosted zone name has a `.` at the end.
```json
{
  "Parameters": {
    "EcsInstanceType": "m4.large",
    "KeyName": "changeme",
    "EfsStackName": "dev-efs-graphite",
    "EfsMountPath": "/mnt/efs",
    "HostedZoneName": "changeme."
    "HostedZoneId": "changeme",
    "CassandraConfigS3Bucket": "changeme",
    "LogRetention": 3,
    "CloudFormationLogGroup": "dev-graphite"
  }
}
```

```bash
./deploy-cassandra cassandra-graphite ../graphite-config/dev-cassandra-params.json
```

To test cluster status, SSH into one of the ECS instances, then use
`docker ps` to locate the cassandra container ID and then use
`nodetool status` on it.
```bash
$ docker ps
CONTAINER ID        IMAGE                            COMMAND                  CREATED             STATUS              PORTS               NAMES
06f05195d663        amazon/amazon-ecs-agent:latest   "/agent"                 3 seconds ago       Up 2 seconds                            ecs-agent
59c97938cf1e        cassandra:3.11                   "docker-entrypoint..."   37 seconds ago      Up 36 seconds                           cassandra

$ docker exec -it 59c97938cf1e nodetool status
Datacenter: us-east
===================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load       Tokens       Owns (effective)  Host ID                               Rack
UN  10.0.5.229  235.53 KiB  256          66.9%             1843ddc7-8192-4dc9-87f6-7fc5313beb62  1d
UN  10.0.3.232  69.85 KiB  256          66.0%             cad549a1-a94a-4b76-87be-839b9920da0a  1c
UN  10.0.1.222  108.63 KiB  256          67.0%             1aa2d578-c4a3-449f-8f7f-edf65a008b42  1b
```

You can also use CQLSH. First copy the `cluster-ca-certificate.pem` to
`/home/ec2-user/cassandra.pem` and change the hostname suffix below
for `nodea`.

```
sudo yum install -y java-1.8.0

curl -O http://apache.forsale.plus/cassandra/3.11.2/apache-cassandra-3.11.2-bin.tar.gz
tar xvzf apache-cassandra-3.11.2-bin.tar.gz

mkdir -p  /home/ec2-user/.cassandra

# Change the hostname suffix
cat << EOF | tee /home/ec2-user/.cassandra/cqlshrc
[authentication]
username = cassandra
password = cassandra

[cql]
version = 3.4.4

[connection]
hostname = nodea.cassandra.changeme
port = 9042

[tracing]
max_trace_wait = 10.0

[ssl]
certfile = /home/ec2-user/cassandra.pem
validate = true
factory = cqlshlib.ssl.ssl_transport_factory
EOF
```

```bash
./apache-cassandra-3.11.2/bin/cqlsh --ssl
```

## Deploy Graphite

Use the steps above for `cqlsh` and connect to the Cassandra cluster.
You can configure the schema manually by running the commands in
`biggraphite/schema.cql`.

Create a configuration file `../graphite-config/dev-master-params.json`:
```json

```

```bash

```
