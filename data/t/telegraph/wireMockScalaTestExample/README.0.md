Get WireMock running:
- build jar    - mvn clean compile assembly:single
- build image  - docker build -t wiremockserver .
- run image    - docker run -p 8080:8081 wiremockserver

api          - http://localhost:8080/resource/it

Wiremock log - GET http://host:port/__admin/requests

CLI test     - mvn clean package
