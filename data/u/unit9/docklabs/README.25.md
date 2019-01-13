# Collectd frontend

This image installs [`CGP`](https://github.com/pommi/CGP) which is a frontend
for [`collectd`](https://collectd.org/).

A default configuration is used which means that you either need to provide
your own `/var/www/html/conf/config.php` or attach a directory containing
rrd files from the host to `/var/lib/collectd/rrd`.
