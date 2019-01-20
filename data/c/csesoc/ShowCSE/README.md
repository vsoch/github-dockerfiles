# ShowCSE
## Developing

```
(you) $ vagrant up
(you) $ vagrant ssh
(vagrant@debian) $ cd /deploy/com.csesoc.showcse
(vagrant@debian) $ source .env
# Now you're in the venv
(vagrant@debian) $ python run.py server --host 0.0.0.0
```

##### Upgrading the virtual environment with new requirements
```
(vagrant@debian) $ source .env
(vagrant@debian) $ upgrade
```

##### Re-Provision the VM
```
(you) $ vagrant destroy 
(you) $ vagrant up
```

##### Connecting UNSW LDAP
```
ssh you@cse.unsw.edu.au -L 1389:ad.unsw.edu.au:1389
```

## Deploying
Deploy using docker.

These instructions assume you've got the Makefile which is at the top 
level of this repository. It is not required, however may save you some
time copying out commands.


### Initial Creation
**Configure Environment Variables**

Create an env.sh file, which we will use when creating our docker containers to ensure the expected environment is passed to each container. Save this file as `env.sh`, unless you wish to modify subsequent commands that use it. We've included an example one: `env.example.sh`

```
MYSQL_DATABASE=showcse
MYSQL_USER=showcse

# MySQL Password is required.
MYSQL_PASSWORD=

# Secret key used for signing cookies and CSRF tokens
SECRET_KEY=

# Ship exceptions to a sentry logging instance if provided (optional)
SENTRY_DSN=

# Determine what configuration setting should be used for the app
CONFIG_CLASS=Production
```

**Setup the Containers and Links**

```
make create
```

** Initially Seed the Database **
```
make seed
```

**Start ShowCSE**
```
make start
```

### Run at Startup with systemd
Copy or Clone this repo to acquire the service files. See folder `./systemd/` which contains systemd services.

**Stop existing containers**
```
make stop
```

**Enable/Install the Services**

```
# Enable the Services
systemctl enable systemd/showcse.mysql.service
systemctl enable systemd/showcse.service

# Start the service. 
systemctl start showcse
```

## Building the Docker Image
```
make build
```

## Push Docker Image To Cloud

make push



