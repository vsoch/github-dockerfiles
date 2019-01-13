## build and run

```
$ sudo docker run -d -p 8080:8080  test/topeka
$ curl http://locahost:8080/
```

## Round1 zh_TW

UI TRUE/FALSE to 是/否
```
    {
                "type": "true-false",
                "question": "咖啡的咖啡因比茶葉還多",
                "answer": false
    },
```

topeka single html size

```
cd /opt/topeka
# du -h components
8.0M    components
# npm install -g vulcanize
# vulcanize index.html
# ls
bower.json   icons       leaderboard.html  sw.js
components   images      polyfills         theme.css
favicon.ico  index.html  README.md         vulcanized.html
# ls -al
-rw-r--r--  1 root root 612436  8æœˆ 14 07:30 vulcanized.html
```

test the vulcanized.html and upload to the hosting 
```
sudo docker run test/topeka cat /opt/topeka/vulcanized.html > /tmp/topeka_round1.html
upload to testsite and load topeka_round1.html

GET http://odtc.y12.tw/data/topeka/components/platform/platform.js 404 (Not Found) topeka_round1.html:40
GET http://odtc.y12.tw/data/topeka/components/polymer/polymer.js 404 (Not Found) topeka_round1.html:563
GET http://odtc.y12.tw/data/topeka/components/firebase/firebase.js 404 (Not Found) topeka_round1.html:1927
GET http://odtc.y12.tw/data/topeka/theme.css 404 (Not Found) topeka_round1.html:42
Uncaught ReferenceError: Polymer is not defined topeka_round1.html:574
Uncaught ReferenceError: Polymer is not defined topeka_round1.html:658
Uncaught ReferenceError: Polymer is not defined 

components/platform/platform.js = http://www.polymer-project.org/components/platform/platform.js
rewrite html and upload topeka_round1.html and theme.css

GET http://odtc.y12.tw/data/topeka_r1/components/firebase-simple-login/firebase-simple-login.js 404 (Not Found) topeka_round1.html:2364
GET http://odtc.y12.tw/data/topeka_r1/images/splash.svg 404 (Not Found) topeka_round1.html:1

rewrite and upload again

GET http://odtc.y12.tw/data/topeka_r1/components/topeka-elements/images/splash.svg 404 (Not Found) page.js:30
GET http://odtc.y12.tw/data/topeka_r1/polyfills/fonts/RobotoDraft-Thin.woff2 404 (Not Found) topeka_round1.html:11212
GET http://odtc.y12.tw/data/topeka_r1/components/topeka-elements/categories.json 404 (Not Found) topeka_round1.html:1588
GET http://odtc.y12.tw/data/topeka_r1/polyfills/fonts/RobotoDraft-Regular.woff2 404 (Not Found) topeka_round1.html:1
GET http://odtc.y12.tw/data/topeka_r1/polyfills/fonts/RobotoDraft-Thin.woff 404 (Not Found) topeka_round1.html:1
GET http://odtc.y12.tw/data/topeka_r1/polyfills/fonts/RobotoDraft-Regular.woff 404 (Not Found) topeka_round1.html:1

got in trouble with vulcanized.html
```


## ref

[Polymer/topeka](https://github.com/Polymer/topeka)

[Polymer/topeka-elements](https://github.com/Polymer/topeka-elements)

[Polymer/tools](https://github.com/Polymer/tools)

backend [Polymer/firebase-element](https://github.com/Polymer/firebase-element)

data flow

* [topeka/index.html at master · Polymer/topeka](https://github.com/Polymer/topeka/blob/master/index.html)
* [topeka-elements/topeka-datasource.html at master · Polymer/topeka-elements](https://github.com/Polymer/topeka-elements/blob/master/topeka-datasource.html)
* [firebase Search Results](https://github.com/Polymer/topeka-elements/search?q=firebase-element)