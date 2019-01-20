# Schedule Scripts

simple scripts relating to schedules

## schedule-bootstrap.py

Makes HTTP requests to bootstrap schedules for a range of days for a set of
channels or all the channels on a platform.

e.g.
```
./schedule-bootstrap.py -source pressassociation.com -start 2014-05-05 hkqs
./schedule-bootstrap.py -source pressassociation.com -start 2014-05-05 -end 2014-05-06 hkqs hkrh
./schedule-bootstrap.py -source pressassociation.com -start 2014-05-05 -end 2014-05-06 -platform cbhN
./schedule-bootstrap.py -source pressassociation.com -start 2014-05-05 -end 2014-05-06 -platform cbhN -offset 50
```

The target host can be overridden with the `-host` parameter.

## schedule-compare.py

Fetches schedules from two sources and produces a table comparing them. Output
versions 3 and 4 are supported.

__N.B__ only v3 channel IDs are supported because only a v3 `/channels` resource exists.

Parameters are described with `./schedule-compare.py -h`

Target API servers are controller with the -h1, -p1, -v1 and -h2, -p2, -v2 parameters which set the host, port and API version of the comparison requests respectively.

An entire platform can be compared through the -platform parameter.

If more than one channel-day is compared then rather than printing the comparison table only a comparison count is printed for each channel-day. If there are differences then a script call is output for that specific channel-day.

e.g.
```
./schedule-compare.py -h2 stage.atlas.metabroadcast.com -v2 4 -k <key> pressassociation.com 2014-05-05 2014-05-06 cbbh cbbj 
./schedule-compare.py -h2 app2.prod.deer.atlas.mbst.tv -p2 8080 -k <key> -platform cbhN pressassociation.com 2014-05-13 2014-05-20
```
