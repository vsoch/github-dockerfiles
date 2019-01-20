# etools-partner-reporting-portal

## Container build status
* Polymer: [![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=unicef&repoName=etools-partner-reporting-portal&branch=develop&pipelineName=polymer&accountName=unicef&type=cf-1)]( https://g.codefresh.io/repositories/unicef/etools-partner-reporting-portal/builds?filter=trigger:build;branch:develop;service:58d57dc1d28e8f0100907a76~polymer)

* PostGIS: [![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=unicef&repoName=etools-partner-reporting-portal&branch=develop&pipelineName=db&accountName=unicef&type=cf-1)]( https://g.codefresh.io/repositories/unicef/etools-partner-reporting-portal/builds?filter=trigger:build;branch:develop;service:58d57dc1d28e8f0100907a75~db)

* Django API: [![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=unicef&repoName=etools-partner-reporting-portal&branch=develop&pipelineName=django_api&accountName=unicef&type=cf-1)]( https://g.codefresh.io/repositories/unicef/etools-partner-reporting-portal/builds?filter=trigger:build;branch:develop;service:58d57dc1d28e8f0100907a74~django_api)

* Nginx proxy: [![Codefresh build status]( https://g.codefresh.io/api/badges/build?repoOwner=unicef&repoName=etools-partner-reporting-portal&branch=develop&pipelineName=proxy&accountName=unicef&type=cf-1)]( https://g.codefresh.io/repositories/unicef/etools-partner-reporting-portal/builds?filter=trigger:build;branch:develop;service:58d57dc1fa94a00100a3096c~proxy)

## macOS Setup
1. Install Docker for Mac. Also install Fabric via `pip install fabric==1.13.1`
2. Create .env file in repository root with the reference of `.env.example` or receive .env file from your team member.
3. Run `fab up` !
4. Go to http://127.0.0.1:8082/ to see the frontend / polymer running. The Django app is running under http://127.0.0.1:8082/api/
5. As a separate terminal tab, run `fab fixtures` if this is first time running environment - load Site & ReportingEntity objects from fixture json files.
6. As a separate terminal tab, run `fab fake_data` to generate fake data like account, core, partner and other modules. There is also `fab real_data` command as well.
7. TEMP: Go to http://127.0.0.1:8082/api/admin/ login with admin/Passw0rd! and can now go to http://127.0.0.1:8082/app/ to see the frontend interface. Replace 'ip-reporting' or 'cluster-reporting' in the URL's to switch between the two interfaces.

## Ubuntu 16.04 setup
1. Install docker and docker-compose
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update -y
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo systemctl status docker
```

2. Set ubuntu user to docker group
```
sudo usermod -aG docker ${USER}

# (Password will be prompt)
su - ${USER}
```

3. Install pip and fabric 1.X
```
sudo apt-get install --assume-yes --reinstall ca-certificates
sudo apt-get install -y --no-install-recommends build-essential vim python-dev python-setuptools

sudo easy_install pip

sudo pip install --upgrade pip --trusted-host pypi.python.org
sudo pip install fabric==1.13.1 --trusted-host pypi.python.org

sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

4. Check docker-compose is installed
```
docker-compose --version
```

5. Create .env file in repository root with the reference of `.env.example` or receive .env file from your team member.
6. Run `fab up` !
7. Go to http://127.0.0.1:8082/ to see the frontend / polymer running. The Django app is running under http://127.0.0.1:8082/api/
8. As a separate terminal tab, run `fab fixtures` if this is first time running environment - load Site & ReportingEntity objects from fixture json files.
9. As a separate terminal tab, run `fab fake_data` to generate fake data like account, core, partner and other modules. There is also `fab real_data` command as well.
10. TEMP: Go to http://127.0.0.1:8082/api/admin/ login with admin/Passw0rd! and can now go to http://127.0.0.1:8082/app/ to see the frontend interface. Replace 'ip-reporting' or 'cluster-reporting' in the URL's to switch between the two interfaces.

## Development
Here are some docker tips:
   1. display all containers:
   ```
   $ docker-compose ps
   ```
   2. ssh into running django_api container
   ```
   $ fab ssh:django_api
   ```
   3. Stop all containers
   ```
   $ fab stop
   ```
   4. Re-build docker images for containers
   ```
   $ fab rebuild
   ```
