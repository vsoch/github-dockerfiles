# Digital Ocean Setup

## Dockers

Digital Ocean setup using Dockers and Nginx to run my Blog and my friend's and Ponniyin Selvan Community

The day Dockers [announced the Release Candidate](https://blog.docker.com/2014/05/docker-0-11-release-candidate-for-1-0/) and after reading about the application virutalization I could immediately sense the advantages related to isolating different applications and upgrade them without affecting other applications/components. Started experimenting it on Digital Ocean on May 26th 2014 and never looked back since then.

Some of the advantages I found during my experiments

* I am able to hide application instances to the public internet. For example, mysql is accessible only by the other Docker Containers
* I have a wordpress blog which is bit old due to plugin dependency and doesn't work properly in new PHP 5.4.x, so I had to use both old PHP and PHP 5.4+ at the same time. Docker allows me to create and run both without having to worry about conflicting dependency components and upgrades. I proxy to respective PHP Fast CGI docker instance based on the domain/blog.
* I was able to switch from MySQL to MariaDB silently without even worrying as everything else including the Docker name is same (mysql!) but internally it is running MariaDB.
* Able to run different Linux distributions on top of Ubuntu due to dependency of the component. Without dockers then I would have to provision another Digital Ocean droplet and install that particular OS.
* Able to run multiple instances of the same Docker Image, upgrade and test and make sure the newer version of the application works before switching over to production mode.
* Portable, when I upgraded from Ubuntu 14.04 to Ubuntu 15.10, I ran into some issues on the same Digital Ocean Droplet. I just created a new droplet with 15.10, exported the Docker Image from 14.04 Droplet and imported to the new Droplet. No need to go through all installation procedures again.
* Can create multiple versions of the Image and switch between them.
* Light weight/Less Memory/Cheaper than creating new VPS.

### Dockers Running

![](screenshots/Dockers-Running-Digital-Ocean.png)

### Docker Images

![](screenshots/Docker-Images-Digital-Ocean.png)

### Dockers running At Work

![](screenshots/Docker-Setup-At-Work.png)

### Dockers Images At Work

![](screenshots/Docker-Images-At-Work.png)

## Nginx

When I started setting public websites with Dreamhost on 7th Dec 2006 they offered cheap hosting for $2 a month, it was shared hosting where you don't get to run lot of apps due to memory/cpu restrictions. My websites were served using Apache Web Sever

After my websites started creating some traffic, Dreamhost on 26th Dec 2008 sent a nice email stating that my websites consuming lot of CPU/RAM and better move to private server with some promotion. I took it and started using lighttpd with some Lua scripting for couple of years.

Finally moved to nginx on 26th Jan 2010 and never looked at any other web server since then. Nginx is fast, consumes less memory and able to customize easily than Apache.

When I was doing a POC for work to convert an existing Web application to Hybrid application, I had to use some Lua scripting at the Nginx layer to do Single Sign On. After that I started using Nginx from OpenRestry distribution which allows to have Lua scripting which allows me to do much more than just static configurations.

## Backup and alerts using IFTTT and Pushbullet

Instead of sending/checking email to ensure that my backups are running, when does it start and ends. I am using IFTTT Maker Channel which in turn push the data to Pushbullet and PushBullet App on Android Phone shows Notification that it completed.

I am creating daily Incremental backup with Day Name and Full Monthly backup with Month Name and Weekly back with Week number of the month. This will allow me to control how many backup file I create and don't have to go and remove older backups.

```
curl -X POST -H "Content-Type: application/json" -d '{"value1":"Starte","value2":"test","value3":"test"}' https://maker.ifttt.com/trigger/ubuntu_daily_backup/with/key/b8xEtGuB-9Mrt0sz4Lnu2P
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd /data
sudo tar -czvf backups/$(date '+%A').tar.gz .  --exclude=swap4G.swap --exclude=backups --listed-incremental=backups/data.snar
sudo mv -f backups/$(date '+%A').tar.gz /backups/daily/
curl -X POST -H "Content-Type: application/json" -d '{"value1":"Completed","value2":"test","value3":"test"}' https://maker.ifttt.com/trigger/ubuntu_daily_backup/with/key/b8xEtGuB-9Mrt0sz4Lnu2P
```
![](screenshots/Screenshot_2016-09-07-15-32-14-088.jpeg)

![](screenshots/backup-schedule.png)
