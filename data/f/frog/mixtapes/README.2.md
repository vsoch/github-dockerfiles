# RAD Nginx
A starting point for containerized Nginx instances.  Based on RAD Container:  https://github.com/frog/rad-container

# Getting Started
To get started using this Nginx container, you must have the latest version of Docker installed on your system.  If you are using an older version of Docker, please uninstall it and use the appropriate installer from the docker website.

https://docs.docker.com/engine/installation/

Once Docker is installed on your machine, follow the steps below to begin developing your application.  This is intended for local development, and will map your project root directory into the container and auto restart the application when changes are made.

1.  Navigate to your project root directory and copy the contents of this repository to that location.
2.  Create a copy of `make_env.dist` and rename it to `make_env`.  Update with your project specific information.
3.  Edit `/config/sites-enabled/default` or add an additional config file in `/config/sites-enabled/` with the server configuration you want to use.
3.  `make build`
4.  `make start`

# Success
1.  If successful, the location(s) you configured will route http traffic as expected from the host location.

# Troubleshooting

1.  If you are using Chrome and are experiencing issue with browser caching - try the steps outlined here to temporarily disable browser caching:  http://stackoverflow.com/questions/5690269/disabling-chrome-cache-for-website-development