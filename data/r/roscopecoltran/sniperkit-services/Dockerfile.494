FROM t0t0/docker-alpine-kibana

# where 'elastic' in URL is name of linked container providing elastic search
ENTRYPOINT ["kibana","-e http://elastic:9200"]
