
# Getting Started w/ Mixtapes Server

For this app, we make heavy use of the Spotify API. For security, we've left out any reference to Spotify Credentials, App Keys, or Secrets necessary to use the app.
In order to get started developing, please contact `james.walton@frogdesign.com` (or other admin) to get the appropriate Spotify information added to the `make_env` for this container.

1.  Navigate to your project root directory and copy the contents of this repository to that location.
2.  Create a copy of `make_env.dist` and rename it to `make_env`.  Update with your project specific information.
3.  'make build'
4.  'make shell'
5.  'npm install'
6.  'npm start'

# Success
1.  If successful, you will see "Server running on port:: 3000" in your console.

# Environment Variables

(see noted above re: Spotify)
You may pass additional environment variables to your application by including them in your `make_env` file.  Follow these steps to add new environment variables.

1.  Add your environment variable to your `make_env` file inside the DOCKER_ENV specification.  Remember, the last line does not get a trailing slash.
2.  Destroy your existing container and rebuild it using `make build`.
3.  Run and re-attach to your updated container using `make shell`.
