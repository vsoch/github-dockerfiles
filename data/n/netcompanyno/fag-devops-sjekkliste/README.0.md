# todomvc-common

> Common TodoMVC utilities used by our apps


## Install

```
$ npm install --save todomvc-common
```


## License

MIT © [TasteJS](http://tastejs.com)
# todomvc-app-css

> CSS for TodoMVC apps

![](screenshot.png)


## Install


```
$ npm install --save todomvc-app-css
```


## Getting started

```html
<link rel="stylesheet" href="node_modules/todomvc-app-css/index.css">
```

See the [TodoMVC app template](https://github.com/tastejs/todomvc-app-template).



## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This <span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/InteractiveResource" rel="dct:type">work</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://sindresorhus.com" property="cc:attributionName" rel="cc:attributionURL">Sindre Sorhus</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.
# packaged angular-mocks

This repo is for distribution on `npm` and `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngMock).
Please file issues and pull requests against that repo.

## Install

You can install this package either with `npm` or with `bower`.

### npm

```shell
npm install angular-mocks
```

You can `require` ngMock modules:

```js
var angular = require('angular');
angular.module('myMod', [
  require('angular-animate'),
  require('angular-mocks/ngMock')
  require('angular-mocks/ngAnimateMock')
]);
```

### bower

```shell
bower install angular-mocks
```

The mocks are then available at `bower_components/angular-mocks/angular-mocks.js`.

## Documentation

Documentation is available on the
[AngularJS docs site](https://docs.angularjs.org/guide/unit-testing).

## License

The MIT License

Copyright (c) 2010-2015 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# packaged angular

This repo is for distribution on `npm` and `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js).
Please file issues and pull requests against that repo.

## Install

You can install this package either with `npm` or with `bower`.

### npm

```shell
npm install angular
```

Then add a `<script>` to your `index.html`:

```html
<script src="/node_modules/angular/angular.js"></script>
```

Or `require('angular')` from your code.

### bower

```shell
bower install angular
```

Then add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular/angular.js"></script>
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/).

## License

The MIT License

Copyright (c) 2010-2015 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
# packaged angular-route

This repo is for distribution on `npm` and `bower`. The source for this module is in the
[main AngularJS repo](https://github.com/angular/angular.js/tree/master/src/ngRoute).
Please file issues and pull requests against that repo.

## Install

You can install this package either with `npm` or with `bower`.

### npm

```shell
npm install angular-route
```

Then add `ngRoute` as a dependency for your app:

```javascript
angular.module('myApp', [require('angular-route')]);
```

### bower

```shell
bower install angular-route
```

Add a `<script>` to your `index.html`:

```html
<script src="/bower_components/angular-route/angular-route.js"></script>
```

Then add `ngRoute` as a dependency for your app:

```javascript
angular.module('myApp', ['ngRoute']);
```

## Documentation

Documentation is available on the
[AngularJS docs site](http://docs.angularjs.org/api/ngRoute).

## License

The MIT License

Copyright (c) 2010-2015 Google, Inc. http://angularjs.org

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
