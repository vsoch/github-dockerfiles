# message-test

A Clojure library designed to ... well, that part is up to you.

## Usage

### Drop messages between 2 hosts on a port:

    sudo iptables -R FORWARD 1 -p tcp -s 172.17.1.1 -d 172.17.1.5 --sport 61616 -j DROP


## License

Copyright © 2014 FIXME

Distributed under the Eclipse Public License either version 1.0 or (at
your option) any later version.
