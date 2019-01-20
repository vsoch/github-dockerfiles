# Spina as an EY Container Service

## Introduction

[Spina](https://www.spinacms.com/) is a Rails-based CMS which we adapted to an example app for EY Cloud at [github.com/engineyard/spina_sample_app](https://github.com/engineyard/spina_sample_app).

This example takes the Engine Yard Spina example app and transforms it
to a dockerized Engine Yard Container Service with a RDS database.

It also includes a local setup which helps in development and testing.

## Local Setup

You need a recent version of Docker and Docker Compose installed to be able to run this example.

The `docker-compose.local.yml` file describes the local setup. You can start through the following steps:
1. Create a file `.env` from the `.env.example` file. Fill it with values appropriate for your local environment.
2. Start the database service: `docker-compose -f docker-compose.local.yml up -d database`
3. Initialize the database: `docker-compose -f docker-compose.local.yml run --rm web bundle exec rake db:load_sample_if_empty_db`
4. Start the rails web app: `docker-compose -f docker-compose.local.yml up -d web`
5. View the logs: `docker-compose -f docker-compose.local.yml logs -f`
6. Open the browser and go to [http://localhost:3000/](http://localhost:3000/)
7. Clean up: `docker-compose -f docker-compose.local.yml down`

## Deployment on Engine Yard

To deploy the app as a Container Service on Engine Yard Cloud, you need to go through the following process.

1. Create a RDS service
  1. Database Engine: PostgreSQL 9.6.x
  2. DB Instance type: db.t2.small
  3. Volume size: 10GB
  4. Network: the same in which your App Load Balancer is deployed and in which you will deploy the Container Service.
2. Configure access to the RDS instance from you IP address
  1. This is needed so you can initialize the database.
  2. Open a support ticket, state your IP, and our support team will help you with that.
3. Create a Docker Repository
4. Create a file `.env` from the `.env.example` file.
  1. You can access the database connection details from the "RDS Management" page.
  2. The Docker Repository URI is shown on the "Docker Repositories" page.
5. Init the DB: `docker-compose -f docker-compose.dbinit.yml run --rm dbinit`
6. Build the Docker Image: `docker-compose -f docker-compose.deploy.yml build`
7. Authenticate against the Docker Registry.
  1. The `docker login` command can be copied from the "Docker Repositories" page.
8. Push the Docker Image: `docker-compose -f docker-compose.deploy.yml push`
9.  Create a Container Service Definition
  1.  With one container: rails
  2.  Set the Image repository you created in step 3.
  3.  Yes, the container is essential for the service.
  4.  Exposed Ports: 3000
  5.  Enable Container health check and set the health check command to `wget --spider http://localhost:3000`.
  6.  Click on "Add Container" and then create the Container Service Definition.
10. Deploy a Container Service
  1.  Choose the same Region and Network as your RDS database.
  2.  Desired Count: 1
  3.  Use the default CPU and Memory reservation and configure the same values in the container configuration (set the CPU limit and Memory hard limit).
  4.  Configure load balancing and choose the App Load Balancer which you already created in a prerequisite step.
  5.  Configure the rails container.
  6.  Select the "latest" image tag.
  7.  Setup the environment variables with values from the `.env` file.
  8.  Click on "Save Container Configuration" and then create the Container Service.
11. Request access to the RDS instance from the Container Service
  1.  Open a support ticket, and our support team will help you with that.
12. Verify the Container Service works correctly by accessing the service through the App Load Balancer endpoint.
