# Helm chart for k8ecr autodeployment

| Parameter                 | Description                                             | Default                    |
| ---------                 | -----------                                             | -------                    |
| `targetNamespace`         | Target namespace in which to autodeploy all deployments | Required value             |
| `replicaCount`            | Number of replica pods in the deployment                | `1`                        |
| `image.repository`        | Image repository                                        | `isotoma/k8ecr-autodeploy` |
| `image.tag`               | Image tag                                               | `latest`                   |
| `image.pullPolicy`        | Image pull policy                                       | `IfNotPresent`             |
| `resources`               | Resources                                               | `{}`                       |
| `nodeSelector`            | Deployment node selector                                | `{}`                       |
| `tolerations`             | Deployment tolerations                                  | `[]`                       |
| `affinity`                | Deployment affinity                                     | `{}`                       |
| `podAnnotations`          | Deployment pod annotations                              | `{}`                       |
| `rbac.create`             |                                                         |                            |
| `rbac.serviceAccountName` |                                                         |                            |
| `webhookUrl`              | URL to post results to                                  | `''`                       |
| `awsRegion`               | AWS region to check for ECR                             |                            |
