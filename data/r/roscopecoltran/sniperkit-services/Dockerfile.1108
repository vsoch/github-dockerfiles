FROM quay.io/coreos/etcd:v3.1.6
RUN apk --no-cache add bash
ADD goodrain_etcd.sh .
RUN chmod 655 /goodrain_etcd.sh 
EXPOSE 2379
EXPOSE 2380
ENTRYPOINT ["/goodrain_etcd.sh"]
