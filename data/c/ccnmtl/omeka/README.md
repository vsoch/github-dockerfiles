# CTL's Omeka container

This used to be based on `erochest/omeka`, but we needed to upgrade to a newer omeka, and now build the omeka image ourselves and then adds our plugins.

The db.ini looks for database credentials in the default mysql environment variables, and can be set up with a linked mysql container (in dev), or against our database server in prod.

See [Dockerizing Omeka](http://wiki.ccnmtl.columbia.edu/index.php/Docker_-izing_Omeka) for more info.

This omeka container needs to be linked to a postfix container and a storage container, and optionally, a mysql container (unless it is set up to connect to a non-docker mysql database).

It can be started with a command similar to the following:

```bash
/usr/bin/docker run \
   -p 8880:80 \
   --volumes-from=omeka-data \
   --link mysql:mysql \
   --link postfix:postfix \
   localhost:5000/ccnmtl/omeka
```

Where, omeka-data is simply

```bash
/usr/bin/docker run \
   --name=omeka-data \
   -v /var/local/docker/ data/omeka-files:/app/files \
   -v /app/files \
   localhost:5000/ccnmtl/omeka \
   /bin/echo I am a data only container
```

## docker-compose

If you have `docker-compose` installed, the simplest way to use this
for development is to checkout the code, go into the directory with it
and run:

`$ docker-compose up`

Then visit `http://localhost:8880/install/install.php` and configure
your site. If you run into a message that `mod_rewrite` isn't enabled,
you may need to manually change the path `/install/install.php`
(something seems buggy with omeka's module detection).

This setup should be enough to get started with, but is not ideal for
production since it doesn't split out the data volume. If you want a
persistent data volume, you will need to set it up as described above.
