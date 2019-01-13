# QubeStash / Jenkins

[![TravisCI Status Widget]][TravisCI Status] [![Coverage Status Widget]][Coverage Status]

[TravisCI Status]: https://travis-ci.org/qubestash/jenkins
[TravisCI Status Widget]: https://travis-ci.org/qubestash/jenkins.svg?branch=master
[Coverage Status]: https://coveralls.io/r/qubestash/jenkins
[Coverage Status Widget]: https://coveralls.io/repos/github/qubestash/jenkins/badge.svg?branch=master

Based on official docker [jenkins](https://hub.docker.com/_/jenkins/) image. Please read full documentation before running 
this image. 

## Supported tags

* `2.32.1`, `latest` (use `make build`)
* `2.32.1-alpine`, `alpine` (use `make build-alpine`)

## Additional Environment Variables

### JENKINS_THEME_MATERIAL_COLOR

> Default value: `deep-purple`

Will allow Jenkins to load [Material Theme](http://afonsof.com/jenkins-material-theme/) with a certain color.

> Please note theme may only be seen at second docker image restart. Otherwise, please use them install instructions.

### JENKINS_INSTALL_PLUGINS 

> Default value: ``
