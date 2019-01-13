tinc
====

[tinc][1] is a Virtual Private Network (VPN) daemon that uses tunnelling and
encryption to create a secure private network between hosts on the Internet.

To use this image, you need to have basic knowledges of tinc. (See this [tutor][2])

## Directory Tree

```
~/fig/tinc/
├── docker-compose.yml
└── tinc/
    └── netname/
        ├── hosts/
        │   ├── client
        │   ├── client-down*
        │   ├── client-up*
        │   └── server
        ├── rsa_key.priv
        ├── tinc.conf
        ├── tinc-down*
        └── tinc-up*
```

## docker-compose.yml

```yaml
tinc:
  image: vimagick/tinc
  ports:
    - "655:655/tcp"
    - "655:655/udp"
  volumes:
    - ./tinc:/etc/tinc
  environment:
    - IP_ADDR=1.2.3.4
  cap_add:
    - NET_ADMIN
  dns: 8.8.8.8
  restart: always
```

## Server Setup

```bash
# run
$ docker-compose up -d

# monitor
$ docker-compose logs

# stats
$ watch docker-compose exec tinc netstat -an
```

## Client Setup

```bash
# start
$ tincd -d -D -n netname --pidfile /tmp/tinc.pid

# stop
$ tincd -k --pidfile /tmp/tinc.pid
```

## Client Setup (openwrt)

```bash
$ opkg install tinc ip
 
$ cat > /etc/config/tinc
config tinc-net netname
    option enabled 1
config tinc-host linkit
    option enabled 1
    option net netname
config tinc-host server
    option enabled 1
    option net netname
 
$ mkdir -p /etc/tinc/netname/hosts
 
$ cat > /etc/tinc/netname/tinc.conf
Name = linkit
Interface = tun0
ConnectTo = server
 
$ cat > /etc/tinc/netname/hosts/linkit
Subnet = 10.0.0.125
 
$ tincd -n netname -K < /dev/null
Generating 2048 bits keys:
......+++ p
.....+++ q
Done.
 
$ cat > /etc/tinc/netname/tinc-up
#!/bin/sh
ip link set $INTERFACE up
ip addr add  10.0.0.125/24 dev $INTERFACE
 
$ cat > /etc/tinc/netname/tinc-down
#!/bin/sh
ip addr del 10.0.0.125/24 dev $INTERFACE
ip link set $INTERFACE down
 
$ cat > /etc/tinc/netname/hosts/server-up
#!/bin/sh
ORIGINAL_GATEWAY=`ip route show | grep ^default | cut -d ' ' -f 2-3`
ip route add $REMOTEADDRESS $ORIGINAL_GATEWAY
ip route add 0.0.0.0/1 dev $INTERFACE
ip route add 128.0.0.0/1 dev $INTERFACE
 
$ cat > /etc/tinc/netname/hosts/server-down
#!/bin/sh
ORIGINAL_GATEWAY=`ip route show | grep ^default | cut -d ' ' -f 2-3`
ip route del $REMOTEADDRESS $ORIGINAL_GATEWAY
ip route del 0.0.0.0/1 dev $INTERFACE
ip route del 128.0.0.0/1 dev $INTERFACE
 
$ chmod +x /etc/tinc/netname/tinc-*
$ chmod +x /etc/tinc/netname/hosts/server-*
 
$ scp /etc/tinc/netname/hosts/linkit root@remote-server:/etc/tinc/netname/hosts/
$ scp root@remote-server:/etc/tinc/netname/hosts/server /etc/tinc/netname/hosts/
 
$ /etc/init.d/tinc start
$ /etc/init.d/tinc enable
 
$ ifconfig tun0
 
$ firefox http://192.168.1.125/cgi-bin/luci/
 
# Firewall:
# | lan => wan, vpn | ooo | xx |
# | wan =>          | oox | oo |
# | vpn => wan      | ooo | ox |
```

[1]: http://tinc-vpn.org/
[2]: https://www.digitalocean.com/community/tutorials/how-to-install-tinc-and-set-up-a-basic-vpn-on-ubuntu-14-04
tinc-client
===========

```
[root@alarmpi ~]# mkdir -p /etc/tinc/netname/hosts

[root@alarmpi ~]# cat > /etc/tinc/netname/tinc.conf
Name = alarmpi
Interface = tun0
ConnectTo = server

[root@alarmpi ~]# cat > /etc/tinc/netname/hosts/alarmpi
Subnet = 10.0.0.2

[root@alarmpi ~]# tincd -n netname -K
Generating 2048 bits keys:
.................................................+++ p
.................................................+++ q
Done.
Please enter a file to save private RSA key to [/etc/tinc/netname/rsa_key.priv]:
Please enter a file to save public RSA key to [/etc/tinc/netname/hosts/alarmpi]:

[root@alarmpi ~]# cat > /etc/tinc/netname/tinc-up
#!/bin/sh
ip link set $INTERFACE up
ip addr add  10.0.0.2/24 dev $INTERFACE

[root@alarmpi ~]# cat > /etc/tinc/netname/tinc-down
#!/bin/sh
ip addr del 10.0.0.2/24 dev $INTERFACE
ip link set $INTERFACE down

[root@alarmpi ~]# cat > /etc/tinc/netname/hosts/server-up
#!/bin/sh
ORIGINAL_GATEWAY=`ip route show | grep ^default | cut -d ' ' -f 2-3`
ip route add $REMOTEADDRESS $ORIGINAL_GATEWAY
ip route add 0.0.0.0/1 dev $INTERFACE
ip route add 128.0.0.0/1 dev $INTERFACE

[root@alarmpi ~]# cat > /etc/tinc/netname/hosts/server-down
#!/bin/sh
ORIGINAL_GATEWAY=`ip route show | grep ^default | cut -d ' ' -f 2-3`
ip route del $REMOTEADDRESS $ORIGINAL_GATEWAY
ip route del 0.0.0.0/1 dev $INTERFACE
ip route del 128.0.0.0/1 dev $INTERFACE

[root@alarmpi ~]# chmod +x /etc/tinc/netname/tinc-{up,down}
[root@alarmpi ~]# chmod +x /etc/tinc/netname/hosts/server-{up,down}

[root@alarmpi ~]# scp /etc/tinc/netname/hosts/alarmpi root@remote-server:/etc/tinc/netname/hosts/
[root@alarmpi ~]# scp root@remote-server:/etc/tinc/netname/hosts/server /etc/tinc/netname/hosts/

[root@alarmpi ~]# tree -AF /etc/tinc/
/etc/tinc/
└── netname/
    ├── hosts/
    │   ├── alarmpi
    │   ├── server
    │   ├── server-down
    │   └── server-up
    ├── rsa_key.priv
    ├── tinc-down*
    ├── tinc-up*
    └── tinc.conf

[root@alarmpi ~]# cat > /etc/systemd/network/eth0.network
[Match]
Name=eth0

[Network]
DHCP=yes
UseDNS=false
DNS=8.8.8.8
IPMasquerade=yes

[root@alarmpi ~]# cat > /etc/sysctl.d/99-sysctl.conf
net.ipv4.ip_forward=1
net.ipv6.conf.all.disable_ipv6=1
[root@alarmpi ~]# systemctl restart systemd-sysctl

[root@alarmpi ~]# iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -j MASQUERADE
[root@alarmpi ~]# iptables-save > /etc/iptables/iptables.rules
[root@alarmpi ~]# systemctl enable iptables

[root@alarmpi ~]# systemctl start tincd@netname
[root@alarmpi ~]# systemctl status tincd@netname
[root@alarmpi ~]# systemctl enable tincd@netname
```
