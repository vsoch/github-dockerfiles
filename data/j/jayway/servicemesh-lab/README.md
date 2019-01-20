# Service mesh on Kubernetes lab
This repo contains files for deploying microservices to a Kubernetes cluster.

There are three microservices:
* `numbergen` which generates numbers, for example `42`
* `namegen` which generates names of animals, for example `albatross`
* `combinedgen` which generates combinations of the two services, for example `albatross-42`

## Build docker images

**Using Azure Cloud Shell?**
> First, install a docker machine.
> ```bash
> DOCKER_RESOURCEGROUP_NAME="sandbox-<firstname>.<lastname>"
> docker-machine create \
>  --driver azure \
>  --azure-location ${ACC_LOCATION} \
>  --azure-resource-group ${DOCKER_RESOURCEGROUP_NAME} \
>  --azure-subscription-id "$(az account show --query id -o tsv)" \
> servicemesh-dockerhost
> ```
> The first time you try to create a machine, Azure driver will ask you to authenticate.
>
> If the host already exist, remove it with `$ docker-machine rm servicemesh-dockerhost`
>
> List docker machines with `$ docker-machine ls`
>
> Configure the shell `$ eval $(docker-machine env servicemesh-dockerhost --shell bash)`

### Build containers
```bash
docker-compose -f build-all.yml build

# equivalent to:
# docker build -t namegen-scratch ./namegen/
# docker build -t numbergen-scratch ./numbergen/
# docker build -t combinedgen-alpine ./combinedgen/
```

## Test containers
**Using Azure Cloud Shell?**
> Make sure you have an inboud rule for port 8080, since the Cloud Shell is not in the same vnet.
>
> To list existing rules: `$ az network nsg rule list --nsg-name servicemesh-dockerhost-firewall --resource-group ${DOCKER_RESOURCEGROUP_NAME} --output table`
>
> To create a rule:
> ```bash
> az network nsg rule create \
>  --nsg-name servicemesh-dockerhost-firewall \
>  --name Port8080 \
>  --priority 500 \
>  --destination-port-ranges 8080 \
>  --resource-group ${DOCKER_RESOURCEGROUP_NAME}
> ```

```bash
docker run -d -p 8080:8080 namegen-scratch
curl $(docker-machine ip servicemesh-dockerhost):8080
```

## Troubleshooting
Problem: `Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock:`

Solution: Current user does not have permission. Run command with `sudo`.
