# GFW Blog

The application is a wordpress installation running on Pantheon hosting service.

## Installation

Clone the repo and use one of the following tools to get the project running locally:

### Lando

[Lando](https://github.com/lando/lando) is an open source library for spinning up services or applications without the hassle, and it integrates brilliantly with Pantheon. To develop using lando you will need to be added to the Pantheon project. Please contact someone at Vizzuality before proceeding, and add your public key to your account. Once you have access you can run

    $ lando start

This will build a wordpress docker install and start the server. You will still be missing the database and assets folder. You can pull these with

    $ lando pull
    
This will prompt you for what items you want to pull (code, database, files). As you already have the code, just select database and files. Each time you will be prompted for an environment (dev should be sufficient). Note, lando also allows you to push to Pantheon your changes. You can do this when you want to deploy and changes to the dev environment.

### Local server

If you dont want to use Lando, or are developing without access to Pantheon, you can simple create your own php server with mySQL running. We recommend using [MAMP](https://www.mamp.info/en/)  to set this up. As for database and files, you can create demo content yourself through the wordpress admin fairly painlessly. 

