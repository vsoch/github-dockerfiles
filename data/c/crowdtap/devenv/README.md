Crowdtap Dev Environment
========================

Long gone are the days of installing dependencies for our apps with Boxen or Homebrew. No longer will you have to say "works locally, but not in test or production". Bring on the containers!

![Containerize, All the Things!](http://cdn.meme.li/instances/300x/53435641.jpg)

Say what? That's right, we now have a container for everything. This includes all services (Mongo/Toku, Postgres, ElasticSearch, Redis, Memcache, etc.) as well as one for each backend application.

Installation
------------

All you need to do is
```
curl -s http://bit.ly/1mvr3Mj | bash
```

Feel free to have a look at the source, `bin/install.sh` to see what it will do.


Getting Started
---------------
```
Usage: devenv <ssh|start|stop|update>

  rebuild: Wipe out the VM and rebuild from scratch
  ssh:     SSH into the environment
  start:   Bring up the environment
  stop:    Bring down the environment
  update:  Update all components
```

Looking at the usage above, its easy to see that your first step should be: `devenv start`. This will create a VM inside VirtualBox if you don't have one already and start it up for you. When the command completes, you can then `devenv ssh` to get inside of the VM. Once inside, you will be given a nice command prompt, which comes from our [dotfiles](https://github.com/crowdtap/dotfiles). You will also find familiar tools such as `vim`, `ack` and others.

Filesystem
----------

The environment matches what is in production, so the apps reside in `/srv/<app>`, which is also where you will find `logs`. If you are looking for logs from a specific service, they are located under `/var/log`.

Inspiration
-----------

This would not exist without the repo from RelateIQ: [docker_public](https://github.com/relateiq/docker_public) and their [presentation from DockerCon 2014](http://blog.docker.com/2014/07/dockercon-video-docker-at-relateiq/).

Contributing
------------

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request


License
-------

MIT, see `LICENSE`.
