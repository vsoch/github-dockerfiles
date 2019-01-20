## Description:

Meant to standup a Hadoop 2.7.3 HDFS HA on multiple machines inside Docker containers.  On the "active" namenode, the 1st time it starts up, it will format the namenode as well as format the ZK for failover.  The "standby" namenode will bootStrapStandby.  

#### Runtime options:

* __active__:  Start the 1st namenode with a zkfc service.
* __standby__:  Start the 2nd namenode and bootstrap from an already formatted/running namenode. This will also start a zkfc service.
* __zkfc__:  Start the zkfc in as a separate service
* __journalnode__:  Start a journalnode
* __datanode__:  Starts a datanode
* __bash__:  allows you to jump in and check things out


#### Environment Variables

__CLUSTER_NAME__:  the HDFS URI default filesystem name

__NNODE1_IP__: Namenode #1 IP/hostname

__NNODE2_IP__:  Namenode #2 IP/hostname

__JNODES__: semicolon separated list of journal node IPS, e.g jn01:8485;jn02:8485;jn03:8485

__ZK_NODES__:  comma separated list of zookeeper IPS, e.g. zk01:2181,zk02:2181,zk03:2181

#### Volumes:

/data/hdfs/nn:  inside the container, where the fsimage/namenode metadata exists

/data/hdfs/journal:  inside the container, where the journal node keeps the edits

/data/jdfs/dn: inside the container, where the datanode keeps the blocks

#### Command Line examples


* docker run --name nn01 --net=host --env-file hdfs-envs --env NNODE_ID=nn1 hdfs active
