# Nginx on Kubernetes

Dockerized [nginx][], with a simple config file that makes it easy to
integrate with Kubernetes, without rebuilding the image.

Makes it easy to proxy internal webapps running on the cluster.

[nginx]: https://nginx.org

## Features

### `/etc/nginx/conf.d` as a [ConfigMap][]

Read up about [ConfigMap][].

[ConfigMap]: https://kubernetes.io/docs/user-guide/configmap/

This makes it easy to add vhosts. Save this as `nginx-confd.yaml`:

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: nginx-confd
data:
  example-com.conf: |
    server {
        listen 80;
        server_name example.com www.example.com;
        proxy_pass http://example/
    }
```

Create the ConfigMap with: `kubectl create -f nginx-confd.yaml`

Here's the pod spec (plug it into your ReplicationController,
ReplicaSet, etc):

```yaml
spec:
  containers:
  - name: nginx-frontman
    image: unit9/kubenginx
    volumeMounts:
    - name: nginx-confd
      mountPath: /etc/nginx/conf.d
  volumes:
  - name: nginx-confd
    configMap:
      name: nginx-confd
```

Expose the pods as an external service (e.g. via `type:
LoadBalancer`), and hit the external IP:

    curl -v -H 'Host: www.example.com' 12.34.56.789

### SSL params as a Secret volume

Mount `/etc/secrets`  as a (Secret) volume.
Put things like your `dhparams` and certificates there.
