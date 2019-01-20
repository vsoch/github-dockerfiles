docker-cakephp-cloud
==============
Just a little Docker POC in order to have a self-contained CakePHP application running in a clustered container environment using
docker-compose or docker-cloud tools in a production environment. This image is ready to be scaled out horizonally
on a docker swarm cluster, kubernetes, mesos, docker cloud, etc. It also has Ansible and Let's Encrypt baked-in for
configuration management and free SSL certificate generation. Did I mention it has built-in load-balancing that you don't
have to think about?

## Inspiration
This project was inspired by another project that I developed, [docker-cakephp](https://github.com/Dynamictivity/docker-cakephp),
which was originally based off the code from [docker-symfony](https://github.com/eko/docker-symfony). This new project is a
complete rewrite of docker-cakephp based on my experiences in using it over the last several months to manage several CakePHP
projects in Docker.

## How it works?
The docker container contains all necessary libraries, php-processing and proxy tools to run a self-contained CakePHP
application, minus the database.

Here are the default `docker-compose` images:

* `db`: This is the MySQL database container (can be changed to postgresql or whatever in `docker-compose.yml` file)
* `cakephp`: This is the PHP-FPM container including the application volume mounted on

This results in the following running containers:

```bash
> $ docker-compose ps
        Name                    Command             State                   Ports                 
  -----------------------------------------------------------------------------------------------
  vagrant_cakephp_1   /sbin/my_init                 Up      443/tcp, 0.0.0.0:80->80/tcp, 9000/tcp
  vagrant_db_1        docker-entrypoint.sh mysqld   Up      0.0.0.0:3306->3306/tcp         
```

```bash
> $ docker stats
CONTAINER           CPU %               MEM USAGE / LIMIT       MEM %
e231fff8c78b        0.01%               83.83 MiB / 488.7 MiB   17.16%      vagrant_cakephp_1
1f59f3d11d14        0.06%               102.1 MiB / 488.7 MiB   20.89%      vagrant_db_1
```

## Docker Hub
This image is available on [Docker Hub](https://hub.docker.com/r/dynamictivity/docker-cakephp-cloud/)

## Recommendations
- It is recommended to utilize this stack with database sessions, so your sessions can be persisted across all running
    instances of your application.
- It is also recommended that you mount your `/tmp`, `logs` and `uploads` directories as Docker volumes in order to
    share them across all running instances.

## Contributing
Please see [Contributing](CONTRIBUTING.md) for instructions on contributing to this repository.

## Features
- Ubuntu 16.04
- PHP 7.0
- Built-in `NGINX` proxy server
- Ready for `docker-gen`/`nginx-proxy` for automated cluster-based load-balancing and Let's Encrypt SSL certificate
    management
- Ability to clone repository into docker container upon startup
- `Ansible` built-in for extreme configuration management
  - Anything you can do with `Ansible`, can be done in containers built using this image
- Built on [baseimage-docker](https://github.com/phusion/baseimage-docker) for great flexibility
  - All features and functionality from `baseimage-docker` are available in this image

## Installed Packages
```
netcat
unzip
php
php-sqlite3
php-pear
php-ldap
php-pgsql
php-mcrypt
php-mbstring
php-gmp
php-json
php-mysql
php-gd
php-odbc
php-xmlrpc
php-memcache
php-curl
php-imagick
php-intl
php-fpm
git
curl
wget
libxrender1
nginx
ansible
nano
```

## Todo
- Get database sessions working (currently it always creates the `data` field of the `sessions` table as `binary(255)`
    no-matter what)
- Suggestions?

# Usage
There are multiple ways to use this container and I will describe the common, recommended ways, below.

### Method 1 (preferred): Build your app inside the image
You can build your app into the container image by adding a `Dockerfile` similar to the following to your application
source code repository.

```
FROM dynamictivity/docker-cakephp-cloud:latest

# Add source code
ADD . /source

# Add custom init scripts
#ADD app-init.sh /etc/my_init.d/app-init.sh

```

After you do that, you'll want to setup `docker-compose` using a `docker-compose.yml` similar to the following:

```
version: '2'
services:
  db:
    image: mariadb:5.5
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: 'cakephp'
      MYSQL_DATABASE: 'cakephp'
  cakephp:
    build: .
    expose:
      - "9000"
    volumes:
      - /www
      - /mnt/docker/cakephp/logs:/www/logs
      - /mnt/docker/cakephp/tmp:/www/tmp
    links:
      - db
    environment:
      DEBUG: 'true'
      DB_HOST: 'db' # Leave this as 'db' to utilize MySQL container(s)
      DB_USERNAME: 'root'
      DB_PASSWORD: 'cakephp'
      DB_DATABASE: 'cakephp'
      DB_SEED: 'DatabaseSeed'
      EMAIL_HOST: 'localhost'
      EMAIL_PORT: '25'
      EMAIL_TIMEOUT: '30'
      EMAIL_USERNAME: 'user'
      EMAIL_PASSWORD: 'secret'
      EMAIL_TLS: 'false'
      SECURITY_SALT: '4F3mzqXRuQ4X9S9sR2d64YV2Ftcfd2KVek678m4K63q35g9z7YT8YwEu4s46A25Y'
    ports:
        - "80:80"
```

Next, build your application:

```bash
$ docker-compose build
```

Then, run:

```bash
$ docker-compose up -d
```

You can check the status of your running application using the following command:

```bash
$ docker-compose logs
```

### Method 2: Auto-clone your app to the container
First, clone this repository:

```bash
$ git clone git@github.com:Dynamictivity/docker-cakephp-cloud.git
```

Next, edit the `docker-compose.yml` file and change the `REPO:` value to the URL of your application's GIT repository.

Finally (required only for SSH GIT repositories), edit `config/id_rsa` file and put your GIT deployment (private key)
in there so that the docker container can access your private GIT repository. If you are using GIT via SSH you'll also
want to change the `REPO_HOST:` value to the FQDN of your GIT server host, that way the host key can be automatically
accepted.

Then, run:

```bash
$ docker-compose up
```

You are done, you can visit your CakePHP application on the following URL: `http://localhost`

_Note :_ you can rebuild all Docker images by running:

```bash
$ docker-compose build
```

# Custom Application Configuration

### Database Migrations and Seeds
When the container spins up it runs the following 2 commands (aside from `composer install`):

```bash
$ cd /www; bin/cake migrations migrate
$ cd /www; bin/cake migrations seed --seed $DB_SEED
```

You can specify the database seed file inside of `docker-compose.yml` by changing the `DB_SEED:` value to that of your database seed file.

### E-Mail Configuration
Change the following variables in `docker-compose.yml` to configure email in your application:

```
EMAIL_HOST: 'localhost'
EMAIL_PORT: '25'
EMAIL_TIMEOUT: '30'
EMAIL_USERNAME: 'user'
EMAIL_PASSWORD: 'secret'
EMAIL_TLS:
```

### Security Salt
Be sure to update the `SECURITY_SALT` value in the `docker-compose.yml`.

```
environment:
  DEBUG: 'true'
  DB_HOST: 'db' # Leave this as 'db' to utilize MySQL container(s)
  DB_USERNAME: 'root'
  DB_PASSWORD: 'cakephp'
  DB_DATABASE: 'cakephp'
  DB_SEED: 'DatabaseSeed'
  EMAIL_HOST: 'localhost'
  EMAIL_PORT: '25'
  EMAIL_TIMEOUT: '30'
  EMAIL_USERNAME: 'user'
  EMAIL_PASSWORD: 'secret'
  EMAIL_TLS: 'false'
  REPO: 'https://gitlab.dynamictivity.com/cakephp/cakephp-bookmarker.git'
  REPO_HOST: 'gitlab.dynamictivity.com'
  SECURITY_SALT: '4F3mzqXRuQ4X9S9sR2d64YV2Ftcfd2KVek678m4K63q35g9z7YT8YwEu4s46A25Y'
```

## Read logs
You can access Nginx and CakePHP application logs in the following directories on your host machine, provided you use
the recommended docker-compose configuration:

* `/mnt/docker/cakephp/logs`

# docker-gen nginx-proxy and Let's Encrypt
This image is setup to work with `docker-gen/nginx-proxy` for easy, automated cluster-based load-balancing. You can
try out the automated load-balancing functionality using the following `docker-compose.yml`:

```
version: '2'
services:
  db:
    image: mariadb:5.5
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: 'cakephp'
      MYSQL_DATABASE: 'cakephp'
    ports:
        - "3306:3306"
  cakephp:
    build: .
    restart: always
    volumes:
      - '/www'
      - '/mnt/docker/cakephp/logs:/www/logs'
      - '/mnt/docker/cakephp/tmp:/www/tmp'
    links:
      - db
    environment:
      DEBUG: 'true'
      DB_HOST: 'db' # Leave this as 'db' to utilize MySQL container(s)
      DB_USERNAME: 'root'
      DB_PASSWORD: 'cakephp'
      DB_DATABASE: 'cakephp'
      DB_SEED: 'DatabaseSeed'
      EMAIL_HOST: 'localhost'
      EMAIL_PORT: '25'
      EMAIL_TIMEOUT: '30'
      EMAIL_USERNAME: 'user'
      EMAIL_PASSWORD: 'secret'
      EMAIL_TLS: 'false'
      VIRTUAL_HOST: 'example.com'
      LETSENCRYPT_HOST: 'example.com'
      LETSENCRYPT_EMAIL: 'support@example.com'
    expose:
      - '80'
  nginx:
    restart: always
    image: nginx
    container_name: nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - "/etc/nginx/conf.d"
      - "/etc/nginx/vhost.d"
      - "/usr/share/nginx/html"
      - "/mnt/docker/cakephp/proxy/certs:/etc/nginx/certs:ro"
  nginx-gen:
    restart: always
    image: jwilder/docker-gen
    container_name: nginx-gen
    volumes:
      - "/var/run/docker.sock:/tmp/docker.sock:ro"
      - "/mnt/docker/cakephp/proxy/templates/nginx.tmpl:/etc/docker-gen/templates/nginx.tmpl:ro"
    volumes_from:
      - nginx
      - cakephp
    entrypoint: /usr/local/bin/docker-gen -notify-sighup nginx -watch -wait 5s:30s /www/config/nginx.tmpl /etc/nginx/conf.d/default.conf
```

You can now scale up your cakephp service and it will automatically be added to the load-balancer by running the following command:

```bash
$ docker-compose scale cakephp=3
```

Here's the containers you should now see running:

```bash
$ docker-compose ps
         Name                   Command                   State                    Ports
-------------------------------------------------------------------------------------------------
nginx                    nginx -g daemon off;     Up                       0.0.0.0:443->443/tcp,
                                                                           0.0.0.0:80->80/tcp
nginx-gen                /usr/local/bin/docker-   Up
                         gen  ...
vagrant_cakephp_1        /sbin/my_init            Up                       443/tcp, 80/tcp,
                                                                           9000/tcp
vagrant_cakephp_2        /sbin/my_init            Up                       443/tcp, 80/tcp,
                                                                           9000/tcp
vagrant_cakephp_3        /sbin/my_init            Up                       443/tcp, 80/tcp,
                                                                           9000/tcp
vagrant_db_1             docker-entrypoint.sh     Up                       0.0.0.0:3306->3306/tcp
                         mysqld
```

If you want to add automated SSL certificate generation using Let's Encrypt simply add this to your `docker-compose.yml`:

```
  letsencrypt-nginx-proxy-companion:
    restart: always
    image: jrcs/letsencrypt-nginx-proxy-companion
    container_name: letsencrypt-nginx-proxy-companion
    volumes_from:
      - nginx
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "/mnt/docker/cakephp/proxy/certs:/etc/nginx/certs:rw"
    environment:
      - "NGINX_DOCKER_GEN_CONTAINER=nginx-gen"
```

# Vagrant
You can also use `vagrant` for testing by typing the following commands from the work tree:

```bash
$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ docker-compose build
$ docker-compose up
```

# Ansible
Ansible is used inside the docker image to configure NGINX. You may find our custom configuration in
[ansible/playbook.yml](ansible/playbook.yml)). This is based on another open-source project from Dynamictivity called
[nginx-ansible](https://gitlab.dynamictivity.com/dynamictivity/nginx-ansible). The original code is modified from a
pre-existing nginx Ansible role: https://galaxy.ansible.com/jdauphant/nginx/ by jdauphant.

This docker container has the ability to pull in a playbook specification from a remote URL and automatically run that
playbook on container startup. Primarily this is used to configure the in-build nginx server which is running in this
container, however that doesn't stop you from configuring Ansible in this container to perform any number of additional
tasks.

### Configuring Ansible Playbooks

### Pull in Remote Playbook
Simply pass in the environment variable `ANSIBLE_PLAYBOOK_URL` with the url of your remote playbook.

### Pull in Ansible Galaxy Roles
Pass in the environment variable `ANSIBLE_GALAXY_ROLES` as a comma-separated list of roles. The container will
automatically download them on start-up.

#### Example docker-compose.yml
```
version: '2'
services:
    nginx-ansible:
        build: .
        ports:
            - "80:80"
            - "443:443"
        environment:
            ANSIBLE_PLAYBOOK_URL: http://gitlab.dynamictivity.com/ansible/nginx-ansible/snippets/1/raw
            ANSIBLE_GALAXY_ROLES: "carlosbuenosvinos.ansistrano-deploy,jdauphant.nginx,ANXS.postgresql,dev-sec.os-hardening"
```

Role Variables
--------------
The variables that can be passed to this role and a brief description about
them are as follows. (For all variables, take a look at [ansible/roles/nginx/defaults/main.yml](ansible/roles/nginx/defaults/main.yml))

```yaml
# The user to run nginx
nginx_user: "www-data"

# A list of directives for the events section.
nginx_events_params:
 - worker_connections 512
 - debug_connection 127.0.0.1
 - use epoll
 - multi_accept on

# A list of hashes that define the servers for nginx,
# as with http parameters. Any valid server parameters
# can be defined here.
nginx_sites:
 default:
     - listen 80
     - server_name _
     - root "/usr/share/nginx/html"
     - index index.html
 foo:
     - listen 8080
     - server_name localhost
     - root "/tmp/site1"
     - location / { try_files $uri $uri/ /index.html; }
     - location /images/ { try_files $uri $uri/ /index.html; }
 bar:
     - listen 9090
     - server_name ansible
     - root "/tmp/site2"
     - location / { try_files $uri $uri/ /index.html; }
     - location /images/ {
         try_files $uri $uri/ /index.html;
         allow 127.0.0.1;
         deny all;
       }

# A list of hashes that define additional configuration
nginx_configs:
  proxy:
      - proxy_set_header X-Real-IP  $remote_addr
      - proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for
  upstream:
      - upstream foo { server 127.0.0.1:8080 weight=10; }
  geo:
      - geo $local {
          default 0;
          127.0.0.1 1;
        }
  gzip:
      - gzip on
      - gzip_disable msie6

# A list of hashes that define user/password files
nginx_auth_basic_files:
   demo:
     - foo:$apr1$mEJqnFmy$zioG2q1iDWvRxbHuNepIh0 # foo:demo , generated by : htpasswd -nb foo demo
     - bar:$apr1$H2GihkSo$PwBeV8cVWFFQlnAJtvVCQ. # bar:demo , generated by : htpasswd -nb bar demo

```

Examples
========
1) Install nginx with HTTP directives of choice, but with no sites
configured and no additionnal configuration:

```yaml
- hosts: all
  roles:
  - role: nginx,
    nginx_http_params: ["sendfile on", "access_log /var/log/nginx/access.log"]
```

2) Install nginx with different HTTP directives than in the previous example, but no
sites configured and no additional configuration.

```yaml
- hosts: all
  roles:
  - role: nginx,
    nginx_http_params: ["tcp_nodelay on", "error_log /var/log/nginx/error.log"]
```

Note: Please make sure the HTTP directives passed are valid, as this role
won't check for the validity of the directives. See the nginx documentation
for details.

3) Install nginx and add a site to the configuration.

```yaml
- hosts: all

  roles:
  - role: nginx
    nginx_http_params:
      - sendfile "on"
      - access_log "/var/log/nginx/access.log"
    nginx_sites:
      bar:
        - listen 8080
        - location / { try_files $uri $uri/ /index.html; }
        - location /images/ { try_files $uri $uri/ /index.html; }
    nginx_configs:
      proxy:
        - proxy_set_header X-Real-IP  $remote_addr
        - proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for
```

4) Install nginx and add extra variables to default config

