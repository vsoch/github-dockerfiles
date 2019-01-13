# Docker Private Registry using Nexus

## Run

```
mkdir /your-path/nexus-data
sudo chown -R 100:101 /your-path/nexus-data
docker run \
  -d \
  --name nexus \
  -v /your-path/nexus-data:/nexus-data \
  -p 8081:8081 \
  -p 5000:5000 \
  giabar/docker-registry-nexus
```

The Nexus default credentials are admin/admin123

Follow the instructions on Nexus website to add the Docker registry to your Nexus instance: https://books.sonatype.com/nexus-book/3.0/reference/docker.html?__hstc=239247836.7e789409bfa516187dbb0cc3fb843cee.1487784788853.1489409847685.1489412772483.7&__hssc=239247836.4.1489412772483&__hsfp=2635578825
