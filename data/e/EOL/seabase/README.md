SeaBase
=======

SeaBase is a tool for searching, analysing and sharing gene expression
data of marine organisms.

[![Continuous Integration Status][1]][2]
[![Coverage Status][3]][4]
[![CodePolice][5]][6]
[![Dependency Status][7]][8]


Install
-------

General requirements:

  - Ruby version 2.3
  - MySQL server version 5.7
  - Web Server for production (Nginx, or Apache)

### required packatges on Ubuntu:

    sudo apt-get update
    sudo apt-get install mysql-server csh libqt4-dev

Running in production with docker-compose
-----------------------------------------

Get source code and switch to production branch

```bash
git clone https://github.com/GlobalNamesArchitecture/gnrd.git
cd gnrd
git checkout production
```

Create directories for database and configuration files

```bash
sudo mkdir -p /opt/seabase/data/mysql
sudo chown 999:999 -R /opt/seabase/data/mysql
sudo cp ./config/seabase-dev.env ./config/seabase-production.env
```

Modify `seabase-production.env` to suit your needs.
Run compose in daemon mode from the project's root directory

```bash
nohup docker-compose up -d
```

Running Tests
-------------

Javascript tests use capybara-webkit, which requires installation of
QT Webkit library, you can find installations instruction on
[capybara-webkit wiki][9]

    bundle exec rake db:migrate SEABASE_ENV=test
    bundle exec rake db:seed SEABASE_ENV=test
    bundle exec rake

Also look at [.travis.yml][10] file for more information

### Running Tests With Docker Compose

Docker and Docker Compose need to be installed on the host machine

```.bash
sudo rm -rf .sass-cache
docker-compose build
docker-compose up -d
docker-compose run app db:reset
docker-compose run app db:seed SEABASE_ENV=test
docker exec -it seabase_app_1 rake
```

For some reason ``docker-compose run app rake`` does not work for webkit-based
tests.

Copyright
---------

Code: [Nathan Wilson][11],[Dmitry Mozzherin][12]

Copyright (c) 2014 [Marine Biological Laboratory][13]. See [LICENSE][14] for
further details.

[1]: https://secure.travis-ci.org/EOL/seabase.png
[2]: http://travis-ci.org/EOL/seabase
[3]: https://coveralls.io/repos/EOL/seabase/badge.png?branch=master
[4]: https://coveralls.io/r/EOL/seabase?branch=master
[5]: https://codeclimate.com/github/EOL/seabase.png
[6]: https://codeclimate.com/github/EOL/seabase
[7]: https://gemnasium.com/EOL/seabase.png
[8]: https://gemnasium.com/EOL/seabase
[9]: http://goo.gl/BNFBZM
[10]: https://github.com/EOL/seabase/blob/master/.travis.yml
[11]: https://github.com/nwilson-EOL
[12]: https://github.com/dimus
[13]: http://mbl.edu
[14]: https://github.com/EOL/seabase/blob/master/LICENSE