```yaml
-hosts: all
  vars:
    - my_extra_params:
      - client_max_body_size 200M
# retain defaults and add additional `client_max_body_size` param
  roles:
    - role: jdauphant.nginx
      nginx_http_params: "{{ nginx_http_params_defaults + my_extra_params }}"
```

Note: Each site added is represented by a list of hashes, and the configurations
generated are populated in /etc/nginx/site-available/ and linked from /etc/nginx/site-enable/ to /etc/nginx/site-available.

The file name for the specific site configuration is specified in the hash
with the key "file_name", any valid server directives can be added to the hash.
Additional configurations are created in /etc/nginx/conf.d/

5) Install Nginx, add 2 sites (different method) and add additional configuration

```yaml
- hosts: all
  roles:
    - role: nginx
      nginx_http_params:
        - sendfile on
        - access_log /var/log/nginx/access.log
      nginx_sites:
         foo:
           - listen 8080
           - server_name localhost
           - root /tmp/site1
           - location / { try_files $uri $uri/ /index.html; }
           - location /images/ { try_files $uri $uri/ /index.html; }
         bar:
           - listen 9090
           - server_name ansible
           - root /tmp/site2
           - location / { try_files $uri $uri/ /index.html; }
           - location /images/ { try_files $uri $uri/ /index.html; }
      nginx_configs:
         proxy:
            - proxy_set_header X-Real-IP  $remote_addr
            - proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for
```

