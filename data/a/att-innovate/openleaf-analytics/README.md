## Openleaf-Analytics
Lightweight and easy to install on-board analytics stack for white-box switches running [ONL](http://www.opennetlinux.org) and SnapRoute [FlexSwitch](https://snaproute.com).

We run this stack on [Wedge100-32X](http://www.edge-core.com/productsInfo.php?cls=1&cls2=5&cls3=67&id=128) and [Wedge100BF-65X](https://barefootnetworks.com/blog/disaggregation-and-programmable-forwarding-planes/) switches from Edge-Core.

![diagram](https://github.com/att-innovate/openleaf-analytics/blob/master/docs/openleaf-analytics-demo.png)

All telemetry data gets collected and stored locally on the switch itself. An on-board dashboard and a query tool provide easy access to the stored telemetry. Plus an additional rule-engine provides a simple way to process the data for aggregation purposes or simple anomaly detection. 

The individual open-source components are:
- [InfluxDB](https://www.influxdata.com/time-series-platform/influxdb/): The Time Series Database
- [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/): Agent for Collecting and Reporting Metrics Data
- [Kapacitor](https://docs.influxdata.com/kapacitor/v1.3/introduction/getting_started/): A Rule-based Data Processing Engine
- [Grafana](https://grafana.com/grafana): Dashboard for Visualizing Metrics Data

All those services run as individual [Docker](https://www.docker.com) containers managed by [Docker Compose](https://docs.docker.com/compose/overview/).

Additionally this project comes with:
- [scripts](./scripts): Scripts to build, run, and configure Openleaf-Analytics
- [telegraf-snaproute](./telegraf-snaproute): Code for the SnapRoute plugin for Telegraf
- [grafana](./grafana): Pre-configured Dashboards for Health, Docker, and Network Metrics
- [docker](./docker): All the Docker and Configuration Files for the different services

### Installation Guide
The few required steps to install the Openleaf Analytics Stack can be found in the [Installation Guide](./docs/install.md).

### User Guide
Information about the different dashboards and tools can be found in the [User Guide](./docs/userguide.md).

### Example Dashboard
#### Default Network Dashboard
![dashboard](https://github.com/att-innovate/openleaf-analytics/blob/master/docs/grafana-network.png)

### Additional Scenarios
Out of the box the scripts will install a demo setup as outlined above. The Kapacitor will only be used to calculate a “Health Index”. Obviously this setup can be used as a foundation for more advanced scenarios.

#### Controller Scenario
The rule language of Kapacitor can be used to describe anomalies and actions to be taken. An action can for example be sending an alert, like an snmp event, to some global collector, or making a REST call to the local Flexswitch instance to reconfigure the forwarding plane of the switch itself.

Examples can be found in the [Kapacitor](https://docs.influxdata.com/kapacitor/v1.3/introduction/getting_started/) documentation.

![diagram](https://github.com/att-innovate/openleaf-analytics/blob/master/docs/openleaf-analytics-controller.png)

#### Control and Forward Scenario
It is also pretty simple to implement an Aggregator Agent whose job it is to aggregate and forward Metrics Data to some centralized Telemetry Platform at a certain time interval.

![diagram](https://github.com/att-innovate/openleaf-analytics/blob/master/docs/openleaf-analytics-forwarder.png)
