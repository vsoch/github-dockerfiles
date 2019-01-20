Charmander-Experiment: Maxusage
--------------------------------

Our MaxUsage-Experiment will analyze the actual memory usage of a running simulators and use that result to overwrite
the memory-allocation for subsequent run-requests for the same simulators.

#### Prerequisite
A local Charmander cluster has to be up and running.
Related documentation available at [https://github.com/att-innovate/charmander](https://github.com/att-innovate/charmander).

Verify that you are in your local Charmander directory and reset the Charmander cluster.

    ./bin/reset_cluster

Verify that no task is running using the Mesos console at [http://172.31.1.11:5050](http://172.31.1.11:5050)

#### Build and deploy the simulators and the analyzer
The maxusage analyzer is implemented in Scala using Spark-Streamning and Spark-SQL.
The code is part of this project and can be found at [MaxUsage.scala](https://github.com/att-innovate/charmander-experiment-maxusage/blob/master/analytics/maxusage/src/main/scala/MaxUsage.scala).

One could argue that using Spark to resolve the max memory usage of a simulator is an over-kill .. but hey, we had
to try out streaming and Spark-SQL .. and we are certain that we can scale it up if needed.

Lets build it first. Change to the experiments folder and check out the code into a folder called `maxusage`

    cd experiments
    git clone https://github.com/att-innovate/charmander-experiment-maxusage.git maxusage

Change your working directory back to the root of Charmander and start the build process

    cd ..
    ./experiments/maxusage/bin/build

This command builds maxusage, and creates and deploys Docker images for itself and the different load simulators.
This process will take some time the first time you run it.


#### Start cAdvisor and Analytics-Stack

    ./bin/start_cadvisor
    ./bin/start_analytics

#### Start the different simulators

    ./experiments/maxusage/bin/start_lookbusy200mb
    ./experiments/maxusage/bin/start_lookbusy80mb
    ./experiments/maxusage/bin/start_stress60mb

#### Start maxusage

    ./experiments/maxusage/bin/start_maxusage

#### Verify the experiment setup in Redis

Redis-UI can be found at: [http://172.31.2.11:31610](http://172.31.2.11:31610)

The information in Redis gets updated by the scheduler every 15s. Give it some time to get synchronized. Refresh the page
until "task-intelligence" shows up. You should then see something like:

![image](https://github.com/att-innovate/charmander-experiment-maxusage/blob/master/docs/redis.png?raw=true)

Redis shows all the 3 slaves/nodes, all the currently running tasks, all the "metered" tasks, and the "intelligence" collected
by maxusage in the task-intelligence section. The _mem_ value represents the highest memory-use of a metered task, for lookbusy it should
be something roughly _210MB_ (_209928192_).

#### Verify idle memory

Open the Mesos console at [http://172.31.1.11:5050](http://172.31.1.11:5050) and look for the _Resources_ _idle_ number at the bottom left.
It should be something like _682MB_.

#### Redeploy simulators

    ./bin/reshuffle

This command will kill and restart our running simulators. The Mesos console can be used to see the progress of the _reshuffling_.

#### Verify idle memory

The memory allocation for the simulators gets adjusted based on our "task intelligence" (maxusage + 10% safety).
That decrease in allocated memory should increase the amount of idle memory for the cluster.

Open Mesos console at [http://172.31.1.11:5050](http://172.31.1.11:5050) and look for the _Resources_ _idle_ number at the bottom left.
It should now be roughly _790MB_.

#### Timeseries in InfluxDB

In case you are curious about the raw timeseries stored in InfluxDB. InfluxDB is available at [http://172.31.2.11:31400](http://172.31.2.11:31400)

To Login: Username/password: both _root_ , hostname: _172.31.2.11_ and port _31410_

After log in click on "Explore Data" for charmander and execute following queries:

    select memory_usage from machine where hostname='slave1' limit 200

This returns and shows a histogram based on 200 data points

To get the memory usage for the stress60mb simulator try

    select memory_usage from stats where container_name =~ /stress*/ limit 500

This returns 500 datapoints for the stress simulator.


#### That's it, let's clean up

    ./bin/reset_cluster

..and head back to the Charmander [Homepage](https://github.com/att-innovate/charmander/)
