# HackRVA-docker-infrastructure
Various Dockerfiles and configuration files to allow restoring HackRVA's non-vital infrastructure quickly when necessary

## Live Usage

Starting this project on the production server necessitates running
`production/initialize.sh`. After the initialization script, run
`docker-compose build` to generate the images for the application. Next, start
the application by running `docker-compose start`.

## Testing and Local Development

Starting this project locally requires running `test/initialize.sh` to
configure the project correctly so that a locally created certificate authority
is utilized. After the initialization script configures this repository, run
`docker-compose build` in order to create the necessary images. Finally, run
`docker-compose up` to start the application locally.

Once the server is running, go to `localhost/.well-known/index.html` to access
the host file and CA cert for the local servers. On most linuces the host file
can be appended to your existing host file at `/etc/hosts`. Installation of the
cert varies significantly based upon your OS and your browser.

