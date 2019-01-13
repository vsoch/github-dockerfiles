Postgres on Kubernetes
======================

Extends the original postgres docker image to (optionally) read the
secrets from `/etc/postgres-credentials`.

Image Name: `unit9/postgres`


Usage
=====

## Replication controller

    kind: ReplicationController
    apiVersion: v1
    metadata:
      name: postgres-master
    spec:
      replicas: 1  # only one is allowed
      selector:
        app: postgres-master
      template:
        metadata:
          name: postgres-master
          labels:
            app: postgres-master
        spec:
          containers:
            - name: postgres
              image: unit9/postgres:9.5
              ports:
                - name: transport
                  containerPort: 5432
              volumeMounts:
                - name: data-storage
                  mountPath: /var/lib/postgresql/data
                - name: credentials
                  mountPath: /etc/postgres-credentials
              env:
                - name: PGDATA
                  value: /var/lib/postgresql/data/pgdata
          volumes:
            - name: data-storage
              gcePersistentDisk:  # Whatever suits your case
                pdName: postgres-data
                fsType: ext4
            - name: credentials
              secret:
                secretName: postgres-credentials

## Secret

    apiVersion: v1
    kind: Secret
    metadata:
      name: postgres-credentials
    data:
      password: <base64 encoded secret>
