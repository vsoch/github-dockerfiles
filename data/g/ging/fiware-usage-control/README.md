# Fiware Usage Control

Usage control is a promising approach for access control in open, distributed, heterogeneous and network-connected computer environments. It encompasses and enhances traditional access control models, Trust Management (TM) and Digital Rights Management (DRM), and its main novelties are mutability of attributes and continuity of access decision evaluation.

Usage control encompass Data Access control and data Usage Control, a good representation of this concepts are showed in the next figure:

![usage-control-concept](images/usage-concept.png)

Data Access Control:
 * Specify who can access what resource
 * Also the rights to access it (actions)

Data Usage Control:
 * Ensures data sovereignty
 * Regulates what is allowed to happen with the data  (future use).
 * Related with data ingestion and processing
 * Context of intellectual property protection, privacy protection, compliance with regulations and digital rights management

In order to include the capabilities of usage control, in this repo are include a set of components and operations for providing usage control capabilities over Data coming from the Orion Context Broker and processed by a data streaming processing engine (Apache Flink). First, the architecture and scenario are presented, and then the instructions and resources of how you can replicate the case of use presented.
## Architecture

The next figure presents an abstract representation of the architecture of usage control proposed.
Fist this architecture is divided into two parts: the first one is represented by the Data User side which made the data request and process it
using the streaming processing engine. The second part is the Data provided side which includes the different components to 
ensure the complaint of the obligations defined and acts as a Digital Rights Management.
![usage-architecture](images/usage-architecture.png)
 
## Scenario
The scenario is composed by:
User Side:
 * Apache Flink Cluster (1 Job manager and 1 task manager)
 * A streaming Job for making the avg of some values of and Entity created in the Orion context Broker
Data Provider
 * One IDM keyrock instance for Access control and define the Usage control Policies
 * One Orion (with mongo) instance where the entities are created.
 * One PEP proxy instance for access control
 * One instance of fluentd which acts as log collector of all the events and execution task of the Apache flink cluster (Data User Side)
 * One instance of a PUB/SUB engine (Kafka) for sending and receiving values from/to the Obligation compliant engine (Apache flink cluster- Data Provider Side)
 * One Apache flink cluster with complex event processing capabilities for analyzing the logs ensure the compliant of the obligations defined in the IDM 
 
![usage-scenario](images/usage-scenario.png) 

### Case of use

Th

## Deployment

For deploying and running this scenario you need to be pre-installed and running docker and docker compose
1. Clone the repository
```
git clone https://github.com/ging/fiware-usage-control.git
```
2. Go to the root directory
```
cd fiware-usage-control
```
3. Run containers
```
sudo docker-compose up -d
```
4. Check if all the containers are running
```
sudo docker ps
```
Once you have all up and running, you need to create the entities in the orion context broker
5. Give execution permission and execute the create entities script
```
chmod 775 -R orion
./orion/create-entities.sh
```
6. Check the orion entities
```
curl localhost:1026/v2/entities -s -S --header 'Accept: application/json' | python -mjson.tool
```

