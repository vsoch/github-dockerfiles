## Section 4: Making Real Projects with Docker

The objective for this section is,

1. Deeper dive into creating Dockerfiles and images containing a simple, nodejs web app.

### Notes:
* **port mapping**: ports specified when starting the container via docker run is as follows,

	`<port-forward>:<port-in>` where,
	
	**Port-forward:** route incoming requests on this port (on localhost) to…
		
	**Port-in:** ...this port inside the container 

* Files inside a running container can be modified, (via exec), but if they are part of a web server, you will have to stop/restart the web server for the changes to be picked up.
