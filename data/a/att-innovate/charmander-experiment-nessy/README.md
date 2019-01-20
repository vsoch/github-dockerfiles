Charmander-Experiment: Nessy
----------------------------

Nessy is an experiment that runs on the Charmander Lab Platform that performs the dynamic orchestration of DNS servers and detection of DDoS Attack. 


![image](https://github.com/att-innovate/charmander-experiment-nessy/blob/master/docs/Nessy.jpg?raw=true)


#### Main features of Nessy:
 - Allow for a dynamic orchestration of containerized DNS servers (configured with Bind9 services) 
    
 - Generating the necessary training data sets by implementing load generators for both normal user load & DDoS traffic patterns
    
 - Processing the streamed data and applying a simple algorithm for auto-scaling and DDoS detection.
    
#### Step by step Instructions:

1. [Set Up Nessy in Charmander Environment][1]

    - Configure and build the five nodes with Vagrant and VirtualBox
    - Reload and reset environment

2. [Build analyzers, vector and Nessy] [2] 
    
    - Build and configure the containers for nessy experiemnt
    - Build analytics, datacollectors and vector

3. [Lets try it out] [3]
    
    - You can understand the system behavior better by manually starting tasks and seeing the change
    - You can use it to confirm whether the smartscaling or your own analytics is working appropriately

4. [Or let us run a script] [4]

    - The scripts are designed for collecting data easily for Machine Learning model training.
    - The scripts include setting up analytics an vectors for you, but it does NOT start smartscaling.
    - You will be able to collect all data generated from the experiment and run your own data analysis.

5. [You can build your own Nessy analytics] [5]

    - We have built the data query and streaming that can be esaily utilized
    - You can plugin your own code for auto-scaling and DDoS attack


To clean up the experiment, just run inside charmander folder

    ./bin/reset_cluster




[1]: https://github.com/att-innovate/charmander-experiment-nessy/blob/master/docs/SETUPNESSYNODES.md
[2]: https://github.com/att-innovate/charmander-experiment-nessy/blob/master/docs/BUILDNESSY.md
[3]: https://github.com/att-innovate/charmander-experiment-nessy/blob/master/docs/RUNMANUALLY.md
[4]: https://github.com/att-innovate/charmander-experiment-nessy/blob/master/docs/RUNSCRIPT.md
[5]: https://github.com/att-innovate/charmander-experiment-nessy/blob/master/analytics/
