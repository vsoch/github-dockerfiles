MySQL (Percona Server)

- Exposed port: `3306`
- Exposed volumes
  - Data directory: `/var/lib/mysql`
  - Configuration directory: `/var/lib/mysql`

```sh
$ docker run -d -p 3306:3306 orgsync/mysql
#=> container id

$ mysql -h $(boot2docker ip)
#=> Server version: 5.6.21-69.0-log Percona Server (GPL), Release 69.0, Revision 675
#=> mysql>
```
