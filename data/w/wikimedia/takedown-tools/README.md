# takedown-tools [![Build Status](https://travis-ci.org/wikimedia/takedown-tools.svg?branch=master)](https://travis-ci.org/wikimedia/takedown-tools)
Tools for the Wikimedia Support and Safety team related to content takedown

## Setup
1. Copy the `.env.dist` file to `.env` and customize however you would like.
2. To login to the app, you will need to obtain OAuth Keys by registering an
	 [OAuth Consumer](https://meta.wikimedia.org/wiki/Special:OAuthConsumerRegistration/propose)
	 (not an owner-ownly as it will need a callback url). With at least the
	 following permissions:
	 - [High-volume editing](https://meta.wikimedia.org/wiki/Special:ListGrants#highvolume)
	 - [Edit existing pages](https://meta.wikimedia.org/wiki/Special:ListGrants#editpage)
	 - [Access private information](https://meta.wikimedia.org/wiki/Special:ListGrants#privateinfo)
3. Execute `docker-compose up`
4. After the database has started and ready to accept connections, open another
   terminal
5. Execute `docker-compose exec api key-create` to create the JWT key.
6. Execute `docker-compose exec api db-setup` to create the database schema and
	  load the fixtures.

## Running
Once the app has been setup, you can start the app by executing (if you haven't
already done so in step 3):
```
docker-compose up
```

## Deploying
1. Connect to [Wikimedia Foundation's Virtual Private Network](https://office.wikimedia.org/wiki/Office_IT/OpenVPN_Setup).
2. SSH into the production server:
   ```
	 ssh lcatools.corp.wikimedia.org
	 ```
3. Switch to the `lcatools` user:
   ```
	 sudo su - lcatools
	 ```
4. Change into the `takedowntools` directory:
   ```
	 cd sites/takedowntools
	 ```
5. Pull the changes:
   ```
	 git pull origin master
	 ```
6. Build the container(s)
   ```
	 docker-compose build
	 ```
7. Start the new containers:
   ```
	 docker-compose up -d
	 ```
