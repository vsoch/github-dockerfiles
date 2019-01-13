pptpd
=====

![](https://badge.imagelayers.io/vimagick/pptpd:latest.svg)

The Point-to-Point Tunneling Protocol is a method for implementing virtual private networks.

`PPTP` uses a control channel over TCP and a GRE tunnel operating to encapsulate PPP packets.

## Directory Tree

```
~/fig/pptpd/
├── docker-compose.yml
├── pptpd.conf
├── pptpd-options
└── chap-secrets
```

file: docker-compose.yml

```yaml
pptpd:
  image: vimagick/pptpd
  volumes:
    - ./pptpd.conf:/etc/pptpd.conf
    - ./pptpd-options:/etc/ppp/pptpd-options
    - ./chap-secrets:/etc/ppp/chap-secrets
  privileged: true
  restart: always
```

file: pptpd.conf

```
option /etc/ppp/pptpd-options
pidfile /var/run/pptpd.pid
localip 192.168.127.1
remoteip 192.168.127.100-199
```

file: pptpd-options

```
name pptpd
refuse-pap
refuse-chap
refuse-mschap
require-mschap-v2
require-mppe-128
proxyarp
nodefaultroute
lock
nobsdcomp
novj
novjccomp
nologfd
ms-dns 8.8.8.8
ms-dns 8.8.4.4
```

file: chap-secrets

```
# Secrets for authentication using CHAP
# client    server  secret          IP addresses

username    *       password        *
```

> Please use strong password in `chap-secrets` file to protect your server.

## Server Setup

```bash
$ modprobe nf_conntrack_pptp nf_nat_pptp
$ cd ~/fig/pptpd/
$ docker-compose up -d
$ docker-compose logs -f
```

You need to config firewall:

- To let PPTP tunnel maintenance traffic, `allow port 1723/tcp`.
- To let PPTP tunneled data to pass through router, `allow proto gre`.
- Set `DEFAULT_FORWARD_POLICY=ACCEPT`
- Set `net.ipv4.ip_forward=1` (sysctl)

## Client Setup

Connect PPTP server using `username:password` with `mschap-v2/mppe-128` encyption.

## References

- <https://wiki.archlinux.org/index.php/PPTP_server>
- <https://wiki.archlinux.org/index.php/PPTP_Client>
pptp
====

Containerized PPTP Client

## docker-compose.yml

```yaml
pptp:
  image: vimagick/pptp
  environment:
    - SERVER=1.2.3.4
    - TUNNEL=vps
    - USERNAME=username
    - PASSWORD=password
  net: host
  privileged: yes
  restart: unless-stopped
```

## up and running

```
sudo modprobe nf_conntrack_pptp nf_conntrack_proto_gre

docker-compose up -d
docker-compose logs -f

ip link show
ip addr show
ip route show

curl ifconfig.co
curl ifconfig.ovh
curl ifconfig.me
```

## references

- <http://pptpclient.sourceforge.net/howto-debian.phtml>
- <https://wiki.archlinux.org/index.php/PPTP_Client>
