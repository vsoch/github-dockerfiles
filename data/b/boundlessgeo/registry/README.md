Registry
========

[![Build Status](https://travis-ci.org/boundlessgeo/registry.svg?branch=master)](https://travis-ci.org/boundlessgeo/registry)
[![Coverage Status](https://coveralls.io/repos/github/boundlessgeo/registry/badge.svg?branch=master)](https://coveralls.io/github/boundlessgeo/registry?branch=master)


[![Build Status](http://ci.boundlessps.com/buildStatus/icon?job=commit-build-registry-centos6)](http://ci.boundlessps.com/job/commit-build-registry-centos6) (Enterprise Linux 6 RPM)

[![Build Status](http://ci.boundlessps.com/buildStatus/icon?job=commit-build-registry-centos7)](http://ci.boundlessps.com/job/commit-build-registry-centos7) (Enterprise Linux 7 RPM)

Registry is a web-based platform that captures geo-spatial content using CSW-T
protocol. Information is indexed into the Elasticsearch engine allowing fast
searches.

<p align="center"><img src="https://cloud.githubusercontent.com/assets/3285923/20119468/a58abe98-a5d6-11e6-89ad-b29903150324.png" width=80%> </p>

Installation
============

Assuming ubuntu 14.04 OS.

1. Install and configure elasticsearch

	```sh
	wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
	echo "deb https://packages.elastic.co/elasticsearch/2.x/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-2.x.list
	sudo apt-get update && sudo apt-get install elasticsearch
	sudo sed -i -e 's/#ES_HEAP_SIZE=2g/ES_HEAP_SIZE=1g/' /etc/default/elasticsearch
	sudo service elasticsearch start
	```

2. Get registry source code

	```sh
	wget https://github.com/boundlessgeo/registry/archive/master.zip
	unzip master.zip
	cd registry-master/
	```

	Alternative using git

	```sh
	git clone https://github.com/boundlessgeo/registry.git
	cd registry
	```

3. Installation of registry modules

	```sh
	pip install -r requirements.txt
	pip install -e .
	```

4. Configure pycsw database

	```sh
	python registry.py pycsw -c setup_db
	```

5. Database optimization (works only with PostgreSQL and MySQL)

	```sh
	python registry.py pycsw -c optimize_db
	```

Usage
=====

0. Run the test suite to verify everything is okay and install some dependencies like pytest for generating fake data.
       ```sh
       python setup.py test
       ```

1. Run the server. The server will listen in port 8000
	```sh
	python registry.py runserver
	```

2. List catalogs
	```sh
	curl http://localhost:8000/catalog
	```

3. Create catalog using registry API
	```sh
	curl -XPUT http://localhost:8000/catalog/<catalog_slug>/csw
	```

4. Add records into the database and search engine
	- Using CSW transactions.
	```sh
	curl -XPOST -d @payload.xml  http://localhost:8000/catalog/<catalog_slug>/csw
	```

	**Note.** You cannot records to Registry if catalog has not been created before.

	- From command line.
	```sh
	python registry.py pycsw -c load_records -p /records/files/path/ -s <catalog_slug>
	```

5. Search api endpoint.

	- For all records.

		```sh
		curl http://localhost:8000/api/
		```

	- For a single catalog.

		```sh
		curl http://localhost:8000/catalog/<catalog_slug>/api/
		```

6. Get record from csw.

	```sh
	curl -XGET http://localhost:8000/layer/<layer_uuid>.xml
	```

7. Get mapproxy yaml configuration file.

	```sh
	curl -XGET http://localhost:8000/layer/<layer_uuid>.yml
	```

8. Get mapproxy png.

	```sh
	curl -XGET http://localhost:8000/layer/<layer_uuid>.png
	```

9. Re-index layers from pycsw database.

	```sh
	python registry.py pycsw -c reindex -s catalog_slug
	```

9. Delete catalog.
	- Removing records using a server request.
	```sh
	curl -XDELETE http://localhost:8000/catalog/<catalog_slug>/csw
	```

	- From command line.
	```sh
	python registry.py pycsw -c delete_records -s catalog_slug
	```

You should see the indexed information. The ```a.matchDocs``` value refers
to the number of layers returned by the search api.

**Note.** In registry, is possible to read all catalogs and layers. However, the catalog slug is necessary in order to add layers.


Swagger UI
==========

For development and testing of search api using a standalone swagger-ui server, please do the following.

1. Open Google Chrome without web-security.

	```sh
	open -a Google\ Chrome --args --disable-web-security --user-data-dir
	```

2. Download and create a swagger instance specifying a different port.
	```sh
	git clone git@github.com:swagger-api/swagger-ui.git
	python -m SimpleHTTPServer 8001
	```

3. Paste in the api selector, the endpoint for the registry swagger yml configuration file ```http://localhost:8000/api/config```



Reliability
===========

1. List layers uuid and save in a text file.
	```sh
	python registry.py pycsw -c list_layers > uuids.txt
	```

2. Execute checking function for each layer uuid.
	```sh
	cat uuids.txt | python registry.py check_layers > checked_uuids.txt
	```

3. Update Elasticsearch including reliability.
	```sh
	cat checked_uuids.txt | python registry.py reliability
	```

Testing
=======

1. Start elasticsearch

2. Run tests

	```sh
	python setup.py test
	```


Troubleshooting
================

1. Record parsing failed: 'Csw' object has no attribute 'repository'

	```xml
	<ows:ExceptionText>Transaction (insert) failed: record parsing failed: 'Csw' object has no attribute 'repository'</ows:ExceptionText>
	```

	**Reason 1:** Elasticsearch is not running. This makes pycsw to silent the error using exception. Start elasticsearch service.

	**Reason 2:** Database was not configured. Run in console ```python registry.py pycsw -c setup_db```

2. UNIQUE constraint failed: records.identifier.

	```xml
	<ows:ExceptionText>Transaction (insert) failed: ERROR: UNIQUE constraint failed: records.identifier.</ows:ExceptionText>
	```

	**Reason:** Records have been added previously into the database.

3. To debug mapproxy for a single layer.

	- Install mapproxy locally.

		```sh
		pip install MapProxy==1.9.0
		```

	- Retreive from registry the yaml configuration file and copy.

		```sh
		curl http://localhost:8000/layer/<layer_uuid>.yml > layer.yml
		```

	- Create mapproxy local server using the downloaded configuration file. The server will listen port 8080

		```sh
		mapproxy-util serve-develop layer.yml
		```

	- Navigate through mapproxy web server and check the logs in terminal.

	- For arcgis servers, make sure the url path does not have the *?f=json*. Also, verify that layer coordinates are in wgs84 projection.


Features
========

 - [x] CSW-T support via pycsw
 - [x] Mirror information to Elasticsearch for faster searches
 - [x] OpenSearch based API to enable the use of facets on different fields (extending CSW standard).
 - [x] MapProxy support for easy TMS/WMTS access to any kind of resource
 - [x] Multi-catalog support.
