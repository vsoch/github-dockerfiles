# Please note: spm-agent-docker has moved 

You can find the latest version here: 
- **Github: [sematext/sematext-agent-docker](https://github.com/sematext/sematext-agent-docker)**
- **Docker Hub: [sematext/sematext-agent-docker](https://hub.docker.com/r/sematext/sematext-agent-docker/)**

----------------------
----------------------
# Original Readme
---------------------
----------------------

# SPM for Docker

This is the Docker Monitoring Agent and Log Shipper for [SPM Docker Monitoring](http://sematext.com/spm/integrations/docker-monitoring.html) (for Docker metrics and events) & [Logsene / Hosted ELK](http://sematext.com/logsene) (for centralized logging)

Gathered information:
- Operating System Metrics of the Host machine (CPU / Mem / Swap/ ...) 
- Docker Container **Metrics/Stats**
	- CPU Usage
	- Memory Usage
	- Network Stats
	- Disk I/O Stats
- **Docker Events**
    - Version Information on Startup:
        - server-info – created by spm-agent framework with node.js and OS version info on startup
        - docker-info – Docker Version, API Version, Kernel Version on startup
    - Docker Events:
        - Container Lifecycle Events like
            - create, exec_create, destroy, export
        - Container Runtime Events like
            - die, exec_start, kill, pause, restart, start, stop, unpause, ...
- Docker **Logs**
  - default fields
	- hostname / IP address
	- container id
	- container name
	- image name
	- message
  - Log format detection and log parsers: 
	- NGINX
	- APACHE httpd, Kafka, Solr, HBase, Zookeeper, Cassandra
	- MySQL
	- MongoDB
	- Redis
	- Elasticsearch
	- Nsq.io
	- JSON, ... 

![](https://sematext.files.wordpress.com/2015/06/spm-for-docker.png?w=630&h=455)


## Installation 
1. Get a free account at [sematext.com/spm](https://apps.sematext.com/users-web/register.do)  
2. [Create an SPM App](https://apps.sematext.com/spm-reports/registerApplication.do) of type "Docker" and copy the SPM Application Token 
   - For logs (optional) [create a Logsene App](https://apps.sematext.com/logsene-reports/registerApplication.do) to an App Token for [Logsene](http://www.sematext.com/logsene/)  
3. Run the image 
	```
	docker pull sematext/spm-agent-docker
	docker run -d --name spm-agent -e SPM_TOKEN=YOUR_SPM_TOKEN -e LOGSENE_TOKEN=YOUR_LOGSENE_TOKEN  -e HOSTNAME=$HOSTNAME  -v /var/run/docker.sock:/var/run/docker.sock sematext/spm-agent-docker
	```

	**Required Parameters:**
	- -e SPM_TOKEN - SPM Application Token
	- -e HOSTNAME - Name of the docker host e.g. '$HOSTNAME' for Amazon ECS see HOSTNAME_LOOKUP_URL 
	- -v /var/run/docker.sock - Path to the docker socket
	
	**Optional Parameters:**
	- --privileged  might be required for Security Enhanced Linux (the better way is to have the right policy ...)
	- -e HOSTNAME_LOOKUP_URL - On Amazon ECS, a [metadata query](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) must be used to get the instance hostname (e.g. "169.254.169.254/latest/meta-data/local-hostname")
	- -e HTTPS_PROXY - url for a proxy server
	
	**Docker Logs Parameters:**
	- -e LOGSENE_TOKEN - Logsene Application Token for logs
	- -e REMOVE_ANSI_ESCAPE_SEQ=enabled - removes e.g. ANSI Terminal color codes from logs for pattern matching 
	- Whitelist containers for logging 
	  - -e MATCH_BY_NAME - A regular expression to white list container names 
	  - -e MATCH_BY_IMAGE - A regular expression to white list image names 
	- Blacklist containers 
	  - -e SKIP_BY_NAME - A regular expression to black list container names 
	  - -e SKIP_BY_IMAGE - A regular expression to black list image names for logging 
	  - -v /yourpatterns/patterns.yml:/etc/logagent/patterns.yml - to provide custom patterns for log parsing, see [logagent-js](https://github.com/sematext/logagent-js)


	You’ll see your Docker metrics in SPM after about a minute.
	
5. Watch metrics, use anomaly detection for alerts, create e-mail reports and [much more ...](http://blog.sematext.com/2015/06/09/docker-monitoring-support/)

![](https://sematext.files.wordpress.com/2015/06/docker-overview-2.png)

![](https://sematext.files.wordpress.com/2015/06/docker-network-metrics.png)

Docker Events:
![](https://sematext.files.wordpress.com/2015/06/bildschirmfoto-2015-06-24-um-13-56-39.png)

## Integrated Log Parser

SPM for Docker recognizes log formats - so your logs arrive in a structured format in Logsene!
The format recognition, data extractions, date parsing etc. is provided by [logagent-js](https://github.com/sematext/logagent-js) and covers:
- Format detection e.g. for
    	- Mongo DB
	- Nginx
	- Apache httpd, Kafka, Cassandra, HBase, Solr, Zookeeper
	- MySQL
	- Redis  
- plain text log messages
- line delimited JSON logs

To use a custom pattern definition simply mount a volume to '/etc/logagent/patterns.yml':
```
-v /mydir/patterns.yml:/etc/logagent/patterns.yml
```

Feel free to contribute to [logagent-js](https://github.com/sematext/logagent-js) to enrich the default pattern set. 

# Installation on CoreOS Linux

SPM for Docker can monitor CoreOS clusters including metrics and logs from Docker and journald.   
See: [Setup SPM on CoreOS](https://github.com/sematext/spm-agent-docker/tree/master/coreos)

![](https://sematext.files.wordpress.com/2015/06/spm-logsene-coreos.png)

# Support

1. Please check the [SPM for Docker Wiki](https://sematext.atlassian.net/wiki/display/PUBSPM/SPM+for+Docker)
2. If you have questions about SPM for Docker, chat with us in the [SPM user interface](https://apps.sematext.com/users-web/login.do) or drop an e-mail to support@sematext.com
3. Open an issue [here](https://github.com/sematext/spm-agent-docker/issues) 
4. Contribution guide [here](https://github.com/sematext/spm-agent-docker/blob/master/contribute.md)


