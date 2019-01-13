
For historical reasons, I wanted a Docker image based on CentOS 6...

Alternate ways to modernize the old CentOS6 YUM repos... 

* http://sharadchhetri.com/2014/05/30/install-pip-centos-rhel-ubuntu-debian/
    * installs only 6 RPMs --but you are stuck with old Python 2.6
* https://github.com/h2oai/h2o-2/wiki/installing-python-2.7-on-centos-6.3.-follow-this-sequence-exactly-for-centos-machine-only
    * installs 30 RPMs (121 MB) --but you get Python 2.7

```
~/docker/sandbox/from-centos6-py2 $ docker images | head -n2
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
markhu/c6-py2       latest              867e50451864        8 minutes ago       329.6 MB

~/docker/sandbox/from-centos6-py2 $ docker run -i -p 8000:8000 -t markhu/c6-py2 pip list

distribute (0.6.10)
iniparse (0.3.1)
ordereddict (1.2)
pip (7.1.0)
pycurl (7.19.0)
pygpgme (0.1)
requests (2.11.1)
setuptools (0.6rc11)
urlgrabber (3.9.1)
yum-metadata-parser (1.1.2)

~/docker/sandbox/from-centos6-py2 $ docker run -i -p 8000:8000 -t markhu/c6-py2 rpm -qa --last | head

mlocate-0.22.2-6.el6.x86_64                   Fri Oct 28 23:49:13 2016
python-pip-7.1.0-1.el6.noarch                 Fri Oct 28 23:48:32 2016
python-setuptools-0.6.10-3.el6.noarch         Fri Oct 28 23:48:28 2016
gpg-pubkey-c105b9de-4e0fd3a3                  Fri Oct 28 23:48:25 2016
gpg-pubkey-0608b895-4bd22942                  Fri Oct 28 23:48:25 2016
epel-release-6-8.noarch                       Fri Oct 28 23:43:18 2016
vim-minimal-7.4.629-5.el6.x86_64              Wed Aug 19 18:26:25 2015
rootfiles-8.1-6.1.el6.noarch                  Wed Aug 19 18:26:25 2015
bind-utils-9.8.2-0.37.rc1.el6.x86_64          Wed Aug 19 18:26:25 2015
centos-release-6-7.el6.centos.12.3.x86_64     Wed Aug 19 18:26:06 2015
19:58:41 ~/docker/sandbox/from-centos6-py2 $ 
```
