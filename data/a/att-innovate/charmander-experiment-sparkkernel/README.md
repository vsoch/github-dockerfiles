Charmander-Experiment: Spark-Kernel
-----------------------------------

IBM open-sourced their [Spark-Kernel](https://github.com/ibm-et/spark-kernel) project.
It allows anyone to run the Spark-Shell as a _Notebook_ in jupyter (previously known as iPython).

This project includes scripts to build and run a Spark-Kernel docker image plus a load simulator to run an experiment
similar to [maxusage](https://github.com/att-innovate/charmander-experiment-maxusage).

#### Prerequisite
A local Charmander cluster has to be up and running.
Related documentation available at [https://github.com/att-innovate/charmander](https://github.com/att-innovate/charmander).

Verify that you are in your local Charmander directory and reset the Charmander cluster.

    ./bin/reset_cluster

Verify that no task is running using the Mesos console at [http://172.31.1.11:5050](http://172.31.1.11:5050)

#### Build and deploy the "sparkkernel" and the load simulator

Change to the experiments folder and check out the code into a folder called `sparkkernel`

    cd experiments
    git clone https://github.com/att-innovate/charmander-experiment-sparkkernel.git sparkkernel

Change your working directory back to the root of Charmander and start the build process

    cd ..
    ./experiments/sparkkernel/bin/build

Run Spark-Kernel with Charmander

    ./bin/start_cadvisor
    ./bin/start_analytics
    ./experiments/sparkkernel/bin/start_stress60mb
    ./experiments/sparkkernel/bin/start_sparkkernel

Wait a few seconds and open Spark-Kernel/jupyter at [172.31.2.11:31800/](http://172.31.2.11:31800/)

Open the _CharmanderUtils.ipynb_ notebook and wait until the Spark Kernel is ready, indicated in the header by the dot
changing in to a circle, that takes roughly 10s, and you should see something like this:

![image](https://github.com/att-innovate/charmander-experiment-sparkkernel/blob/master/docs/SparkKernel.png?raw=true)

You can now execute all the _cells_ using menu _Cell/Run All_ .. Have fun!


#### That's it, let's clean up

    ./bin/reset_cluster

..and head back to the Charmander [Homepage](https://github.com/att-innovate/charmander/)
