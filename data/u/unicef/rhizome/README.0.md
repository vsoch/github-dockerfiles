# react-json
A JSON editor packed as a React.js component, but also the simplest way of creating web forms.

[Play safe with react-json forms in the playground](http://codepen.io/arqex/pen/rVWYgo?editors=001).

React-json is like having an special input type for JSON objects, developers only need to listen to changes in the JSON instead of writing all the boilerplate needed to handle every single input of the form. It comes with top features:
* Field type guessing for quick forms
* Validation
* Styles easily customizable
* Extensible with custom field types

## Examples
Do you want to edit some JSON in your app? Pass it to the Json component:
```js
var doc = {
  hola: "amigo",
  array: [1,2,3]
};

React.render(
  <Json value={ doc } onChange={ logChange } />,
  document.body
);

function logChange( value ){
   console.log( value );
}
```
[See this example working](http://codepen.io/arqex/pen/rVWYgo?editors=001)

## A simple form creator
Do you hate creating forms? React-json handles all the dirty markup for you, and makes you focus in what is important;
```js
var doc = {
  user: "",
  password: ""
};

// form: true
// make objects not extensible,
// fields not removable
// and inputs always visible
var settings = {
  form: true,
  fields: { password: {type: 'password'} }
};

React.render(
  <Json value={ doc } settings={ settings }/>, 
  document.body
);
```
[See this form working](http://codepen.io/arqex/pen/xGRpOx?editors=011)

## Docs
React JSON is highly configurable, have a look at the docs to discover how.

## MIT licensed
[License here](LICENSE)
react-hot-boilerplate
=====================

The minimal dev environment to enable live-editing React components.

### Usage

```
npm install
npm start
open http://localhost:3000
```

Now edit `src/App.js`.  
Your changes will appear without reloading the browser like in [this video](http://vimeo.com/100010922).

### Linting

This boilerplate project includes React-friendly ESLint configuration.

```
npm run lint
```

### Using `0.0.0.0` as Host

You may want to change the host in `server.js` and `webpack.config.js` from `localhost` to `0.0.0.0` to allow access from same WiFi network. This is not enabled by default because it is reported to cause problems on Windows. This may also be useful if you're using a VM.

### Missing Features

This boilerplate is purposefully simple to show the minimal configuration for React Hot Loader. For a real project, you'll want to add a separate config for production with hot reloading disabled and minification enabled. You'll also want to add a router, styles and maybe combine dev server with an existing server. This is out of scope of this boilerplate, but you may want to look into [other starter kits](https://github.com/gaearon/react-hot-loader/blob/master/docs/README.md#starter-kits).

### Dependencies

* React
* Webpack
* [webpack-dev-server](https://github.com/webpack/webpack-dev-server)
* [babel-loader](https://github.com/babel/babel-loader)
* [react-hot-loader](https://github.com/gaearon/react-hot-loader)

### Resources

* [Demo video](http://vimeo.com/100010922)
* [react-hot-loader on Github](https://github.com/gaearon/react-hot-loader)
* [Integrating JSX live reload into your workflow](http://gaearon.github.io/react-hot-loader/getstarted/)
* [Troubleshooting guide](https://github.com/gaearon/react-hot-loader/blob/master/docs/Troubleshooting.md)
* Ping dan_abramov on Twitter or #reactjs IRC
