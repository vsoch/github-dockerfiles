## Adding your SSL custom certificate

Set the environment variable in `~/.docker-compose-plugins-xml.env`:

    export SSL_CUSTOM_CERT=1

Place your server's certificate chain and private key in your HOME directory, then
name them exactly (note dot at beginning):

- `.qgisrepo-server.crt`
- `.qgisrepo-server.key`

Note: the `.crt` file should contain, in the following order:

1. Server's primary certificate
2. Primary certificate's issuer certificate (i.e. intermediate authority)
3. Optionally any other issuer's certificate, up the chain (parents towards
   bottom of file), but not including root authority

See: <http://nginx.org/en/docs/http/configuring_https_servers.html#chains>
