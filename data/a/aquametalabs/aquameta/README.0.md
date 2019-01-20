# IDE - User interface to Aquameta
Filesystem Foreign Data Wrapper
===============================
Exposes the filesystem to PostgreSQL, allowing files and directories to be read via SQL commands.

Install
-------

First, install the required python modules:

```shell
pip install -r requirements.txt
pip install .
```

Next, install the extension files into PostgreSQL's `extension` directory:
```shell
make install
```

Finally, from a PostgreSQL shell, install the extension:
```sql
CREATE EXTENSION multicorn;
CREATE EXTENSION filesystem_fdw;
```


Usage
-----

### filesystem.file

List files in a directory or show contents of a file

```
-------------------------------------------------------------------------------------------------------------------------------------------
| id                | directory_id | name         | path              | content | permissions | links | size | owner | group | last_mod   |
-------------------------------------------------------------------------------------------------------------------------------------------
| /etc/einstein.jpg | /etc/        | einstein.jpg | /etc/einstein.jpg | ...     | drwxr-xr-x  | 1     | 3    | mic   | staff | Dec 1 2015 |
-------------------------------------------------------------------------------------------------------------------------------------------
```

- ls
```sql
select permissions, links, size, owner, group, last_mod, name from filesystem.file where directory_id = '/var/www/public';
```

- cat
```sql
select content from filesystem.file where path = '/var/www/public/index.php';
```

### filesystem.directory 

List contents of a directory

```
-----------------------------------------------------------------------------------------------------------------------
| id              | parent_id | name   | path               | permissions | links | size | owner | group | last mod   |
-----------------------------------------------------------------------------------------------------------------------
| /var/www/public | /var/www  | public | /var/www/public    | drwxr-xr-x  | 1     | 3    | mic   | staff | Dec 1 2015 |
-----------------------------------------------------------------------------------------------------------------------
```

- ls
```sql
select * from filesystem.directory where parent_id = '/var/www';
```
# A REST/JSON API for database operations

## Components
* uWSGI
* Database functions

## uWSGI
A simple server that creates a REST-like API for querying and modifying data in
the database. When making a request to the server, it parses the URL to get the
API version and resource path, then makes a query to the endpoint.request
function in the database.

### URLS
* /endpoint/0.2/row
* /endpoint/0.2/relation
* /endpoint/0.2/function
* /endpoint/0.2/field

## Database functions
The entry point is a request function that the uWSGI server uses to pass on th
HTTP verb, API version, and resource path.

### endpoint.request

Arguments
* version
* verb
* path
* query_args
* post_data

Out
* status
* message
* response
* mimetype

## How Aquameta processes a request

1. Every request is first processed by the uWSGI server.  The uWSGI server
   connects to PostgreSQL initially as the `anonymous` user, which has a
   limited set of permissions for authenticating and not much else.  If the user
   has a session cookie set, that cookie is checked to be valid and if it is, they
   can keep being that user.  If not, there is no cookie so they are anonymous.

2. Once authentication is handled, the request is routed to the appropriate
   handler based on the requested path.  If the request begins with the base
   endpoint URL (usually `/endpoint`), it is handled as a REST request.
   Otherwise, it is handled by the uWSGI server.



Meta: A writable system catalog extension for PostgreSQL
========================================================

This extension provides two facilities:

1. A set of "meta-identifiers" for unambiguously referencing database objects like tables, views, schemas, roles, etc.
2. A writable system catalog that makes DDL operations accessible via DML operations, allowing PostgreSQL administration via INSERT, UPDATE and DELETE.  It is similar in function to `pg_catalog`, but is updatable and is laid out more sensibly.

INSTALL
-------

Install the extension into PostgreSQL's `extension/` directory:
```shell
make install
```

From a PostgreSQL shell, install meta's required extensions:
```sql
CREATE EXTENSION hstore SCHEMA public;
```

Finally, install the meta extension:
```sql
CREATE EXTENSION meta;
```


USAGE
-----

### Schema
```sql
insert into meta.schema (name) values ('bookstore');
update meta.schema set name = 'book_store' where name = 'bookstore';
delete from meta.schema where name = 'book_store';
```
### Table
```sql
insert into meta.table (schema, name) values ('bookstore', 'book');
update meta.table set name = 'books' where schema = 'bookstore' and name = 'book';
delete from meta.table where name = 'books';
```
### Column
```sql
insert into meta.column (schema, "table", name, type, nullable)
values ('bookstore', 'book', 'price', 'numeric', false);

update meta.column set "default" = 0
where schema = 'bookstore' and "table" = 'book' and name = 'price';
-- or alternatively
update meta.column set "default" = 0
where id = ('bookstore', 'book', 'price')::meta.column_id;

delete from meta.column where id = ('bookstore', 'book', 'price')::meta.column_id;
```
### View
```sql
insert into meta.view (schema, name, query)
values ('bookstore', 'inexpensive_books', 'select * from bookstore.book where price < 5;');

update meta.view
set query = 'select * from bookstore.book where price < 10;'
where id = ('bookstore', 'inexpensive_books')::meta.view_id;
```
### Check Constraint
```sql
insert into meta.constraint_check (schema, "table", name, "check")
values ('bookstore', 'book', 'min_price', 'price > 1');

update meta.constraint_check
set "check" = 'price > 0.50'
where schema = 'bookstore' and "table" = 'book' and name = 'min_price';
```
### Unique Constraint
```sql
insert into meta.constraint_unique (schema, "table", name, columns)
values ('bookstore', 'book', 'unique_name', array['name']);

update meta.constraint_unique
set columns = array['category_id', 'name']
where schema = 'bookstore' and "table" = 'book' and name = 'unique_name';
```
aquameta-endpoint
-----------------

`aquameta-endpoint` is a uWSGI service responsible for receiving HTTP requests
and passing them off to the Aquameta Endpoint extension.  It is a thin
middleware layer that handles authentication, and passes REST and resource
requests to the Aquameta `request` procedure in PostgreSQL.

INSTALL
-------
pip install .
Endpoint nginx Configuration Files
----------------------------------
By default, nginx is configured without SSL encryption.


= Development SSL Configuration
To setup a development SSL server, follow [these instructions](https://www.humankode.com/ssl/create-a-selfsigned-certificate-for-nginx-in-5-minutes).


= Production SSL Configuration
To setup a "real" SSL server with letsencrypt, do something like:
```
sudo apt-get install certbot
sudo certbot --certonly
```

Then copy the `aquameta_endpoint.letsencrypt.conf` file to `/etc/nginx/aquameta_endpoint.conf`.
