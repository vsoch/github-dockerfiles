DNSizer
=======
A small program which emulates a DNS server. It serves a single top-level domain to a single IP address

Use Case
-------
In your development setup we have all your services running via Vagrant on VirtalBox. We want to redirect all the requests to *.dev to the vagrant machine.
On our Mac's we create the file `/etc/resolver/dev` with the contents

```
nameserver 33.33.33.10
port 53
```

When we start the binary on our machine with `dnsizer -addr=:53 -domain=dev -ip=33.33.33.10` all the requests to *.dev will be served by 33.33.33.10, without manually adjusting our hostfile.

Installation
------------
1. Install Go
2. `go get github.com/moneybird/dnsizer`
3. `go install github.com/moneybird/dnsizer`
