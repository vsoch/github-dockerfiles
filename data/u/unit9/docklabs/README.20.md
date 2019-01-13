# Collectd daemon

This image installs [`collectd`](https://collectd.org/). Collectd is compiled
from source and installed to `/opt` by default. Only two plugins are
configured during compilation: snmp and rrd.

No configuration provided for collectd in this image. You need to create
your own config file and place it into `/opt/collectd/etc/collectd.conf`. Here's
an example of one:

```
LoadPlugin snmp
<Plugin snmp>
    <Data "ifmib_if_octets64">
      Type "if_octets"
      Table true
      Instance "IF-MIB::ifName"
      Values "IF-MIB::ifHCInOctets" "IF-MIB::ifHCOutOctets"
    </Data>
    <Data "ifmib_if_packets64">
      Type "if_packets"
      Table true
      Instance "IF-MIB::ifName"
      Values "IF-MIB::ifHCInUcastPkts" "IF-MIB::ifHCOutUcastPkts"
    </Data>
    <Host "gateway-router">
      Address "192.168.1.1"
      Version 1
      Community "public"
      Collect "ifmib_if_octets64" "ifmib_if_packets64"
      Interval 120
    </Host>
</Plugin>

LoadPlugin rrdtool
<Plugin rrdtool>
        DataDir "/var/lib/collectd/rrd"
        CreateFilesAsync false
        CacheTimeout 120
        CacheFlush   900
        WritesPerSecond 50
</Plugin>
```

The above configuration collects network traffic data from `gateway-router`
and saves it as RRD database files in `/var/lib/collectd/rrd` directory.
# Collectd frontend

This image installs [`CGP`](https://github.com/pommi/CGP) which is a frontend
for [`collectd`](https://collectd.org/).

A default configuration is used which means that you either need to provide
your own `/var/www/html/conf/config.php` or attach a directory containing
rrd files from the host to `/var/lib/collectd/rrd`.
