
CONTENTS OF THIS FILE
---------------------

 * About Drupal
 * Configuration and features
 * Installation profiles
 * Appearance
 * Developing for Drupal

ABOUT DRUPAL
------------

Drupal is an open source content management platform supporting a variety of
websites ranging from personal weblogs to large community-driven websites. For
more information, see the Drupal website at http://drupal.org/, and join the
Drupal community at http://drupal.org/community.

Legal information about Drupal:
 * Know your rights when using Drupal:
   See LICENSE.txt in the same directory as this document.
 * Learn about the Drupal trademark and logo policy:
   http://drupal.com/trademark

CONFIGURATION AND FEATURES
--------------------------

Drupal core (what you get when you download and extract a drupal-x.y.tar.gz or
drupal-x.y.zip file from http://drupal.org/project/drupal) has what you need to
get started with your website. It includes several modules (extensions that add
functionality) for common website features, such as managing content, user
accounts, image uploading, and search. Core comes with many options that allow
site-specific configuration. In addition to the core modules, there are
thousands of contributed modules (for functionality not included with Drupal
core) available for download.

More about configuration:
 * Install, upgrade, and maintain Drupal:
   See INSTALL.txt and UPGRADE.txt in the same directory as this document.
 * Learn about how to use Drupal to create your site:
   http://drupal.org/documentation
 * Download contributed modules to sites/all/modules to extend Drupal's
   functionality:
   http://drupal.org/project/modules
 * See also: "Developing for Drupal" for writing your own modules, below.

INSTALLATION PROFILES
---------------------

Installation profiles define additional steps (such as enabling modules,
defining content types, etc.) that run after the base installation provided
by core when Drupal is first installed. There are two basic installation
profiles provided with Drupal core.

Installation profiles from the Drupal community modify the installation process
to provide a website for a specific use case, such as a CMS for media
publishers, a web-based project tracking tool, or a full-fledged CRM for
non-profit organizations raising money and accepting donations. They can be
distributed as bare installation profiles or as "distributions". Distributions
include Drupal core, the installation profile, and all other required
extensions, such as contributed and custom modules, themes, and third-party
libraries. Bare installation profiles require you to download Drupal Core and
the required extensions separately; place the downloaded profile in the
/profiles directory before you start the installation process. Note that the
contents of this directory may be overwritten during updates of Drupal core;
it is advised to keep code backups or use a version control system.

Additionally, modules and themes may be placed inside subdirectories in a
specific installation profile such as profiles/your_site_profile/modules and
profiles/your_site_profile/themes respectively to restrict their usage to only
sites that were installed with that specific profile.

More about installation profiles and distributions:
 * Read about the difference between installation profiles and distributions:
   http://drupal.org/node/1089736
 * Download contributed installation profiles and distributions:
   http://drupal.org/project/distributions
 * Develop your own installation profile or distribution:
   http://drupal.org/developing/distributions

APPEARANCE
----------

In Drupal, the appearance of your site is set by the theme (themes are
extensions that set fonts, colors, and layout). Drupal core comes with several
themes. More themes are available for download, and you can also create your own
custom theme.

More about themes:
 * Download contributed themes to sites/all/themes to modify Drupal's
   appearance:
   http://drupal.org/project/themes
 * Develop your own theme:
   http://drupal.org/documentation/theme

DEVELOPING FOR DRUPAL
---------------------

Drupal contains an extensive API that allows you to add to and modify the
functionality of your site. The API consists of "hooks", which allow modules to
react to system events and customize Drupal's behavior, and functions that
standardize common operations such as database queries and form generation. The
flexible hook architecture means that you should never need to directly modify
the files that come with Drupal core to achieve the functionality you want;
instead, functionality modifications take the form of modules.

When you need new functionality for your Drupal site, search for existing
contributed modules. If you find a module that matches except for a bug or an
additional needed feature, change the module and contribute your improvements
back to the project in the form of a "patch". Create new custom modules only
when nothing existing comes close to what you need.

More about developing:
 * Search for existing contributed modules:
   http://drupal.org/project/modules
 * Contribute a patch:
   http://drupal.org/patch/submit
 * Develop your own module:
   http://drupal.org/developing/modules
 * Follow best practices:
   http://drupal.org/best-practices
 * Refer to the API documentation:
   http://api.drupal.org/api/drupal/7
# What is the Open Government Partnership?

[Open Government Partnership](http://www.opengovpartnership.org/) (OGP) is a
project that was launched in 2011 to provide an international platform for domestic reformers committed to making their governments more open, accountable, and responsive to citizens.

This repository contains the new OGP web app of 2016.

![Cover picture](/sites/all/themes/custom/ogp_theme/screenshot.png?raw=true "Cover Home page")


# Technology and dependencies

The project is based on [Drupal 7](https://www.drupal.org/). You will also need [npm](https://www.npmjs.com/) to install
and process JavaScript and SASS assets.

# Set up - native

A [LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)) or similar stack is recommended, although the project should
also work with different operating systems, web servers or database servers. Follow any Drupal 8 installation guide to learn
how to set up your environment



To build the project assets (JavaScript and CSS compiling) you first need to install the asset compiler and its dependencies:

```
npm install
```

After, run the following command to generate the actual assets:

```
npm run build
```

If you are manipulating those assets, you might prefer a watch command, that tracks changes and automatically updates the
generated files

```
npm run watch
```

# Set up - Docker

#### Copy Docker's settings file (only once)
 * In the terminal, move to the project root and execute:
 ```
 cp sites/default/settings.docker.php sites/default/settings.php
 ```

#### Populate the database
 * See the instructions bellow on how to import existing data to your database:

#### Build the image using Docker Composer
- Install dependencies
```
npm install
```

- Start the project
```
npm start docker
```


#### Enjoy
  * Open the browser and access [http://localhost:8010](http://localhost:8010)


#### Extra - To access the server's bash
 * Open the terminal and type:
 ```
 docker exec -ti ogp bash
 ```


## Managing your database

As Drupal projects rely heavily on the database, you need to make sure to import and export your database at relevant times


### Using a local database server

#### Importing from source to local database server

```
database/import.sh <host> <user> <database>
```

#### Exporting from local database server to source

```
database/export.sh <host> <user> <database>
```

### Using a docker database container

#### Importing from source to local database server

```
docker exec -ti ogp /var/www/html/database/import.sh db root ogp
```

#### Exporting from local database server to source

Use the following to clear caches:

```
docker exec -ti ogp drush cc all
```

Then, use this command to export the database:

```
docker exec -ti ogp /var/www/html/database/export.sh db root ogp
```

# License

This project is available as OSS under the [GPL v2](/LICENSE.txt) license
