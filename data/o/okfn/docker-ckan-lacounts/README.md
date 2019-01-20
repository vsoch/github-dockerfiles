# Docker Compose setup for the LA Counts project

**Note**: This is intended just as a development setup. Don't push any production specific configuration or code, specially secrets.

Based on the main [Docker Compose setup](https://github.com/okfn/docker-ckan) for CKAN.

These images and Docker Compose files are used to deploy the LA Counts web app. There are different compose files based on the environment:

## Local development

Use `docker-compose.dev.yml`:

    docker-compose -f docker-compose.dev.yml build
    docker-compose -f docker-compose.dev.yml up -d

This starts all necessary services. Make sure to clone [ckanext-lacounts](https://github.com/okfn/ckanext-lacounts) in the `src` folder.


## Updating upstream CKAN images

If you want to get upstream changes in  `ckan-base` or `ckan-dev` in the local `ckan` images run the following commands:

	docker pull openknowledge/ckan-base:2.8
	docker pull openknowledge/ckan-dev:2.8
	docker-compose -f docker-compose.dev.yml build ckan-dev
	docker-compose -f docker-compose.dev.yml stop ckan-dev
	docker-compose -f docker-compose.dev.yml rm -f ckan-dev
	docker-compose -f docker-compose.dev.yml up -d
