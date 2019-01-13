Reactive, real-time log search with Play, Akka, AngularJS, D3js and MongoDB
===========================================================================

Demonstration using Play!, Akka, AngularJS, D3.js, and a MongoDB capped collection and tailable cursor to perform real-time log entry search.

Please see the initial implementation discussion at [blog article](http://www.dreweaster.com/blog/2013/07/08/reactive-real-time-log-search-with-play-akka-angularjs-and-elasticsearch/).
for the note on the base application I 

DaVe : List of changes/additions
* Some actor cleanup where state is involved
* Isolate log generator code to allow it to be optional
* Added raw display of server fed data via Akka actors
* Added D3.js dynamic chart, updates fed from the server
* All data feed through 1 WebSocket connection with the server.
* MongoDB tailable cursor implemented in place of elasticsearch
* New Bootsrap 3 look and feel theme.

## Licence

This software is licensed under the Apache 2 license, quoted below.

Copyright &copy; 2014 **[DaVe Buschman](https://github.com/dbuschman7)**. 

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this project except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

scala-in-java
=============

Investigation of using a Scala Dispatch HTTP client library from within Java


This is your new Play application
=====================================

This file will be packaged with your application, when using `play dist`.
