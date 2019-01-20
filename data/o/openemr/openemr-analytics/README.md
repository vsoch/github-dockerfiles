# Shiny Analytics for OpenEMR

This is a testbed for shiny-driven analytics in OpenEMR.

## Prerequisites

Right now, just docker in a 64 bit environment.

## Getting Started

Clone this repo and cd into it. Run `./install-all.sh`, which will take a *long* time to first build the image, but should subsequently be fast when updating. You'll now have OpenEMR, Mysql, and a Shiny server running together.

## Adding Shiny Apps

Just drop them in the `shiny-server/server-contents` directory, which is available as the root directory of your shiny server (ie: `shiny-server/otdi/index.Rmd` will be available at `localhost:3838/otdi`)

Note: the host machine (with its delicious database of information) should be accessible as the host `mysql` from your shiny apps. 

## Adding dependencies

Add them in the Dockerfile, in either the 'install.packages' portion for R packages, or appended to an apt-get command if it is an ubuntu package.

## Using with existing OpenEMR installations

If you're using a docker-compose file to coordinate your existing OpenEMR installation, you can add the shiny segment from the docker-compose.yml included in the root of this repo, along with the shiny-server directory. 
