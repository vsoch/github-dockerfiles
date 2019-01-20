This docker container aims to minimize the efforts to get a development
environment running. The idea is that you simply run this container and start
hacking. The container mounts the repository root as volume and does not store
any data within itself.

The container comes preinstalled with all static dependencies. In addition, it
takes care of the following:
* installing npm dependencies
* installing bower dependencies
* running `grunt serve`
