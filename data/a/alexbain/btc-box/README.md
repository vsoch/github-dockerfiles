btc-box
=======

This repository will spin up a collection of Docker containers that work together to form a bitcoin development environment. Tested using DigitalOcean VPS.

Currently, this repostiroy creates the following containers:

* [bitcoind](https://bitcoin.org/en/) - full bitcoin-qt core, exposes json-rpc port
* [logstash](http://logstash.net/) - aggregates logs from all containers and host
* [elasticsearch](http://www.elasticsearch.org/) - ingests all logs, provides way to search and analyze
* [kibana](http://www.elasticsearch.org/overview/kibana/) - AngularJS UI on top of elasticsearch, available at port 80 to monitor box
* [insight](http://insight.is/) - RESTful API on top of bitcoind w/ UI to explore blockchain, available at port 3000

### Installation

On a fresh Ubuntu 14.04 x64 box (minimum 40GB HDD and 2GB RAM), run the following commands as root:

```
apt-get install -y git
git clone https://github.com/alexbain/btc-box/
cd btc-box
./provision.sh
```

When this is complete, open a web browser to your server's IP and you'll be able to see realtime analytics of the box and the bitcoin network displayed via Kibana. You an also explore the blockchain using an indexed database on port 3000. Insight exposes a RESTful API you may want to use for any bitcoin/blockchain applications you want to create. If you want to load a sensible dashboard for Kibana - I have used [btc-box-dashboard](https://gist.github.com/alexbain/18f83ac40a1369224173) before.

More to come.

### Ideas for improvement

* Load up a sensible default dashboard into Kibana upon installation [btc-box-dashboard](https://gist.github.com/alexbain/18f83ac40a1369224173)
* Centralize configuration, allow for ability to use testnet or livenet programatically
* Reverse proxy elasticsearch behind nginx, close port 9200 to outside
* Reverse proxy insight behind nginx, close port 3000 to outside
* Run an nginx container and find way to provide configuration files for each container needing a reverse proxy
* Support Vagrant for local development (use testnet by default)
* CoreOS + etcd + fleet looks like an interesting combination long term - would allow btc-box to scale to multiple instances
* Running ``apt-get update`` on each container slows down build process, consider removing it
* Find a way to automatically restart container when it fails
* Find a way to automatically route logs from containers to logstash
* Ensure that /var/log/* is being logged to logstash
* Elasticsearch endpoints used for writing data should require HTTP basic auth, at a minimum

### Disclaimer

Do not use btc-box to store bitcoins. It is not intended to be used as a wallet. This project is designed to provide a strong foundation you can use to build bitcoin based applications.
