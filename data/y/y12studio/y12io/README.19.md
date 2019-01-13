## Build on Ubuntu 14.04 
```
$ sudo apt-get install npm nodejs-legacy
$ sudo npm install -g strong-cli
// make loopback project
$ slc lb project lb-hello
$ tree -L 2 lb-hello
lb-hello
├── app.js
├── app.json
├── datasources.json
├── models
├── models.json
├── node_modules
│   ├── loopback
│   ├── loopback-datasource-juggler
│   ├── loopback-explorer
│   └── loopback-push-notification
└── package.json

6 directories, 5 files
$ cd lb-hello
// make model
$ slc lb model person -i
// first last
$ node .
// browser to http://localhost:3000/explorer
// PUT new person
// Request http://192.168.2.73:3000/api/people
  {
    "id": 1,
    "first": "Lin",
    "last": "None"
  }
```

## Docker

```
$ git clone https://github.com/y12studio/y12io
$ cd y12io/projects/loopback-hello/
$ sudo docker.io build -t="test/lbho" .
$ sudo docker.io run -d -p 80:3000 test/lbho
$ curl http://localhost/
```
