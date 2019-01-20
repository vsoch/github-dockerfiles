## TAEP-Analytics
This project contains all the TAEP Analytics Stack related code, scripts, and configurations.

The Analytics Stack is based on the open-source version of [InfluxData](https://www.influxdata.com/time-series-platform/) stack and the [Grafana](https://grafana.com) dashboard.

All the components of the stack run in individual [Docker](https://www.docker.com) containers controlled by [Docker-Dompose](https://docs.docker.com/compose/overview/).

All the components run on the switch itself. TAEP is a self-contained environment. No outside service or functionality is needed to run experiments on TAEP.

The project is structured as follow:
- *`docker/`* : Contains all the files needed by Docker to build all the different components.
- *`grafana/`* : Contains definitions for the different default dashboards used by TAEP.
- *`scripts/`* : Contains scripts to build and configure our stack.
- *`telegraf-barefoot/`* : Source code for the [Telegraf](https://github.com/influxdata/telegraf) plugin needed to retrieve network metrics from our TAEP-Controller.

For any additional information regarding TAEP please refer to [github.com/att-innovate/taep](https://github.com/att-innovate/taep).

### Installation
For installation please refer to [TAEP-Scripts](https://github.com/att-innovate/taep-scripts).

### Components
#### Agent
The Agent is the place, the service in which one would implement any AI/ML logic related to an experiment.

The [Kapacitor](https://github.com/influxdata/kapacitor) will forward metrics to the Agent based on a [configurable rule](https://github.com/att-innovate/taep-analytics/blob/master/docker/kapacitor/tasks/agent.tick).

The Agent then can use those metrics to change/modify divert rules via the available [TAEP-Controller API’s](https://github.com/att-innovate/taep-controller#rest-api).

The sample [Agent code](https://github.com/att-innovate/taep-analytics/blob/master/docker/agent/src/agent.py) that comes with this project can be used as a starting point, as a template to implement individual AI/ML logic. By default it just outputs the metrics it receives from the Kapacitor.

The `./scripts/build-it.sh` (see below) script can be used to rebuild the Agent container after any code change.

#### Grafana
[Grafana](https://grafana.com) is used to visualize System, Docker, and Network metrics stored locally in InfluxDB.

Our installation comes installed with four default dashboards (Docker, Network, Network-TAEP (template), and System Health).

Specific Grafana configurations can be changed in the [`grafana.ini`](https://github.com/att-innovate/taep-analytics/blob/master/docker/grafana/grafana.ini). Any change requires a rebuild of the container, see scripts below.

#### InfluxDB
[InfluxDB](https://github.com/influxdata/influxdb) is our timeseries database. Its small footprint and its excellent data compaction algorithm makes it a perfect choice for running it on the switch itself.

InfluxDB configurations can be changed in [`influxdb.conf`](https://github.com/att-innovate/taep-analytics/blob/master/docker/influxdb/influxdb.conf). Any changes require a rebuild of the container, see scripts below.

#### Kapacitor
[Kapacitor](https://github.com/influxdata/kapacitor) is a framework for rule-based processing and monitoring of timeseries data.

Our installation comes with two predefined rules written in [TICKscript](https://docs.influxdata.com/kapacitor/v1.3/tick/).

- The “Health” task, enabled by default, is a simple sample script that runs every 5 minutes and calculates a “Health-Index” based on timeseries data. The calculated index is written back into InfluxDB.
- The “Agent” task, disabled by default, queries the timeseries database every 10s and forwards the retrieved metrics to the Agent service, see above.

#### Telegraf
[Telegraf](https://github.com/influxdata/telegraf) is a service for collecting and reporting metrics from a wide variety of sources. It is easily extensible through a plugin architecture. 

The project comes with our own [plugin](https://github.com/att-innovate/taep-analytics/tree/master/telegraf-barefoot/barefoot) that enables Telegraf to collect metrics from the TAEP-Controller.

### Docker-Compose
We use Docker-Compose as a simple orchestration mechanism. Details about all the services can be found in [`docker-compose.yml`](https://github.com/att-innovate/taep-analytics/blob/master/docker/docker-compose.yml).

### Available Scripts
All the scripts have to be run on the switch from the root directory of this project.

- `./scripts/build-it.sh` : Used to build all the Docker containers. Gets called as part of the global `deploy-taep.sh` script.
- `./scripts/clean-it.sh` : Can be used to clean the state and log files of the containers controlled by Docker-Compose.
- `./scripts/configure-grafana.sh` : Used to install our default Grafana dashboards. Gets called as part of the global `configure-analytics.sh` script.
- `./scripts/configure-kapacitor-agent.sh` : Script to add the `Agent` task to the Kapacitor. Gets called as part of the global `configure-analytics.sh` script.
- `./scripts/configure-kapacitor-health.sh` : Script to add the `Health` task in the Kapacitor. Gets called as part of the global `configure-analytics.sh` script.
- `./scripts/disable-kapacitor-agent.sh` : Script to stop Kapacitor from sending metrics to the Agent.
- `./scripts/enable-kapacitor-agent.sh` : Script to tell Kapacitor to start sending metrics to the Agent.
- `./scripts/log-agent.sh` : Retrieve log-output for the Agent.
- `./scripts/log-it.sh` : Retrieve log-output for the components of our stack.
- `./scripts/run-client-influxdb.sh` : Start the command-line interface to InfluxDB.
- `./scripts/run-it.sh` : Tell Docker-Compose to start the whole stack. Gets called by global `run-analytics.sh` script.
- `./scripts/stop-it.sh` : Tell Docker-Compose to stop the whole stack. Gets called by global `stop-analytics.sh` script.

