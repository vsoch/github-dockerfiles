Add your ldap client certificate, key and CA certificate here
or during docker run mount a data volume with those files to /container/service/ldap-client/assets/certs
Add your https server certificate, key and the CA certificate (if any) here
or during docker run mount a data volume with those files to /container/service/phpldapadmin/assets/apache2/certs
Add your custom config.php file here or mount one at docker run to /container/service/phpldapadmin/assets/config/config.php
