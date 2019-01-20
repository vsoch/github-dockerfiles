# Lenses

`@atomic-object/lenses` is a small functional lens library for TypeScript with the goal of being small, with zero dependencies, and strong, precise types. It is inspired by [Aether](https://github.com/xyncro/aether), for F#.

Lenses are getter/setter pairs that let you represent a location within some data structure for both reading and updating that location. "Update" in this case is in the functional sense – not by mutation, but by creating a new data structure with a new value in the location of interest. A little like a pointer offset in C, but memory-, type-, and mutation-safe.


## Basic Usage

The simplest use is to represent a property of an object. Consider this type 

```ts
type Something = { foo: number; bar: string };
```

We could define a helper module with lenses for interacting with this type:

```ts
export namespace Something = {
  export const foo = Lens.from<Something>().prop("foo");
  export const bar = Lens.from<Something>().prop("bar");
}
```

In this example, `Something.foo` has type `Lens<Something, number>`, meaning that it can read numbers from and write numbers to a `Something`. `bar` is inferred to have type `Lens<Something, string>` – it only accepts string values.

Given a value of type `Something`:

```ts
let o: Something = { foo: 1, bar: "hello" };
```

we can get values

```ts
// Get the foo of a Something
expect(Something.foo.get(o)).toBe(1);
// Or just treat the lens as a function to do the same thing:
expect(Something.foo(o)).toBe(1);
expect(Something.bar(o)).toEqual("hello")
```

And we can create updated by `set`ting the lens:

```ts
let o2 = Something.foo.set(o, 10);
expect(o2).toEqual({ foo: 10, bar: "hello" });
expect(o).toEqual({ foo: 1, bar: "hello" });
```

Or `update`-ing the value by running it through a function:

```ts
let o3 = Something.foo.update(o, i => i+1);
expect(o3).toEqual({ foo: 2, bar: 'hello'})
```

## Lens Composition

Lenses can also be composed. This is a powerful technique for building abstractions. While immutability helper and spreads require deep knowledge about the shape of a data structure, violating the [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter), lenses represent concepts, and programming to them decouples you from the underlying data structure.

For example, consider a container type which contains a `Something` and a value of that type:

```ts
type ContainsSomething = {
  something: Something;
};
const container: ContainsSomething = {
  something: { foo: 19, bar: "hola" }
};
```

We can create a lens for the `something` property, and compose it with our other lenses:

```ts
let innerFoo = Lens.from<ContainsSomething>()
  .prop("something")
  .comp(Something.foo);
expect(innerFoo(container)).toEqual(19);
```

Users of our `innerFoo` lens don't need to couple themselves to either the location of `Something` within `ContainsSomething`, nor the location of the logical value of `foo` within it. We're completely free to reorganize our data structure, provided all users of it are programmed to lenses.

## Currying

Both `set` and `update` are curried – you can provide just a target value or an update function to get back "updater" functions (e.g. `Something => Something`) that can be composed together to make multiple updates at once.

For example,

```ts
import { flow } from "lodash";
let o5 = flow(
  Something.foo.update(i => 10 * i),
  Something.bar.set("world")
)(o);
```

## Custom Lenses

Lenses need not point simply to properties of an object, but can be used for anything that could be logically get/set. The underlying representation need not matter.

For example, we could create a lens that presents the low bit of an integer as a boolean:

```ts
const lowBitLens = Lens.of<number, boolean>({
  get: n => (n & 1 ? true : false),
  set: (n, b) => (b ? n | 1 : n & ~1)
});
```

Given this definition, we're free to read/write booleans into numbers as follows:

```ts
expect(lowBitLens(10)).toBe(false);
expect(lowBitLens(11)).toBe(true);
expect(lowBitLens.set(10, true)).toBe(11);
expect(lowBitLens.set(11, false)).toBe(10);
expect(lowBitLens.update(9, b => !b)).toBe(8);
```

## Isomorphisms

In addition to creating lenses with `Lens.of` that operate on arbitrary substructure – or even equivalent substructure, such as the low-bit lens example – you can also `map` from one lens type to another.

For example, let's say you have a menu component that takes a `MenuProps`. You have `ApplicationState` in your redux store that you want to control your menu, but that state may be in charge of other things as well that should all be consistent. If you can provide a bi-directional mapping between your application state and a `MenuProps`, you could always convert your app state into menu inputs, and changes to the menu props back into equivalent changes in your application state. Your menu, therefore, can think it is operating on a `MenuProps` when instead it's updating `ApplicationState`.

For a simpler example, let's look at an isomorphism that converts numbers to strings, and use it to create a lens that operates on strings, but stores the value as a number.

```ts
let n2s: Isomorphism<number, string> = {
  to: n => n.toString(),
  from: s => parseInt(s, 10)
};
const sFoo = Lens.map(Something.foo, n2s);

let o: Something = { foo: 1, bar: "hello" };
expect(sFoo(o)).toEqual("1");
const o6 = sFoo.set(o, "1234");
expect(o6).toEqual({ foo: 1234, bar: "hello" });
```

## Prisms

We also provide a type for Prisms, which are lenses for which `get` may fail, returning `undefined`. See the code/tests for more examples.


## Functional array helpers

`@atomicobject/lenses/lib/arrays` provides functional versions of `splice`, `pop`, `push`, `unshift`, and `shift`, as well as an `index` function which returns a `Prism` for read/writing an arbitrary index in an array.
# SPA Starter Kit

This starter kit is meant as a starting point for single-page webapps using TypeScript, React, Redux, and GraphQL that we use at Atomic Object. Feel free to clone this project and use it to seed any project for which it would be helpful.

## TODO
Still to be set up/configured in this starter kit.

### Starter kit todos
- [ ] CoreJS for polyfill support
- [ ] fetch polyfill for Apollo in non-bleeding edge browser?
- [x] Source maps
- [x] Browser testing – nightmare?
- [ ] css prefixing settings
- [ ] Reselect?
- [ ] Clean DB between tests – pull in `knex-cleaner`
- [x] Node clustering
- [x] GraphQL client
- [x] DB / Docker / migrations

### README Todos

- [x] Module organization
- [x] Running tests
- [x] TSlint
- [x] Async (redux sagas)
- [x] Database
- [x] Selectors/state updates – lens intro
- [x] Bourbon/neat trello CSS guide
- [x] Property-based testing
- [ ] Debugging
- [ ] Repositories/DataLoader/GraphQL Context


## Stack
This project is a single-page webapp using the following technologies:

* [TypeScript](https://www.typescriptlang.org)  – a type-safe variant of JavaScript from Microsoft which reduces errors and improves IDE/editor support over regular JavaScript.
* Node.js – powers our server, and is pinned to the latest LTS release.
* [Express](https://expressjs.com) – our HTTP server, which is lightly used only to host our GraphQL API.
* [GraphQL](http://graphql.org) – an alternative to REST apis which supports a demand-driven architecture.  Our GraphQL server is [Apollo GraphQL server](http://dev.apollodata.com/tools/graphql-server/).
* [Jest](http://facebook.github.io/jest/#use) – for unit testing.
* [Webpack](https://webpack.github.io) – builds our application for our various deployment targets.
* [Redux](http://redux.js.org) for client state management.
* [Redux Saga](https://redux-saga.js.org) for workflows and asynchronous processes.
* [JSVerify](http://jsverify.github.io) for property-based testing.
* [Nightmare.js](http://nightmarejs.org) for acceptance testing.
* [React Storybook](https://storybook.js.org/) for component documentation and style guides.

## Code Organization
This repository is structured to encourage a view of the whole repository as one application. The client and server are “just” different entry points, and we use webpack to elide libraries and code that are irrelevant to a particular entry point.

There are a few key directories:
* `entry` – contains the primary entry points of the application. If you want to see what happens when you start up the client or server, start there.  These are also the entry points for webpack.
* `webpack` contains a webpack configuration for each entry point, as well as `webpack-dev-server.js` which sets up the dev server used during development.
* `modules` contains all of the code. Each module is a self-contained concept that may be used by other modules, command-line scripts, etc.
* `config` contains configuration files for our various environments. The default config is set up as a twelve-factor app to be hosted in heroku. Most variables can be controlled via the environment – see `config/default.js`.
* `dist` is where webpack stores compiled slices of the app.

Default modules:
* `client` – React/redux front-end.
* `db` – core knex database connection helpers
* `records` – database record types and repositories, with base record and repository classes in `record`. Depends on `db`
* `graphql` – Graphql schema and implementation. Depends on `records` and `db`
* `server` – express.js server that serves the client and graphql api. Depends on `graphql`
* `helpers` – generic helpers that can be used in any other module – no dependencies

## Environment Variables

This app is set up as a 12-factor app, configurable via environment variables.

The supported environment variables are:

* `NODE_ENV` – `test`, `development`, or `production`
* `DATABASE_URL` – the url of the postgres database.
* `PORT` – port for the server to bind to. Defaults to `3001`
* `PUBLIC_HOST` – the public facing domain name to include in e.g. links.
* `REQUIRE_SSL` – if this is not `false`, all requests are redirected to HTTPS.
* `WEB_CONCURRENCY` – # of workers to use in clustered mode. Clustering disabled if value is 1.
* `NODE_MAX_OLD_SIZE` - limit node process size to a given amount. Defaults to `460` MB to work well in 512MB containers, such as heroku.
* `DEV_SERVER_DISABLE_HOST_CHECK` - disables the host check in webpack dev server, to allow testing from a VM or other host.


## Setup

* Install Docker.app. Our database and other services are configured to run in docker.
* Copy `.env.example` to `.env`. You can set any environment variables you want here to influence the application.
* Start postgres with: `docker-compose up`. This will set up a postgres docker image and start it.
* Run `yarn db:create` to create development and test databases.


Note: Start `docker-compose up` and leave it running any time you want to run the app/tests.

## Running locally
Run `yarn dev` to start up both the server and client at the same time. 

`yarn dev` runs:
* webpack in watch mode to hot recompile the server
* nodemon to run the server on port `3001` and restart the server on recompilation.
* webpack-dev-server to run the client on port `3000`, with proxy through to the server
* nodemon processes to regenerate typescript types corresponding to graphql files on change.

The dev server watches for changes and restarts `express` each time a dependency file changes.

The dev client is using the `webpack-dev-server` to hot reload the client whenever a file changes. Our webpack dev server is configured in `webpack/webpack-dev-server.js`.

To build for production, run:

```
NODE_ENV=production yarn build
```

This will build the entire app into `./dist/`.

## Tests
We are using Jest for unit testing, and colocating tests with the modules they’re testing.

Unit tests for a module are located in a `__tests__` directory  in the same directory as the file being tested.  Tests for `module.ts` should be named `module.test.ts`. Index files should be named after their parent directory. `some-module/index.ts` should be tested in `some-module/__tests__/module.test.ts`.

### Running Unit Tests

To run unit tests, run `yarn jest`. This simply runs jest in the current directory, which will use config in the `jest` section of `package.json`.

To run jest in watch mode, and have it automatically rerun tests when files change:

```
yarn jest -- --watch
```

To see other jest options, you can run:

```
yarn jest -- --help
```

### Property testing

We are using  [JSVerify](http://jsverify.github.io) for property-based testing. Property-based testing is based on generating arbitrary inputs for functions and asserting that properties are invariant across those inputs. If an input is found which violates the property, the library will automatically simplify it to the minimal case that reproduces the error.

### Generating test data

JSVerify has built-in test data generation helpers called `Arbitrary` values. It comes with built-in generators for various types, and `Arbitryary<T>` values can be composed together into larger types.  See the [JSVerify Readme](https://github.com/jsverify/jsverify).

By building up `Arbitrary` objects for our various types, we will have a library of test data generators which can also be used for property-based testing.

### Component tests

We are testing react components with [Enzyme](https://github.com/airbnb/enzyme) . See that for more information.

### Acceptance tests

Acceptance tests are written using [Nightmare](http://codecept.io). See the `test:acceptence` tasks for more.

### Linting

We are using `tslint` for linting. It is run automatically before unit tests.

## Styleguide

We are using [React Storybook](https://storybook.js.org/) to generate a styleguide for our react components.

You can run the style guide with `yarn dev:storybook`

## GraphQL and Code Generation

We're generating type definitions from our graphql schema, queries, and mutations. This allows us to get static type safety between our graphql code and typescript implementations.

To enable this, we're storing all graphql code in individual `.graphql` files. Our build process and dev server look for these and use them to generate the appropriate type definitions.

### Server

The file `modules/graphql/schema-types.ts` is generated by `graphql-code-generator` from `schema.graphql` and any other `.graphql` file in the `graphql` module.

`schema-types` exports interfaces for all graphql `type`s in the schema, including e.g. `Query`.

For example, if we have the following schema:

```graphql
type User {
  id: Int!,
  name: String!,
  email: String!,
}

type Query {
  usersById(id: Int!): [User]!,
}
```

`schema-types.ts` will contain definitions for:
* `Query` – containing the return types for each query
* `UsersByIdQueryArgs` – the expected arguments for the `usersById` query
* `User` – the straightforward typescript definition for `User`.

Note that we make liberal use of `!` in the query definition to disallow `null` values as appropriate. `!` should **not** be used when the operation may fail. `Graphql` prefers `null` returns in that case in most circumstances.

To make use of these types, we import them into our `modules/graphql/index.ts` for our resolver definition.

In particular, we would define our `usersById` resolver as:

```ts
 usersById(obj: {}, args: UsersByIdQueryArgs, context: Context): Promise<Query['usersById']> {
   ...
 }
```

Note that we use `UsersByIdQueryArgs` to tell typescript that this should be consistent with the defined schema arguments. We could use an inline type or separate interface, but doing so would defeat TypeScript's ability to tell us when we change the schema that our implementation is no longer compatible.

Similarly, we define the return type to be `Promise<Query['usersById']>`. `Query['usersById']` is TypeScript syntax that means "whatever tye type of `usersById` on in the `Query` type is". By using this type subscripting syntax, we get static validation that our resolver is compatible with our schema.

### GraphQL in the client

In the client we generate types for our graphql queries and mutations. 

Given a `.graphql` file containing the query:

```graphql
query Users($foo: Int!) {
  usersById(id: $foo) {
    id
    name
  }
}
```

Entries will be added to `modules/client/graphql-types.ts`:

```typescript
export interface UsersQueryVariables {
  foo: number;
}

export interface UsersQuery {
  // Returns all of the users in the system (canned results)
  usersById: Array< {
    id: number,
    name: string,
  } >;
}
```

The types and query can be used with Apollo by `require`-ing the `.grahql` file directly from typescript and passing it in where a query is expected. The `UsersQuery`

```typescript
export async function fetchUsers(id: number): Promise<UsersQuery['usersById']> {
  const vars: UsersQueryVariables = {
    foo: id
  }
  const result = await graphqlClient.query<UsersQuery>({
    query: require('./Answer.graphql'),
    variables: vars
  });

  return result.data.usersById;
}
```

### Graphql building

The `build:graphql` task generates all type files. It:

1. Generates `modules/graphql/schema.json` from the `schema.graphql`. This is used by subsequent steps.
2. Generates `schema-types.ts` in the graphql module
3. Generates `graphql-types.ts` in the client

The `dev:graphql` task – which is run automatically by `dev` – watches for changes to any `.graphql` file and reruns `build:graphql`

## Client Overview

The client has the following capabilities built-in:

* Apollo Client for GraphQL queries/mutations.
* Redux Saga for asynchronous workflows.
* A small lens library for state selectors/updates.

Apollo Client is a smart graphql client with automatic caching and higher-order components for wiring presentation components to graphql queries.

Redux Sagas uses ES7 generator functions to support high level declaration and coordination of asynchronous workflows.

See `modules/client/sagas/index.ts` for an example redux saga which uses the apollo client to execute graphql queries.

Accessing/updating functional state in TypeScript requires a different solution from many of the common solutions in JavaScripot – `immutable-helper`, for example, is fundamentally untypable.

This starter-kit includes a library of functional lenses which are simple read/write helpers for accessing and updating substate of another object. A lens can be used as a function to get something out of an object, or can have `.set` or `.update` called on it to create an updated copy of an object.

The lens library is defined in `modules/helpers/lenses.ts`. See the tests for examples, as well as use in `sagas/index.ts` and `reducers/index.ts`.


## CSS
CSS is implemented using the [Trello CSS Guide](https://github.com/trello/trellisheets/blob/master/styleguide.md) naming conventions.

We are using the [Bourbon stack](bourbon.io) as our CSS framework.

### Organization

Instead of one monolithic stylesheet, each component should have its own `styles.css` which  it requires in it’s main module. This approach eases maintainability, as each react component has its own stylesheet, and webpack will only package up CSS for the components we actually use.

React components should be named with semantic, specific names. However, the CSS classes used for a React component should be as generic as possible.

Prefer using an existing component class name with a new `mod-` modifier to specify the behavior of your component versus adding a new css class per react component.

For example, it is better to have one `btn` class that has a different `mod-foo` modifier for the `FooButton` react component, than make a `foo-button` class.

See the Trello CSS guide for more info.


## DB

The database is postgres and is preconfigured to run in Docker.

To connect via a postgres client:
* Host: 127.0.0.1
* Port: 5432
* Username: root
* No Password 

Database names:
* `development`
* `test`

* To start: `docker-compose up` and leave running
* To create dev/test databases: `yarn db:create`
* To run psql shell against development DB: `yarn db:run -- development`
