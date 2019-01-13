to create a self-signed certificate from the root ca run
sh create-kibana4-certificates.sh

files will be located in ./out directory
take files kibana4.crt (this is the public certificate) and kibana4_pk.pem and store them in the 
 security/certs folder they will be copied by the Dockerfile and used for SSL between the browser and the kibana server. 
 This link is made via the kibana.yml
 
     > sh create-kibana4-certificates.sh
     > cp out/kibana.crt out/kibana_pk.pem out/ca.crt .
     > git add and commit