6) Install Nginx, add 2 sites, add additional configuration and an upstream configuration block

```yaml
- hosts: all
  roles:
    - role: nginx
      nginx_error_log_level: info
      nginx_http_params:
        - sendfile on
        - access_log /var/log/nginx/access.log
      nginx_sites:
        foo:
           - listen 8080
           - server_name localhost
           - root /tmp/site1
           - location / { try_files $uri $uri/ /index.html; }
           - location /images/ { try_files $uri $uri/ /index.html; }
        bar:
           - listen 9090
           - server_name ansible
           - root /tmp/site2
           - if ( $host = example.com ) { rewrite ^(.*)$ http://www.example.com$1 permanent; }
           - location / {
             try_files $uri $uri/ /index.html;
             auth_basic            "Restricted";
             auth_basic_user_file  auth_basic/demo;
           }
           - location /images/ { try_files $uri $uri/ /index.html; }
      nginx_configs:
        proxy:
            - proxy_set_header X-Real-IP  $remote_addr
            - proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for
        upstream:
            # Results in:
            # upstream foo_backend {
            #   server 127.0.0.1:8080 weight=10;
            # }
            - upstream foo_backend { server 127.0.0.1:8080 weight=10; }
      nginx_auth_basic_files:
        demo:
           - foo:$apr1$mEJqnFmy$zioG2q1iDWvRxbHuNepIh0 # foo:demo , generated by : htpasswd -nb foo demo
           - bar:$apr1$H2GihkSo$PwBeV8cVWFFQlnAJtvVCQ. # bar:demo , generated by : htpasswd -nb bar demo
```

