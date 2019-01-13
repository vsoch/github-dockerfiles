
Ansible provides a framework for our administration and deployment. It requires an organization for scripts and variables.  By design it uses SSH to connect to all hosts before it executes the actions. As such it can be run from any machine. All Ansible provided functionality is idempotent and it strongly encourage custom scripts match that standard.

Here is the organization of the files in `devops-scripts/ansible`

* `*-hosts` - Files naming all the servers
* `*.yml` - The top level ansible actions.  These files describe how a host has vars and roles executed on it. 
* `/group_vars` - yml files that define variables and values for your ansible scripts. This mostly maps one to one with machine types in AWS. They’re a key value map. 
* `/library` - Third party libraries and scripts. 
* `/roles` - A set of folders containing the ansible roles. A role defines the executable actions by ansible.  The center pieces is the `/tasks/main.yml`. It defines name actions and requirements. 
The role can have several sub folders.
  * `/handlers` - ??? 
  * `/defaults` - ???
  * `/meta` - contains dependencies
  * `/template` - templates for any files that need to be generate and delivered. 
must add pem files before building
Role Name
========

Ansible Role to Install base_centos deps

Author Information
------------------

# anandkumarpatel
###         #
Role Name
========

Ansible Role to Install Docker on CentOS 6.5

Role Variables
--------------

```
docker_centos_packages:
 - { package: "docker" }
```

Example Playbook
-------------------------

    - hosts: docker-servers
      roles:
         - { role: docker-centos, 
                   tags: ["docker"] }

Author Information
------------------

# anandkumarpatel
###         #
# Configuring Vault

Vault is specifically designed to be manually setup. This is not automated for a reason.

```
kubectl port-forward INSTERT_VAULT_ID 8300:8200
export VAULT_ADDR=http://localhost:8300
```

The first time you setup vault we need to manually configure a bunch 
of things so we don't pass around the root token.

`vault init`

Grab the keys, put them in 1password

`vault unseal $key1`

`vault unseal $key2`

`vault unseal $key3`

Verify the vault unsealed

`vault auth`
Paste in the $rootToken


Now to setup the policies:

```
vault policy-write organizations-writeonly roles/vault/additional-files/user-vault/policies/organizations-writeonly.hcl
vault policy-write organizations-readonly roles/vault/additional-files/user-vault/policies/organizations-readonly.hcl
vault policy-write dock-user-creator roles/vault/additional-files/user-vault/policies/dock-user-creator.hcl
```

Now to setup the roles

`vault write auth/token/roles/organizations-readonly allowed_policies="organizations-readonly"`

Now to setup new token for starlord:

`vault token-create -policy="organizations-writeonly" -ttl="8760h"`

Take the response of this and save it in the configuration for the environment you want as the `starlord_vault_token`

Create a new token for the docks, so they can create readonly tokens.

`vault token-create -policy="dock-user-creator" -ttl="8760h"`

Save that token as the `dock_vault_user_creation_access_token`

This allows the vault user to create a new user using:
vault write -f auth/token/create/organizations-readonly
Run Khronos CLI tool out of cron once daily.

`tasks/main.yml` - install cron entry to run `/khronos/bin/cli.js` and output to `{{ app_log_dir }}/khonos_cron.log`
iptables
===========

This role installs and configure psad and syscfg

This role is to be run on docks to effectivly help limit ratelimiting and stop containers from accessing things they shouldn't
Role Name
========

Ansible Role to Install Docker on CentOS 6.5

Role Variables
--------------

```
docker_centos_packages:
 - { package: "docker" }
```

Example Playbook
-------------------------

    - hosts: docker-servers
      roles:
         - { role: docker-centos, 
                   tags: ["docker"] }

Author Information
------------------

# anandkumarpatel
###         #
# Role Name

Ansible Role to Install Docker Client Certs on Ubuntu

## Manual Setup

Creating new docker client certs:
1. cd into this dir ```cd <roles/docker_client>```
2. ensure you have ca-key.pem here `roles/docker_client/ca-key.pem`
3. run cert generator ```sudo ./scripts/genClientCert.sh <app name> <server ip>```

## Author Information

anandkumarpatel
Role Name
========

Ansible Role to Install base_centos deps

Author Information
------------------

# anandkumarpatel
###         #
# SSH-KEYS

This is fun. In the `vars` file, you can add groups that the user is added to (use comma seperated values)
Role Name
========

Ansible Role to setup redis key

Author Information
------------------

# anandkumarpatel
###         #
# Role Name

Ansible Role to Install Docker on Ubuntu

## Manual Setup

*Important: You must set up the following certificates on new boxes manually (for now):*

For the Docker daemon:
- `/etc/ssl/docker/`:
  - `ca.pem`: CA certificate that also signed the client keys
  - `cert.pem`: Docker _server_ certificate
  - `key.pem`: Key used to sign the Docker server certificate

For the Docker client:
- `/home/ubuntu/.docker/`:
  - `ca.pem`: CA certificate that also signed the client keys (should be the same one as in `/etc/ssl/docker`)
  - `cert.pem`: Docker _client_ certificate
  - `key.pem`: Key used to sign the Docker client certificate

To ensure docker verifies the local client, you need to either pass `--tlsverify` to the docker command, or you need to set `DOCKER_TLSVERIFY=1` in the environment.

## Role Variables

```
docker_centos_packages:
 - { package: "docker" }
```

## Example Playbook

    - hosts: docker-servers
      roles:
         - { role: docker-centos, 
                   tags: ["docker"] }

## Author Information

anandkumarpatel
# Environments

Environments should have the following structure:

```
main.yml (main variable file)
inventory
  hosts
k8 (directory, automatically populated)
secrets (directory, see below)
```

### Secrets

This directory should have the following files:

```
/docker-client
  id_rsa
  known_hosts
  ca.pem
  ${SERVICE_NAME} (api, khronos, etc.)
    cert.pem
    key.pem
/certs
  ca-key.pem
  ca.pem
  ca.srl
  cert.pem
  key.pem
  pass
/domains
  /${DOMAIN}
    ca.pem
    cert.pem
    key.pem
    chained.pem
    dhparam.pem
```
# Deployer
![Deployer](https://cloud.githubusercontent.com/assets/2194285/21335997/6f51847c-c617-11e6-999d-4db7794d6be0.jpg)

## Purpose
Deployer is the application that is in charge of deploying code here at runnable.


## How it works
Deployer is just a runnable wrapper around ansible. It takes jobs from `deploy.requested` exchange and converts them into ansible playbook commands.

