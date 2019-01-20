# APIcast Cloud Hosted on OpenShift

1. Download `3scale+openshift` robot account credentials from quay.io as kubernetes object (`secret.yml`)
1. `oc project NAME`
1. `oc create -f secret.yml`
1. `oc secrets add serviceaccount/default secrets/3scale-openshift-pull-secret --for=pull`
1. `oc secret new-basicauth master-access-token-secret --password=MASTER_ACCESS_TOKEN`
1. `make imagestream` to deploy the imageStreams (Apicast Cloud Hosted and Apicast Builder)
1. `make buildconfig` to create the BuildConfig
1. `make deploy RELEASE_REF=release_number ENVIRONMENT=staging CACHE_TTL=0` - (with `ENVIRONMENT=production CACHE_TTL=300` for production or  `ENVIRONMENT=staging CACHE_TTL=0` for staging)
1. `make route ENVIRONMENT=staging WILDCARD_DOMAIN=cluster.wildcard.domain.com` -  Wildcard Domain Concatenation: `apicast.${ENVIRONMENT}.${WILDCARD_DOMAIN}` 