7) Install Nginx, add a site and use special yaml syntax to make the location blocks multiline for clarity

```yaml
- hosts: all
  roles:
    - role: nginx
      nginx_http_params:
        - sendfile on
        - access_log /var/log/nginx/access.log
      nginx_sites:
        foo:
           - listen 443 ssl
           - server_name foo.example.com
           - set $myhost foo.example.com
           - |
             location / {
               proxy_set_header Host foo.example.com;
             }
           - |
             location ~ /v2/users/.+?/organizations {
               if ($request_method = PUT) {
                 set $myhost bar.example.com;
               }
               if ($request_method = DELETE) {
                 set $myhost bar.example.com;
               }
               proxy_set_header Host $myhost;
             }
```
8) Example to use this role with my ssl-certs role to generate or copie ssl certificate ( https://galaxy.ansible.com/list#/roles/3115 )
```yaml
 - hosts: all
   roles:
     - jdauphant.ssl-certs
     - role: jdauphant.nginx
       nginx_configs:
          ssl:
               - ssl_certificate_key {{ssl_certs_privkey_path}}
               - ssl_certificate     {{ssl_certs_cert_path}}
       nginx_sites:
          default:
               - listen 443 ssl
               - server_name _
               - root "/usr/share/nginx/html"
               - index index.html
```
9) Site configuration using a custom template.
Instead of defining a site config file using a list of attributes,
you may use a hash/dictionary that includes the filename of an alternate template.
Additional values are accessible within the template via the `item.value` variable.
```yaml
- hosts: all

  roles:
  - role: nginx
    nginx_sites:
      custom_bar:
        template: custom_bar.conf.j2
        server_name: custom_bar.example.com
```
Custom template: custom_bar.conf.j2:
```handlebars
# {{ ansible_managed }}
upstream backend {
  server 10.0.0.101;
}
server {
  server_name {{ item.value.server_name }};
  location / {
    proxy_pass http://backend;
  }
}
```
Using a custom template allows for unlimited flexibility in configuring the site config file.
This example demonstrates the common practice of configuring a site server block
in the same file as its complementary upstream block.
If you use this option:
* _The hash **must** include a `template:` value, or the configuration task will fail._
* _This role cannot check tha validity of your custom template.
If you use this method, the conf file formatting provided by this role is unavailable,
and it is up to you to provide a template with valid content and formatting for NGINX._

# Support
support@dynamictivity.com

License
-------
You are free to use the code in this repository under the terms of the MIT license. LICENSE contains a copy of this license.

Author Information
------------------
Travis Rowland
