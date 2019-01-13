tor
===

![](https://badge.imagelayers.io/vimagick/tor:latest.svg)

[`Tor`][1] is free software and an open network that helps you defend against
traffic analysis, a form of network surveillance that threatens personal
freedom and privacy, confidential business activities and relationships, and
state security.

- Tor prevents people from learning your location or browsing habits.
- Tor is for web browsers, instant messaging clients, and more.
- Tor is free and open source for Windows, Mac, Linux/Unix, and Android

ServerTransportPlugin:

- [x] fte
- [x] meek
- [x] obfs3
- [x] obfs4

## docker-compose.yml

```
tor:
  image: vimagick/tor
  ports:
#   - "7002:7002"
    - "9001:9001"
# volumes:
#   - ./torrc:/etc/tor/torrc
#   - ./cert.pem:/var/lib/tor/cert.pem
#   - ./key.pem:/var/lib/tor/key.pem
  restart: always
```

> Default `torrc` is for `obfs4`.
> Uncomment lines to use `meek`.

## torrc (server)

```
BridgeRelay 1
ContactInfo noreply@easypi.info
DataDirectory /var/lib/tor
Exitpolicy reject *:*
Nickname easypi
ORPort 9001
PublishServerDescriptor 0
SocksPort 0
#ServerTransportPlugin fte exec /usr/bin/fteproxy --mode server --managed
#ServerTransportPlugin meek exec /usr/bin/meek-server --port 7002 --cert cert.pem --key key.pem
#ServerTransportPlugin obfs3 exec /usr/bin/obfsproxy managed
ServerTransportPlugin obfs4 exec /usr/bin/obfs4proxy
```

## torrc (client)

```
#Socks5Proxy 127.0.0.1:1080
UseBridges 1
#Bridge fte 1.2.3.4:9001 F24BF4DE74649E205A8A3621C84F97FF623B2083
#Bridge meek 1.2.3.4:9001 url=https://meek.easypi.info:7002/
#Bridge obfs3 1.2.3.4:9001 F24BF4DE74649E205A8A3621C84F97FF623B2083
Bridge obfs4 1.2.3.4:9001 F24BF4DE74649E205A8A3621C84F97FF623B2083
#ClientTransportPlugin fte exec /usr/local/bin/fteproxy
#ClientTransportPlugin meek exec /usr/local/bin/meek-client
#ClientTransportPlugin obfs3 exec /usr/local/bin/obfsproxy
ClientTransportPlugin obfs4 exec /usr/local/bin/obfs4proxy
```

> Please connect via `HTTPProxy`/`HTTPSProxy`/`Socks5Proxy` if you're blocked!

## server

```
$ openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/C=JP/ST=Tokyo/L=Heiwajima/O=DataGeek/OU=Org/CN=meek.easypi.info"
$ docker-compose up -d
$ docker-compose logs
$ docker-compose exec tor tor --quiet --list-fingerprint
easypi F24B F4DE 7464 9E20 5A8A 3621 C84F 97FF 623B 2083
```

## client

```
$ tor -f /etc/tor/torrc
$ curl -x socks5h://127.0.0.1:9050 ifconfig.ovh
```

## references

- https://www.torproject.org/projects/obfsproxy-debian-instructions.html.en
- https://blog.torproject.org/blog/how-use-%E2%80%9Cmeek%E2%80%9D-pluggable-transport
- https://fteproxy.org/help-server-with-tor
- https://github.com/Yawning/obfs4

[1]: https://www.torproject.org/
Tor on OpenWrt
==============

![](https://trac.torproject.org/images/tor-logo.png)

## Install Tor

```bash
$ opkg update
$ opkg install tor

$ vi /etc/tor/torrc
$ vi /etc/config/dhcp
$ vi /etc/firewall.user

$ /etc/init.d/tor restart
$ /etc/init.d/dnsmasq restart
$ /etc/init.d/firewall restart
```

## Config Tor

```
# /etc/tor/torrc

RunAsDaemon 0  
DataDirectory /var/lib/tor  
User tor  
#Socks5Proxy 127.0.0.1:1080
SocksPort 0.0.0.0:9050  
TransPort 0.0.0.0:9040  
DNSPort 0.0.0.0:9053  
AvoidDiskWrites 1 
```

## Socks5 Proxy (optional)

You may need to connect tor network via `Socks5Proxy`.
You can use [ss-local][1] to setup a local socks5 proxy.

```bash
$ wget https://github.com/vimagick/rpi-bin/raw/master/ipk/shadowsocks-libev_2.4.8-3_arm_cortex-a53_neon-vfpv4.ipk
$ opkg install shadowsocks-libev_2.4.8-3_arm_cortex-a53_neon-vfpv4.ipk
$ vi /etc/shadowsocks.json
$ vi /etc/rc.local
$ sh /etc/rc.local
```

```bash
# /etc/rc.local

ss-local -c /etc/shadowsocks.json -f /var/run/ss-local.pid

exit 0
```

```json
{
    "server": "1.2.3.4",
    "server_port": 8388,
    "local_address": "127.0.0.1",
    "local_port": 1080,
    "password": "******",
    "timeout": 60,
    "method": "chacha20",
    "auth": true
}
```

## Config DNS

You can config DNS via Luci.

```bash
# /etc/config/dhcp

config dnsmasq
       option noresolv '1'
       list server '127.0.0.1#9053'
```

## Config Firewall

```bash
# /etc/firewall.user

iptables -t nat -X TOR
iptables -t nat -N TOR
iptables -t nat -A TOR -d 0.0.0.0/8 -j RETURN
iptables -t nat -A TOR -d 10.0.0.0/8 -j RETURN
iptables -t nat -A TOR -d 127.0.0.0/8 -j RETURN
iptables -t nat -A TOR -d 169.254.0.0/16 -j RETURN
iptables -t nat -A TOR -d 172.16.0.0/12 -j RETURN
iptables -t nat -A TOR -d 192.168.0.0/16 -j RETURN
iptables -t nat -A TOR -d 224.0.0.0/4 -j RETURN
iptables -t nat -A TOR -d 240.0.0.0/4 -j RETURN
iptables -t nat -A TOR -p udp --dport 53 -j REDIRECT --to-ports 9053
iptables -t nat -A TOR -p tcp --syn -j REDIRECT --to-ports 9040
iptables -t nat -A PREROUTING -i br-lan -j TOR
```

## Debug Tor

```bash
$ /etc/init.d/tor stop
$ tor
Aug 16 11:49:43.222 [notice] Tor v0.2.7.6 running on Linux with Libevent 2.0.22-stable, OpenSSL 1.0.2h and Zlib 1.2.8.  
Aug 16 11:49:43.223 [notice] Tor can't help you if you use it wrong! Learn how to be safe at https://www.torproject.org/download/download#warning  
Aug 16 11:49:43.223 [notice] Read configuration file "/etc/tor/torrc".  
Aug 16 11:49:43.246 [warn] You specified a public address '0.0.0.0:9050' for SocksPort. Other people on the Internet might find your computer and use it as an open proxy. Please don't allow this unless you have a good reason.  
Aug 16 11:49:43.246 [warn] You specified a public address '0.0.0.0:9053' for DNSPort. Other people on the Internet might find your computer and use it as an open proxy. Please don't allow this unless you have a good reason.  
Aug 16 11:49:43.246 [warn] You specified a public address '0.0.0.0:9040' for TransPort. Other people on the Internet might find your computer and use it as an open proxy. Please don't allow this unless you have a good reason.  
Aug 16 11:49:43.251 [notice] Opening Socks listener on 0.0.0.0:9050  
Aug 16 11:49:43.251 [notice] Opening DNS listener on 0.0.0.0:9053  
Aug 16 11:49:43.251 [notice] Opening Transparent pf/netfilter listener on 0.0.0.0:9040  
Aug 16 11:49:44.000 [notice] Bootstrapped 0%: Starting  
Aug 16 11:49:46.000 [notice] Bootstrapped 5%: Connecting to directory server  
Aug 16 11:49:46.000 [notice] Bootstrapped 80%: Connecting to the Tor network  
Aug 16 11:49:46.000 [notice] Bootstrapped 85%: Finishing handshake with first hop  
Aug 16 11:49:53.000 [notice] Bootstrapped 90%: Establishing a Tor circuit  
Aug 16 11:49:58.000 [notice] Tor has successfully opened a circuit. Looks like client functionality is working.  
Aug 16 11:49:58.000 [notice] Bootstrapped 100%: Done  
^C
$ /etc/init.d/tor start
```

[1]: https://github.com/vimagick/rpi-bin/raw/master/ipk/shadowsocks-libev_2.4.8-3_arm_cortex-a53_neon-vfpv4.ipk
