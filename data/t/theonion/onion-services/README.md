# The Onion's Docker Services

This is a set of containers that provide basic services for use in development. The idea here is that we have an "onion", "clickhole", "avclub" container each, and those link to these.

## OSX Setup instructions

1. Install *Docker for Mac*

1. Run ```scripts/serve```

## Docker Tips

1. Setup shell aliases for commonly used docker commands

        alias dc=docker-compose

2. If running in background (via "-d" flag), use `docker-compose logs` to view the running container's logs + console output

3. List all running docker containers

        docker ps

## Vault

To interact with onion-services Vault:

1. Start vault shell:

        $ docker run -e VAULT_ADDR=http://vault:8201 -it --link onionservices_vault_1:vault --entrypoint=/bin/sh sjourdan/vault

1. Authenticate via default root token (created via docker-compose container script)

        $ vault auth 001fdd19-468b-ef28-c256-b46684c0a6fa
        Successfully authenticated!
        token: 001fdd19-468b-ef28-c256-b46684c0a6fa
        token_duration: 0
        token_policies: [root]

1. Write secret

        $ vault write secret/one hello=world
        Success! Data written to: secret/one

1. Read secret

        $ vault read secret/one
        Key             Value
        lease_duration  2592000
        hello           world

