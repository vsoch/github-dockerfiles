# Full Stack Bot [![Build Status](http://ci.codegram.com/api/badges/codegram/full_stack_bot/status.svg)](http://ci.codegram.com/codegram/full_stack_bot)

The engine behind Full Stack Fest's 2016 AI bot.

![Demo](http://i.giphy.com/l3UcebLyvjNFOAkBq.gif)

## Tech Stack

* An [elixir](http://elixir-lang.org/) umbrella app containing two apps:
  * The bot engine that talks to [api.ai](https://api.ai).
  * A web interface leveraging [phoenix](http://www.phoenixframework.org/).

The web interface uses:

* [webpack](https://webpack.github.io/) to bundle all the assets.
* [babel](https://babeljs.io/) to transpile ES7.
* [react.js](https://facebook.github.io/react/) to render the views.
* [mobx](https://github.com/mobxjs/mobx) for state handling.

It can be easily deployed via docker as it includes a Dockerfile.
