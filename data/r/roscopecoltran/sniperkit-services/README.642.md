# SSL/TLS

Before you run this script you must ensure that the rta-security/certs 
directory contains a dcp_rta_ca.crt, dcp_rta_pk.pem and truststore.jks 

This script will create a new dcp self-signed certificate for our datastorage
nodes. Right now these certificates cannot be hostname verified i.e. we 
use the same secure cert for each node in the datastorage cluster as 
we do not have a DNS in JEDI this means we cannot trust the hostname
expect this to be fixed in the next release.

This script will run and will create an output directory called 
dcp_rta_datastorage_out. Copy the truststore and keystore java keystore 
files to the certs directory. The keystore is a password protected 
store of our public and private keys for the datastorage nodes and 
check them into git.

    > sh create_dcp_rta_datastorage_credentials.sh
    > cp dcp_rta_datastorage_out/*.jks dcp_rta_datastorage_out/*.p12 certs/
    > git add and commit

The .p12 file can be used to load into as a browser cert or with curl requests if
you want to contact the now secure elasticsearch database.

Useful info: if firefox does not like your certificate and says 
'Your certificate contains the same serial number as another certificate issued by the certificate authority' 

    > cd ~/.mozilla/firefox/{profile-name}.default
    > rm cert8.db    --OR-- $ mv cert8.db cert8.db.bak
    > Restart Firefox

# Elasticsearch performance

Also for good performance, one must do the following on the host:
$ sudo sysctl -w vm.max_map_count=262144
$ sudo echo 'vm.max_map_count=262144' >> /etc/sysctl.conf

See https://www.elastic.co/guide/en/elasticsearch/reference/2.1/setup-configuration.html, elasticsearch uses a hybrid mmapfs / niofs directory by default to store its indices. The default operating system limits on mmap counts is likely to be too low, which may result in out of memory exceptions.

# Access

Default users are: 
- elastic: A superuser
- kibana: The user Kibana uses to connect and communicate with Elasticsearch.

Password is: changeme.
Before you run this script you must ensure that the rta-security/certs 
directory contains a dcp_rta_ca.crt, dcp_rta_pk.pem and truststore.jks 

This script will create a new dcp self-signed certificate for our datastorage
nodes. Right now these certificates cannot be hostname verified i.e. we 
use the same secure cert for each node in the datastorage cluster as 
we do not have a DNS in JEDI this means we cannot trust the hostname
expect this to be fixed in the next release.

This script will run and will create an output directory called 
dcp_rta_datastorage_out. Copy the truststore and keystore java keystore 
files to the certs directory. The keystore is a password protected 
store of our public and private keys for the datastorage nodes and 
check them into git.

    > sh create_node_certificates.sh.sh
    > cp out/*.jks out/*.p12 .
    > git add and commit

The .p12 file can be used to load into as a browser cert or with curl requests if
you want to contact the now secure elasticsearch database.

Useful info: if firefox does not like your certificate and says 
'Your certificate contains the same serial number as another certificate issued by the certificate authority' 

    > cd ~/.mozilla/firefox/{profile-name}.default
    > rm cert8.db    --OR-- $ mv cert8.db cert8.db.bak
    > Restart Firefox


    

