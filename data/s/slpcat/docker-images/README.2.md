Bootstrap config, for a container started without an existing ldap config.
Add your custom ldif files here if you don't want to overwrite image default boostrap ldif.
at run time you can also mount a data volume with your ldif files to /container/service/slapd/assets/config/bootstrap/ldif/custom

The startup script provides some substitutions in bootstrap ldif files. Following substitutions are supported:

- `{{ LDAP_BASE_DN }}`
- `{{ LDAP_BACKEND }}`
- `{{ LDAP_READONLY_USER_USERNAME }}`
- `{{ LDAP_READONLY_USER_PASSWORD_ENCRYPTED }}`

Other `{{ * }}` substitutions are left unchanged.

Since startup script modifies `ldif` files,
you **must** add `--copy-service` argument to entrypoint if you don't want to overwrite them.
Bootstrap schemas, for a container started without an existing ldap config.
Mandriva Management Console (MMC) ldap schemas, delete the forlder if not needed ;)Add your tls server certificate, key and the CA certificate (if any) here
or during docker run mount a data volume with those files to /container/service/slapd/assets/certs
