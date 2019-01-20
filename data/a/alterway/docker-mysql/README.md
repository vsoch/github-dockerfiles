# Docker Mysql

## Version available

- Mysql/5.5 - (docker tags: `5.5`) - `docker pull alterway/mysql:5.5`
- Mysql/5.6 - (docker tags: `5.6`) - `docker pull alterway/mysql:5.6`



## Environment variables

### Set your my.cnf

The mysqld configuration is dynamic. Just add environment variable with prefix `MYSQLD__`.

Example with docker-compose :

    ...
    environment:
        MYSQLD__max_allowed_packet : '64M'

Please see https://hub.docker.com/_/mysql/ for more details.


## License

View [LICENSE](LICENSE) for the software contained in this image.
