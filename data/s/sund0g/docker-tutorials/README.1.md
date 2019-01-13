## Section 5: Docker Compose with Multiple Local Containers

The objectives for this section are,

1. Understand the basics of a docker-compose.yml file.
2. Use docker to create a multi-container web app, using Node as the front end and Redis as the back end database.
3. Understand how to configure the application and Docker such that the containers can communicate with each other.
4. Learn how to use docker-compose to start and stop containers,
	
		docker-compose up [-d]
		
		docker-compose down [-v]
		
	the **-d** option starts the containers in the background.
	
	the **-v** option removes any volumes created as part of the application.

5. Understand container restart policies, (lessons 53 and 54).
6. Learn how to use CLI commands with docker-compose, e.g.

		docker-compose ps
	
	**NOTE:** you have to be in the directory where the docker-compose.yml file is for the CLI commands to work.
