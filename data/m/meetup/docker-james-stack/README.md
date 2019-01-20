# docker-james-stack

For running james in a dev env - specifically on our devboxes.

### Install james on your Sabayon devbox

```bash
sudo equo install james
sudo chown ${USER}.root -R /usr/local/james/apps/james
cd /usr/local/james/apps/james
/usr/local/java/bin/jar -xf ../james.sar
```

### Make sure docker-compose is installed

https://docs.docker.com/compose/install/
Or use pip to intall it
```bash
sudo pip install docker-compose
```

### Verify docker is runing; if not install it, enable it to survive reboots and start it

```bash
equo install meetup/docker
# add yourself to the docker group
usermod -aG docker ${USER}
systemctl status docker
# enable it to survive reboots
systemctl enable docker
systemctl start docker
```

### Build james locally

```bash
cd /usr/local/meetup
ant james
```

### Start james and postfix containers
- NOTE: the following volumes are bind-mounted into the james container for providing needed james libs.
    volumes:
     - /usr/local/meetup:/code/meetup
     - /usr/local/james:/james_libs

```bash
# clone this repo and cd into it
cd /path/to/docker-james-stack
(use --force-recreate; there are some errors i have to look into when restarting old james containers)
docker-compose up --force-recreate
```

### Map james.int.meetup.com to localhost
Update /etc/hosts with this entry on your devbox to have your app access james locally
```bash
127.0.0.1    james.int.meetup.com
```

### Note
- The postfix container is accessible from the james container via docker links (using mail.int.meetup.com)
- The postfix container is configured to reject sending emails to all other domains except @meetup.com; configured in /etc/postfix/recipient_domains
