# meedan/pgadmin

 * `PGADMIN_USER` for user name (default value is `admin@pgadmin.org`)
 * `PGADMIN_PASSWORD` for password (default value is `pgadmin`)

#### EXAMPLE
 ```
 docker run -v ~/pgadmin4/data:/home/pgadmin/.pgadmin -P -e PGADMIN_USER=test@test.com -e PGADMIN_PASSWORD=123456 meedan/pgadmin
 ```

then browse to http://localhost:5050