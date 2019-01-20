# README

## Setup Notes

Before running `bin/setup` you need to set two environment variables: `FOREIGN_DATABASE_USERNAME` and `FOREIGN_DATABASE_PASSWORD` to comport with the username and password of your postgres foreign database.

You will need a mapquest api key set `MAPQUEST_API_KEY` in your .env for the geocoder to work.

Before running the test suite you need to enable the foreign data wrapper in the test database:

  RAILS_ENV=test rake db:add_foreign_data_wrapper_interface
  RAILS_ENV=test rake db:add_rpa_fdw
  RAILS_ENV=test rake db:add_counties_fdw
  RAILS_ENV=test rake db:add_municipalities_fdw

### Postgres Security Challenges

In order to implement foreign data wrappers your postgres user defined in `database.yml` needs to have super user privileges or it will fail. You can do this with: `ALTER ROLE massbuilds WITH SUPERUSER;`

The foreign database also needs to allow connections via pg_hba.conf in the following manner:

```
ubuntu@ip:/etc/postgresql/9.5/main$ sudo vi pg_hba.conf
ubuntu@i:/etc/postgresql/9.5/main$ sudo pg_ctlcluster 9.5 main restart -m fast
```

Also make sure the foreign_database_username and foreign_database_password attributes are set in `secrets.yml`.

You also may need to set your Postgres development environment database variables in .env:

`POSTGRES_USER`: should be set to the development database postgres username
`POSTGRES_DEV_HOST`: should be set to the host of the development database
`POSTGRES_PASSWORD`: should be set to the password of the development database username

### Latitude and Longitude Script
If you run into an error about a development or edit not containing latitude or longitude as a required property, you might need to run `rake database:populate_long_lat` to populate the latitude and longitude fields from the point field.
