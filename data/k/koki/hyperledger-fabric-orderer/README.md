Hyperledger Fabric Orderer (Stateless - no local config)
--------------------------------------------------------

Current orderer implementation is

1. Tightly coupled with reading config from local files
2. Using `cryptogen` before setting up orderer is unnecessary, however current impl forces one to do that
3. Not well documented
4. Tied to docker-compose
5. Bootstrapping orderer is complicated and requires co-ordinating files

This implementation reuses most parts of the existing orderer, but

1. cleans up the design
2. is loosely coupled and modular
3. is not tied to docker-compose
4. meant to run on Kubernetes
5. meant to aid dynamic addition of new orgs (orderers, peers, msps)

and Docs! expect a lot of Docs!
