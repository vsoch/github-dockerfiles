# DokuWiki Docker Image

## Run:

Run DokuWiki container:

```shell
docker run -p 8080:8080 --name dokuwiki --restart always --detach dokuwiki
```

Setup DokuWiki using [installer](http://localhost/install.php).

## Data container

Create data container:

```shell
docker run --volumes-from dokuwiki --name dokuwiki_data busybox
```

Now you can safely delete dokuwiki container:

```shell
docker stop dokuwiki && docker rm dokuwiki
```

To restore dokuwiki, create new dokuwiki container and attach dokuwiki_data volume to it:

```shell
docker run -publish 80:80 --volumes-from dokuwiki_data --name dokuwiki --restart always --detach dokuwiki
```

## Backup

Create dokuwiki_backup.tar.gz archive in current directory using temporaty container:

```shell
docker run --rm --volumes-from dokuwiki_data --volume $(pwd):/backups alpine:3.6 tar zcvf /backups/dokuwiki_backup.tar.gz /srv
```

## Restore

Run DokuWiki container:

```shell
docker run -p 8080:8080 --name dokuwiki --restart always --detach dokuwiki
```

Create data container:

```shell
docker run --volumes-from dokuwiki --name dokuwiki_data busybox
```

Stop dokuwiki:

```shell
docker stop dokuwiki
```

Restore from backup using temporary container:

```shell
docker run --rm --volumes-from dokuwiki -w / -v $(pwd):/backup alpine:3.6 tar xzvf /backup/dokuwiki_backup.tar.gz
```

Start dokuwiki:

```shell
docker start dokuwiki
```

