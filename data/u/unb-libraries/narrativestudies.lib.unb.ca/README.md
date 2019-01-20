# narrativestudies.lib.unb.ca
## Lean Instance Repository

## Build Status
| Branch | Status |
|--------|--------|
| dev | [![Build Status](https://travis-ci.org/unb-libraries/narrativestudies.lib.unb.ca.svg?branch=dev)](https://travis-ci.org/unb-libraries/narrativestudies.lib.unb.ca) |
| prod | [![Build Status](https://travis-ci.org/unb-libraries/narrativestudies.lib.unb.ca.svg?branch=prod)](https://travis-ci.org/unb-libraries/narrativestudies.lib.unb.ca) |

### Requirements
The following packages are required to be globally installed on your development instance:

* [PHP7](https://php.org/) - Install instructions [are here for OSX](https://gist.github.com/JacobSanford/52ad35b83bcde5c113072d5591eb89bd).
* [Composer](https://getcomposer.org/)
* [docker](https://www.docker.com)/[docker-compose](https://docs.docker.com/compose/) - An installation HowTo for OSX and Linux [is located here, in section 2.](https://github.com/unb-libraries/docker-drupal/wiki/2.-Setting-Up-Prerequisites).
* [dockworker](https://gist.github.com/JacobSanford/1448fece856be371060d0f16ccb1b194) - Install the dockworker alias.

### 1. Initial Setup
#### A. Configure Local Development
In the ```env/drupal.env``` file, change the environment settings to match your local development environment.

```
DOCKER_ENDPOINT_IP=localhost
LOCAL_USER_GROUP=20
```

* ```DOCKER_ENDPOINT_IP``` - This is the IP of your docker daemon, likely 'localhost'.
* ```LOCAL_USER_GROUP``` - The [group id](https://kb.iu.edu/d/adwf) of your local user. This is used to change permissions when deploying locally.

### 2. Deploy Instance
```
composer install --prefer-dist
```

```
dockworker start-over
```

### 3. Other useful commands
Run ```dockworker``` to get a list of available commands.

## Repository Branches
* `dev` - Core development branch. Deployed to dev when pushed.
* `prod` - Deployed to live when pushed.
