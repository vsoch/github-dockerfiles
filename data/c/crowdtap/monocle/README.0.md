The crowdtap-nginx creates a Kubernetes deployment running Nginx with Crowdtap's URI routing and other sundries. It is based on the official nginx alpine image, which is tiny.

Currently this is a manual build when needed.

You'll need to be logged into AWS ECR by running `aws ecr get-login` and then running the resultant command or in one step: `$(aws ecr get-login)`.

To build and push a new nginx container:

```shell
docker build -t crowdtap-nginx .
docker tag crowdtap-nginx 535700620794.dkr.ecr.us-east-1.amazonaws.com/crowdtap-nginx:latest
docker push 535700620794.dkr.ecr.us-east-1.amazonaws.com/crowdtap-nginx:latest
```
