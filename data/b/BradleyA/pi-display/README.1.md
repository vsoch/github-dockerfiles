## blinkt
#### WARNING: These instructions are incomplete. Consider them as notes quickly drafted on a napkin rather than proper documentation!
Need to continue to organize the research from the many systems running different test cases.   Organize it into; what works, what I want, and what I still need to make this design work:
    
#### Clone
To clone the entire repository, change to the location you want to download the scripts. Use git to pull or clone these scripts into the directory. If you do not have git then enter; "sudo apt-get install git". On the github page of this script use the "HTTPS clone URL" with the 'git clone' command.

    git clone https://github.com/BradleyA/pi-display
    cd pi-display/blinkt/

#### Install
To install, change to the directory, cd /usr/local/bin, to download the script.

    curl -L https://api.github.com/repos/BradleyA/pi-display/tarball | tar -xzf - --wildcards *blinkt/xxxx ; mv BradleyA-pi-display-*/blinkt/xxxx.sh . ; rm -rf BradleyA-pi-display-*

#### Usage
    xxxx 

#### Output
    $ xxxx
    
#### NOTES:

    crontab -l
        @reboot   /usr/local/bin/larson-1.py >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    * * * * * /usr/local/bin/local-create-message.sh >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    * * * * * sleep 5  ; /usr/local/bin/display-led.py >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    * * * * * sleep 20 ; /usr/local/bin/local-create-message.sh >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    * * * * * sleep 25 ; /usr/local/bin/display-led.py >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    * * * * * sleep 40 ; /usr/local/bin/local-create-message.sh >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    * * * * * sleep 45 ; /usr/local/bin/display-led.py >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    #
    @reboot   /usr/local/bin/plasma-1.py >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    */1 * * * * /usr/local/bin/create-message.sh >> /usr/local/data/us-tx-cluster-1/log/`hostname -f`-crontab 2>&1
    @reboot   sleep 60 && /usr/local/bin/display-message-hd.py Connection to six-rpi3b.cptx86.com closed by remote host.tab 2>&1

#### System OS script tested
 * Ubuntu 14.04.3 LTS
 * Ubuntu 16.04.3 LTS (armv7l)

#### Design Principles
 * Have a simple setup process and a minimal learning curve
 * Be usable as non-root
 * Be easy to install and configure

## License
MIT License

Copyright (c) 2019  Bradley Allen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

