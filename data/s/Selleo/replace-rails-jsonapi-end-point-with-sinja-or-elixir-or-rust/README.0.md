Examples here prove that, ruby, and rails overhead is not so big, you can serve decent request below 5ms.
You have to take responsibility for the way you desing your app (data structure, the way you fetch data).

Still for horizontal scaling (handling peak loads) you have to go beyond the scope of optimizing just your ruby code and database (server architecture, balancing, caching, etc). 

# Rails is fast enough for serving API

* use only parts of the rails you really need
* for JSONAPI you ApplicationController should inherit from JSONAPI::ResourceControllerMetal
* reduce number of ActiveRecord objects (by using database views)

# When Rails is not fast enough 

* rewrite only heavy loaded end points (use reverse proxy to keep working two together)
* technology to write the service might be:
    * sinatra + sinja + sequel [yes]
    * elixir + plug [pending]
    * rust + nickel [pending]

# Slides from Lightning talk from WrocLoveRb

http://slides.com/michalczyz/ruby-is-fast-enought-serving-jsonapi-at-speed#/

# How we Benchmark 

````
ab -n 10000 -c 1 -k \
  -H "Content-type: application/json" \
  -H "Accept: application/vnd.api+json" \
  http://0.0.0.0:3000/mail-logs
````  # PlugBench

**TODO: Add description**

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `plug_bench` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [{:plug_bench, "~> 0.1.0"}]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at [https://hexdocs.pm/plug_bench](https://hexdocs.pm/plug_bench).

Guardian
========

An authentication framework for use with Elixir applications.

Guardian is based on similar ideas to Warden but is re-imagined
for modern systems where Elixir manages the authentication requirements.

Guardian remains a functional system. It integrates with Plug, but can be used
outside of it. If you're implementing a TCP/UDP protocol directly, or want to
utilize your authentication via channels, Guardian is your friend.

The core currency of authentication in Guardian is [JSON Web Tokens](https://jwt.io/) (JWT). You can use the JWT to
authenticate web endpoints, channels, and TCP sockets and it can contain any
authenticated assertions that the issuer wants to include.

## Useful articles

If you are very new to Guardian, you'll find the "Simple Guardian" series of articles useful:

* [Simple Guardian - Browser login](http://blog.overstuffedgorilla.com/simple-guardian/)
* [Simple Guardian - API authentication](http://blog.overstuffedgorilla.com/simple-guardian-api-authentication/)
* [Simple Guardian - Permissions](http://blog.overstuffedgorilla.com/simple-guardian-permissions/)
* [Simple Guardian - Multiple Sessions](http://blog.overstuffedgorilla.com/simple-guardian-multiple-sessions/)

## Installation

Add Guardian to your application

mix.exs

```elixir
defp deps do
  [
    # ...
    {:guardian, "~> 0.14"}
    # ...
  ]
end
```

config.exs

```elixir
config :guardian, Guardian,
  allowed_algos: ["HS512"], # optional
  verify_module: Guardian.JWT,  # optional
  issuer: "MyApp",
  ttl: { 30, :days },
  allowed_drift: 2000,
  verify_issuer: true, # optional
  secret_key: <guardian secret key>,
  serializer: MyApp.GuardianSerializer
```

The items in the configuration allow you to tailor how the JWT generation behaves.

* `allowed_algos` - The list of algorithms (must be compatible with JOSE). The first is used as the encoding key. Default is: ["HS512"]
* `verify_module` - Provides a mechanism to setup your own validations for items
  in the token. Default is `Guardian.JWT`
* `issuer` - The entry to put into the token as the issuer. This can be used in conjunction with `verify_issuer`
* `ttl` - The default ttl of a token
* `allowed_drift` - The allowable drift in miliseconds to allow for time fields. Allows for dealing with clock skew
* `verify_issuer` - If set to true, the issuer will be verified to be the same issuer as specified in the `issuer` field
* `secret_key` - The key to sign the tokens. See below for examples.
* `serializer` The serializer that serializes the 'sub' (Subject) field into and out of the token.

## Secret Key

By specifying a binary, the default behavior is to treat the key as an [`"oct"`](https://tools.ietf.org/html/rfc7518#section-6.4) key type (short for octet sequence). This key type may be used with the `"HS256"`, `"HS384"`, and `"HS512"` signature algorithms.

Alternatively, a `Map`, `Function`, or `%JOSE.JWK{} Struct` may be specified for other key types. A full list of example key types is available [here](https://gist.github.com/potatosalad/925a8b74d85835e285b9).

See the [key generation docs](https://hexdocs.pm/jose/key-generation.html) from jose for how to generate your own keys.

```elixir
## Map ##

config :guardian, Guardian,
  allowed_algos: ["ES512"],
  secret_key: %{
    "crv" => "P-521",
    "d" => "axDuTtGavPjnhlfnYAwkHa4qyfz2fdseppXEzmKpQyY0xd3bGpYLEF4ognDpRJm5IRaM31Id2NfEtDFw4iTbDSE",
    "kty" => "EC",
    "x" => "AL0H8OvP5NuboUoj8Pb3zpBcDyEJN907wMxrCy7H2062i3IRPF5NQ546jIJU3uQX5KN2QB_Cq6R_SUqyVZSNpIfC",
    "y" => "ALdxLuo6oKLoQ-xLSkShv_TA0di97I9V92sg1MKFava5hKGST1EKiVQnZMrN3HO8LtLT78SNTgwJSQHAXIUaA-lV"
  }

## Tuple ##
# If, for example, you have your secret key stored externally (in this example, we're using Redix).

# defined elsewhere
defmodule MySecretKey do
  def fetch do
    # Bad practice for example purposes only.
    # An already established connection should be used and possibly cache the value locally.
    {:ok, conn} = Redix.start_link
    rsa_jwk = conn
      |> Redix.command!(["GET my-rsa-key"])
      |> JOSE.JWK.from_binary
    Redix.stop(conn)
    rsa_jwk
  end
end

config :guardian, Guardian,
  allowed_algos: ["RS512"],
  secret_key: {MySecretKey, :fetch}

## %JOSE.JWK{} Struct ##
# Useful if you store your secret key in an encrypted JSON file with the passphrase in an environment variable.

# defined elsewhere
defmodule MySecretKey do
  def fetch do
    System.get_env("SECRET_KEY_PASSPHRASE") |> JOSE.JWK.from_file(System.get_env("SECRET_KEY_FILE"))
  end
end

config :guardian, Guardian,
  allowed_algos: ["Ed25519"],
  secret_key: {MySecretKey, :fetch}
```

## Serializer

The serializer knows how to encode and decode your resource into and out of the
token. A simple serializer:

```elixir
defmodule MyApp.GuardianSerializer do
  @behaviour Guardian.Serializer

  alias MyApp.Repo
  alias MyApp.User

  def for_token(user = %User{}), do: { :ok, "User:#{user.id}" }
  def for_token(_), do: { :error, "Unknown resource type" }

  def from_token("User:" <> id), do: { :ok, Repo.get(User, id) }
  def from_token(_), do: { :error, "Unknown resource type" }
end
```

## Plug API

Guardian ships with some plugs to help integrate into your application.

### Guardian.Plug.VerifySession

Looks for a token in the session. Useful for browser sessions.
If one is not found, this does nothing.

### Guardian.Plug.VerifyHeader

Looks for a token in the Authorization header. Useful for apis.
If one is not found, this does nothing.

### Guardian.Plug.EnsureAuthenticated

Looks for a previously verified token. If one is found, continues, otherwise it
will call the `:unauthenticated` function of your handler.

When you ensure a session, you must declare an error handler. This can be done
as part of a pipeline or inside a Phoenix controller.

```elixir
defmodule MyApp.MyController do
  use MyApp.Web, :controller

  plug Guardian.Plug.EnsureAuthenticated, handler: MyApp.MyAuthErrorHandler
end
```

The failure function must receive the connection, and the connection params.

### Guardian.Plug.LoadResource

Up to now the other plugs have been just looking for valid tokens in various
places or making sure that the token has the correct permissions.

The `LoadResource` plug looks in the `sub` field of the token, fetches the
resource from the Serializer and makes it available via
`Guardian.Plug.current_resource(conn)`.

Note that this does _not ensure_ a resource will be loaded.
If there is no available resource (because it could not be found)
`current_resource` will return nil. You can ensure it's loaded with
`Guardian.Plug.EnsureResource`

### Guardian.Plug.EnsureResource

Looks for a previously loaded resource. If not found, the `:no_resource`
function is called on your handler.

```elixir
defmodule MyApp.MyController do
  use MyApp.Web, :controller

  plug Guardian.Plug.EnsureResource, handler: MyApp.MyAuthErrorHandler
end
```

### Guardian.Plug.EnsurePermissions

Looks for a previously verified token. If one is found, confirms that all listed
permissions are present in the token. If not, the `:unauthorized` function is called on your handler.

```elixir
defmodule MyApp.MyController do
  use MyApp.Web, :controller

  plug Guardian.Plug.EnsurePermissions, handler: MyApp.MyAuthErrorHandler, default: [:read, :write]
end
```

When permissions' sets are specified through a `:one_of` map, the token is searched for at least one
matching permissions set to allow the request. The first set that matches will allow the request.
If no set matches, the `:unauthorized` function is called.

```elixir
defmodule MyApp.MyController do
  use MyApp.Web, :controller

  plug Guardian.Plug.EnsurePermissions, handler: MyApp.MyAuthErrorHandler,
    one_of: [%{default: [:read, :write]}, %{other: [:read]}]
end
```

### Pipelines

These plugs can be used to construct pipelines in Phoenix.

```elixir
pipeline :browser_session do
  plug Guardian.Plug.VerifySession
  plug Guardian.Plug.LoadResource
end

pipeline :api do
  plug :accepts, ["json"]
  plug Guardian.Plug.VerifyHeader
  plug Guardian.Plug.LoadResource
end

scope "/", MyApp do
  pipe_through [:browser, :browser_session] # Use the default browser stack
  # ...
end

scope "/api", MyApp.Api do
  pipe_through [:api] # Use the default browser stack
end
```

From here, you can either EnsureAuthenticated in your pipeline, or on a per-controller basis.

```elixir
defmodule MyApp.MyController do
  use MyApp.Web, :controller

  plug Guardian.Plug.EnsureAuthenticated, handler: MyApp.MyAuthHandler
end
```

## Sign in and Sign out

It's up to you how you generate the claims to encode into the token Guardian uses.
As an example, here are the important parts of a SessionController

```elixir
defmodule MyApp.SessionController do
  use MyApp.Web, :controller

  alias MyApp.User
  alias MyApp.UserQuery

  plug :scrub_params, "user" when action in [:create]

  def create(conn, params = %{}) do
    conn
    |> put_flash(:info, "Logged in.")
    |> Guardian.Plug.sign_in(verified_user) # verify your logged in resource
    |> redirect(to: user_path(conn, :index))
  end

  def delete(conn, _params) do
    Guardian.Plug.sign_out(conn)
    |> put_flash(:info, "Logged out successfully.")
    |> redirect(to: "/")
  end
end
```

### Guardian.Plug.sign\_in

You can sign in with a resource (that the serializer knows about)

```elixir
Guardian.Plug.sign_in(conn, user) # Sign in with the default storage
```

```elixir
Guardian.Plug.sign_in(conn, user, :access, claims)  # give some claims to used for the token jwt

Guardian.Plug.sign_in(conn, user, :access, key: :secret)  # create a token in the :secret location
```

To attach permissions to the token, use the `:perms` key and pass it a map.
Note. To add permissions, you should configure them in your guardian config.

```elixir
Guardian.Plug.sign_in(conn, user, :access, perms: %{ default: [:read, :write], admin: [:all] })

Guardian.Plug.sign_in(conn, user, :access, key: :secret, perms: %{ default: [:read, :write], admin: [:all]})  # create a token in the :secret location
```

### Guardian.Plug.sign\_out

```elixir
Guardian.Plug.sign_out(conn) # Sign out everything (clear session)
```

```elixir
Guardian.Plug.sign_out(conn, :secret) # Clear the token and associated user from the 'secret' location
```

### Current resource, token and claims

Access to the current resource, token and claims is useful. Note, you'll need to
have run the VerifySession/Header for token and claim access, and LoadResource to access the resource.

```elixir
Guardian.Plug.claims(conn) # Access the claims in the default location
Guardian.Plug.claims(conn, :secret) # Access the claims in the secret location
```

```elixir
Guardian.Plug.current_token(conn) # access the token in the default location
Guardian.Plug.current_token(conn, :secret) # access the token in the secret location
```

For the resource

```elixir
Guardian.Plug.current_resource(conn) # Access the loaded resource in the default location
Guardian.Plug.current_resource(conn, :secret) # Access the loaded resource in the secret location
```

### Without Plug

There are many instances where Plug might not be in use. Channels, and raw
sockets for e.g. If you need to do things your own way.

```elixir
{ :ok, jwt, encoded_claims } = Guardian.encode_and_sign(resource, <token_type>, claims_map)
```

This will give you a new JWT to use with the claims ready to go.
The token type is encoded into the JWT as the 'typ' field and is intended to be
used as the _type_ of "access".

```elixir
{ :ok, jwt, full_claims } = Guardian.encode_and_sign(resource, :access)
```

Add some permissions

```elixir
{ :ok, jwt, full_claims } = Guardian.encode_and_sign(resource, :access, perms: %{ default: [:read, :write], admin: Guardian.Permissions.max})
```

Currently suggested token types are:

* `"access"` - Use for API or CORS access. These are basic tokens.

You can also customize the claims you're asserting.

```elixir
claims = Guardian.Claims.app_claims
         |> Map.put("some_claim", some_value)
         |> Guardian.Claims.ttl({3, :days})

{ :ok, jwt, full_claims } = Guardian.encode_and_sign(resource, :access, claims)
```

To verify the token:

```elixir
case Guardian.decode_and_verify(jwt) do
  { :ok, claims } -> do_things_with_claims(claims)
  { :error, reason } -> do_things_with_an_error(reason)
end
```

Accessing the resource from a set of claims:

```elixir
case Guardian.serializer.from_token(claims["sub"]) do
  { :ok, resource } -> do_things_with_resource(resource)
  { :error, reason } -> do_things_without_a_resource(reason)
end
```

### Permissions

Guardian includes support for including permissions. Declare your permissions in
your configuration. All known permissions must be included.

```elixir
config :guardian, Guardian,
       permissions: %{
         default: [:read, :write],
         admin: [:dashboard, :reconcile]
       }
```

JWTs need to be kept reasonably small so that they can fit into an authorization
header. For this reason, permissions are encoded as bits (an integer) in the
token. You can have up to 64 permissions per set, and as many sets as you like.
In the example above, we have the `:default` set, and the `:admin` set.

The bit value of the permissions within a set is determined by it's position in
the config.

```elixir
# Fetch permissions from the claims map

Guardian.Permissions.from_claims(claims, :default)
Guardian.Permissions.from_claims(claims, :admin)

# Check the permissions for all present

Guardian.Permissions.from_claims(claims, :default) |> Guardian.Permissions.all?([:read, :write], :default)
Guardian.Permissions.from_claims(claims, :admin) |> Guardian.Permissions.all?([:reconcile], :admin)

# Check for any permissions
Guardian.Permissions.from_claims(claims, :default) |> Guardian.Permissions.any?([:read, :write], :default)
Guardian.Permissions.from_claims(claims, :admin) |> Guardian.Permissions.any?([:reconcile, :dashboard], :admin)
```

You can use a plug to ensure permissions are present. See Guardian.Plug.EnsurePermissions

#### Setting permissions

When you generate (or sign in) a token, you can inject permissions into it.

```elixir
Guardian.encode_and_sign(resource, :access, perms: %{ admin: [:dashboard], default: Guardian.Permissions.max}})
```

By setting a permission using Guardian.Permission.max you're setting all the bits, so even if new permissions are added, they will be set.

You can similarly pass a `:perms` key to the sign\_in method to have the
permissions encoded into the token.

### Hooks

Often you'll need to take action on some event within the lifecycle of
authentication. Recording logins etc. Guardian provides hooks to allow you to do
this. Use the Guardian.Hooks module to setup. Default implementations are
available for all callbacks.

```elixir
defmodule MyApp.GuardianHooks do
  use Guardian.Hooks

  def after_sign_in(conn, location) do
    user = Guardian.Plug.current_resource(conn, location)
    IO.puts("SIGNED INTO LOCATION WITH: #{user.email}")
    conn
  end
end
```

By default, JWTs are not tracked. This means that after 'logout' the token can
still be used if it is stored outside the system. This is because Guardian does
not track tokens and only interprets them live. When using Guardian in this
way, be sure you consider the expiry time as this is one of the few options you
have to make your tokens invalid.

If you want more control over this you should implement a hook that tracks the
tokens in some storage. When calling `Guardian.revoke!` (called automatically
with sign\_out).

To keep track of all tokens and ensure they're revoked on sign out you can use
[GuardianDb](https://github.com/hassox/guardian_db). This is a simple
Guardian.Hooks module that implements database integration.

    config :guardian, Guardian,
           hooks: GuardianDb

    config :guardian_db, GuardianDb, repo: MyRepo

Configure Guardian to know which module to use.

```elixir
config :guardian, Guardian,
       hooks: MyApp.GuardianHooks,
       #…
```

### Refreshing Tokens

You can use Guardian to refresh tokens. This keeps most of the information in
the token intact, but changes the `iat`, `exp`, `jti` and `nbf` fields.
A valid token must be used in order to be refreshed,
see [Refresh Tokens](###Refresh Tokens) for information on how to refresh invalid tokens

```elixir
case Guardian.refresh!(existing_jwt, existing_claims, %{ttl: {15, :days}}) do
  {:ok, new_jwt, new_claims} -> do_things(new_jwt)
  {:error, reason} -> handle_error(reason)
end
```

Once the new token is created, the old one is revoked before returning the new
token.

### Exhange Tokens

You can exchange one type of token to an other given that the first is valid
This can be used to issue long living tokens that can be exchanged for shorter living ones

```elixir
    # issue a long living refresh token
    {:ok, jwt, claims} = Guardian.encode_and_sign(resource, "refresh")
    # exchange the refresh token for a access token
    {:ok, access_jwt, new_claims} = Guardian.exchange(jwt, "refresh", "access")
```


The old token wont be revoked after the exchange

```elixir
    # issue a long living refresh token
    {:ok, jwt, claims} = Guardian.encode_and_sign(resource, "refresh")
    # exchange the refresh token for a access token
    {:ok, new_jwt, new_claims} = Guardian.exchange!(jwt)
```


### Phoenix Controllers

Guardian provides some helpers for you to use with your controllers.

Provides a simple helper to provide easier access to the current user and their claims.

```elixir
defmodule MyApp.MyController do
  use MyApp.Web, :controller
  use Guardian.Phoenix.Controller

  def index(conn, params, user, claims) do
    # do stuff in here
  end
end
```

You can specify the key location of the user if you're using multiple locations to store users.

```elixir
defmodule MyApp.MyController do
  use MyApp.Web, :controller
  use Guardian.Phoenix.Controller, key: :secret

  def index(conn, params, user, claims) do
  # do stuff with the secret user
  end
end
```

### Phoenix Sockets

Guardian provides integration into the Phoenix channels API to provide
authentication. You can choose to authenticate either on `connect` or every time
someone joins a topic.

To authenticate the initial connect there's a couple of options.

1. Automatically authenticate
2. Authenticate with more control manually.

To automatically authenticate `use` the Guardian.Phoenix.Socket module in your
socket.

```elixir
defmodule MyApp.UsersSocket do
  use Phoenix.Socket
  use Guardian.Phoenix.Socket

  def connect(_params, socket) do
    # if we get here, we did not authenticate
    :error
  end
end
```

Connection authentication requires a `guardian_token` parameter to be provided
which is the JWT. If this is present, Guardian.Phoenix.Socket will authenticate
the connection and carry on or return an `:error` and not allow the connection.

On the javascript side provide your token when you connect.

```javascript
let socket = new Socket("/ws");
socket.connect({guardian_token: jwt});
```

This works fine when all connections should be authenticated. In the case where
you want some of them to be, you can manually sign in.

```elixir
defmodule MyApp.UsersSocket do
  use Phoenix.Socket
  import Guardian.Phoenix.Socket

  def connect(%{"guardian_token" => jwt} = params, socket) do
    case sign_in(socket, jwt) do
      {:ok, authed_socket, guardian_params} ->
        {:ok, authed_socket}
      _ ->
        #unauthenticated socket
        {:ok, socket}
    end
  end

  def connect(_params, socket) do
    # handle unauthenticated connection
  end
end
```

Once you have an authenticated socket you can get the information from it:

```elixir
claims = Guardian.Phoenix.Socket.current_claims(socket)
jwt = Guardian.Phoenix.Socket.current_token(socket)
user = Guardian.Phoenix.Socket.current_resource(socket)
```

If you need even more control, you can use the helpers provided by
Phoenix.Guardian.Socket inside your Channel.

### Phoenix Channels

We can use the Guardian.Phoenix.Socket module to help authenticate channels.

```elixir
defmodule MyApp.UsersChannel do
  use Phoenix.Channel
  import Guardian.Phoenix.Socket

  def join(_room, %{"guardian_token" => token}, socket) do
    case sign_in(socket, token) do
      {:ok, authed_socket, _guardian_params} ->
        {:ok, %{message: "Joined"}, authed_socket}
      {:error, reason} ->
        # handle error
    end
  end

  def join(room, _, socket) do
    {:error,  :authentication_required}
  end

  def handle_in("ping", _payload, socket) do
    user = current_resource(socket)
    broadcast(socket, "pong", %{message: "pong", from: user.email})
    {:noreply, socket}
  end
end
```

Guardian picks up on joins that have been made and automatically verifies the
token and makes available the claims and resource making the request.

```javascript
let socket = new Socket("/ws");
socket.connect();
let guardianToken = jQuery('meta[name="guardian_token"]').attr('content');
let chan = socket.chan("pings", { guardian_token: guardianToken });
```

How to get the tokens onto the page?

```eex
<%= if Guardian.Plug.current_token(@conn) do %>
  <meta name='guardian_token' content="<%= Guardian.Plug.current_token(@conn) %>">
<% end %>
```

# Acknowledgements

Many thanks to Sonny Scroggin (@scrogson) for the name Guardian and great
feedback to get up and running.

### TODO

- [x] Flexible serialization
- [x] Integration with Plug
- [x] Basic integrations like raw TCP
- [x] Service2Service credentials. That is, pass the authentication results through many downstream requests.
- [x] Integration with Phoenix channels
- [x] Integrated permission sets
- [x] Hooks into the authentication cycle
- [x] Revoke tokens
- [x] Refresh tokens
Base64Url
==============

[![Hex.pm](https://img.shields.io/hexpm/v/base64url.svg)](https://hex.pm/packages/base64url)

Standalone [URL safe](http://tools.ietf.org/html/rfc4648) base64-compatible codec.

Usage
--------------

URL-Safe base64 encoding:
```erlang
base64url:encode(<<255,127,254,252>>).
<<"_3_-_A">>
base64url:decode(<<"_3_-_A">>).
<<255,127,254,252>>
```

Vanilla base64 encoding:
```erlang
base64:encode(<<255,127,254,252>>).
<<"/3/+/A==">>
```

Some systems in the wild use base64 URL encoding, but keep the padding for MIME compatibility (base64 Content-Transfer-Encoding). To interact with such systems, use:
```erlang
base64url:encode_mime(<<255,127,254,252>>).
<<"_3_-_A==">>
base64url:decode(<<"_3_-_A==">>).
<<255,127,254,252>>
```

Thanks
--------------

To authors of [this](https://github.com/basho/riak_control/blob/master/src/base64url.erl) and [this](https://github.com/mochi/mochiweb/blob/master/src/mochiweb_base64url.erl).

[License](base64url/blob/master/LICENSE.txt)
-------

Copyright (c) 2013 Vladimir Dronnikov <dronnikov@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Poolboy - A hunky Erlang worker pool factory

[![Build Status](https://api.travis-ci.org/devinus/poolboy.svg?branch=master)](https://travis-ci.org/devinus/poolboy)

[![Support via Gratipay](https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png)](https://gratipay.com/devinus/)

Poolboy is a **lightweight**, **generic** pooling library for Erlang with a
focus on **simplicity**, **performance**, and **rock-solid** disaster recovery.

## Usage

```erl-sh
1> Worker = poolboy:checkout(PoolName).
<0.9001.0>
2> gen_server:call(Worker, Request).
ok
3> poolboy:checkin(PoolName, Worker).
ok
```

## Example

This is an example application showcasing database connection pools using
Poolboy and [epgsql](https://github.com/epgsql/epgsql).

### example.app

```erlang
{application, example, [
    {description, "An example application"},
    {vsn, "0.1"},
    {applications, [kernel, stdlib, sasl, crypto, ssl]},
    {modules, [example, example_worker]},
    {registered, [example]},
    {mod, {example, []}},
    {env, [
        {pools, [
            {pool1, [
                {size, 10},
                {max_overflow, 20}
			], [
                {hostname, "127.0.0.1"},
                {database, "db1"},
                {username, "db1"},
                {password, "abc123"}
            ]},
            {pool2, [
                {size, 5},
                {max_overflow, 10}
			], [
                {hostname, "127.0.0.1"},
                {database, "db2"},
                {username, "db2"},
                {password, "abc123"}
            ]}
        ]}
    ]}
]}.
```

### example.erl

```erlang
-module(example).
-behaviour(application).
-behaviour(supervisor).

-export([start/0, stop/0, squery/2, equery/3]).
-export([start/2, stop/1]).
-export([init/1]).

start() ->
    application:start(?MODULE).

stop() ->
    application:stop(?MODULE).

start(_Type, _Args) ->
    supervisor:start_link({local, example_sup}, ?MODULE, []).

stop(_State) ->
    ok.

init([]) ->
    {ok, Pools} = application:get_env(example, pools),
    PoolSpecs = lists:map(fun({Name, SizeArgs, WorkerArgs}) ->
        PoolArgs = [{name, {local, Name}},
            		{worker_module, example_worker}] ++ SizeArgs,
        poolboy:child_spec(Name, PoolArgs, WorkerArgs)
    end, Pools),
    {ok, {{one_for_one, 10, 10}, PoolSpecs}}.

squery(PoolName, Sql) ->
    poolboy:transaction(PoolName, fun(Worker) ->
        gen_server:call(Worker, {squery, Sql})
    end).

equery(PoolName, Stmt, Params) ->
    poolboy:transaction(PoolName, fun(Worker) ->
        gen_server:call(Worker, {equery, Stmt, Params})
    end).
```

### example_worker.erl

```erlang
-module(example_worker).
-behaviour(gen_server).
-behaviour(poolboy_worker).

-export([start_link/1]).
-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2,
         code_change/3]).

-record(state, {conn}).

start_link(Args) ->
    gen_server:start_link(?MODULE, Args, []).

init(Args) ->
    process_flag(trap_exit, true),
    Hostname = proplists:get_value(hostname, Args),
    Database = proplists:get_value(database, Args),
    Username = proplists:get_value(username, Args),
    Password = proplists:get_value(password, Args),
    {ok, Conn} = epgsql:connect(Hostname, Username, Password, [
        {database, Database}
    ]),
    {ok, #state{conn=Conn}}.

handle_call({squery, Sql}, _From, #state{conn=Conn}=State) ->
    {reply, epgsql:squery(Conn, Sql), State};
handle_call({equery, Stmt, Params}, _From, #state{conn=Conn}=State) ->
    {reply, epgsql:equery(Conn, Stmt, Params), State};
handle_call(_Request, _From, State) ->
    {reply, ok, State}.

handle_cast(_Msg, State) ->
    {noreply, State}.

handle_info(_Info, State) ->
    {noreply, State}.

terminate(_Reason, #state{conn=Conn}) ->
    ok = epgsql:close(Conn),
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.
```

## Options

- `name`: the pool name
- `worker_module`: the module that represents the workers
- `size`: maximum pool size
- `max_overflow`: maximum number of workers created if pool is empty
- `strategy`: `lifo` or `fifo`, determines whether checked in workers should be
  placed first or last in the line of available workers. Default is `lifo`.

## Authors

- Devin Torres (devinus) <devin@devintorres.com>
- Andrew Thompson (Vagabond) <andrew@hijacked.us>
- Kurt Williams (onkel-dirtus) <kurt.r.williams@gmail.com>

## License

Poolboy is available in the public domain (see `UNLICENSE`).
Poolboy is also optionally available under the ISC license (see `LICENSE`),
meant especially for jurisdictions that do not recognize public domain works.
# Postgrex

[![Build Status](https://travis-ci.org/elixir-ecto/postgrex.svg?branch=master)](https://travis-ci.org/elixir-ecto/postgrex)

PostgreSQL driver for Elixir.

Documentation: http://hexdocs.pm/postgrex/

## Example

```iex
iex> {:ok, pid} = Postgrex.start_link(hostname: "localhost", username: "postgres", password: "postgres", database: "postgres")
{:ok, #PID<0.69.0>}
iex> Postgrex.query!(pid, "SELECT user_id, text FROM comments", [])
%Postgrex.Result{command: :select, empty?: false, columns: ["user_id", "text"], rows: [[3,"hey"],[4,"there"]], size: 2}}
iex> Postgrex.query!(pid, "INSERT INTO comments (user_id, text) VALUES (10, 'heya')", [])
%Postgrex.Result{command: :insert, columns: nil, rows: nil, num_rows: 1}}
```

## Features

  * Automatic decoding and encoding of Elixir values to and from PostgreSQL's binary format
  * User defined extensions for encoding and decoding any PostgreSQL type
  * Supports transactions, prepared queries and multiple pools via [DBConnection](https://github.com/elixir-ecto/db_connection)
  * Supports PostgreSQL 8.4 and 9.0-9.6 (hstore is not supported on 8.4)

## Data representation

    PostgreSQL      Elixir
    ----------      ------
    NULL            nil
    bool            true | false
    char            "é"
    int             42
    float           42.0
    text            "eric"
    bytea           <<42>>
    numeric         #Decimal<42.0> *
    date            %Postgrex.Date{year: 2013, month: 10, day: 12}
    time(tz)        %Postgrex.Time{hour: 0, min: 37, sec: 14, usec: 0} **
    timestamp(tz)   %Postgrex.Timestamp{year: 2013 month: 10, day: 12, hour: 0, min: 37, sec: 14, usec: 0} **
    interval        %Postgrex.Interval{months: 14, days: 40, secs: 10920}
    array           [1, 2, 3]
    composite type  {42, "title", "content"}
    range           %Postgrex.Range{lower: 1, upper: 5}
    uuid            <<160,238,188,153,156,11,78,248,187,109,107,185,189,56,10,17>>
    hstore          %{"foo" => "bar"}
    oid types       42
    enum            "ok" ***
    bit             << 1::1, 0::1 >>
    varbit          << 1::1, 0::1 >>
    tsvector        [%Postgrex.Lexeme{positions: [{1, :A}], word: "a"}]

\* [Decimal](http://github.com/ericmj/decimal)

\*\* Timezones will always be normalized to UTC or assumed to be UTC when no information is available, either by PostgreSQL or Postgrex

\*\*\* Enumerated types (enum) are custom named database types with strings as values.

Postgrex does not automatically cast between types. For example, you can't pass a string where a date is expected. To add type casting, support new types, or change how any of the types above are encoded/decoded, you can use extensions.

## Extensions

Extensions are used to extend Postgrex' built-in type encoding/decoding.

Here is a [JSON extension](https://github.com/elixir-ecto/postgrex/blob/master/lib/postgrex/extensions/json.ex) that supports encoding/decoding Elixir maps to the Postgres' JSON type.

Extensions can be specified and configured when building custom type modules. For example, if you want to different a JSON encoder/decode, you can define a new type module as below.

```elixir
# Postgrex.Types.define(module_name, extra_extensions, options)
Postgrex.Types.define(MyApp.PostgrexTypes, [], json: AnotherJSONLib)
```

`Postgrex.Types.define/3` must be called on its own file, outside of any module and function, as it only needs to be defined once during compilation.

Once a type module is defined, you must specify it on `start_link`:

```elixir
Postgrex.start_link(types: MyApp.PostgrexTypes)
```

## OID type encoding

PostgreSQL's wire protocol supports encoding types either as text or as binary. Unlike most client libraries Postgrex uses the binary protocol, not the text protocol. This allows for efficient encoding of types (e.g. 4-byte integers are encoded as 4 bytes, not as a string of digits) and automatic support for arrays and composite types.

Unfortunately the PostgreSQL binary protocol transports [OID types](http://www.postgresql.org/docs/current/static/datatype-oid.html#DATATYPE-OID-TABLE) as integers while the text protocol transports them as string of their name, if one exists, and otherwise as integer.

This means you either need to supply oid types as integers or perform an explicit cast (which would be automatic when using the text protocol) in the query.

```elixir
# Fails since $1 is regclass not text.
query("select nextval($1)", ["some_sequence"])

# Perform an explicit cast, this would happen automatically when using a
# client library that uses the text protocol.
query("select nextval($1::text::regclass)", ["some_sequence"])

# Determine the oid once and store it for later usage. This is the most
# efficient way, since PostgreSQL only has to perform the lookup once. Client
# libraries using the text protocol do not support this.
%{rows: [{sequence_oid}]} = query("select $1::text::regclass", ["some_sequence"])
query("select nextval($1)", [sequence_oid])
```

## PgBouncer

When using PgBouncer with transaction or statement pooling named prepared
queries can not be used because the bouncer may route requests from the same
postgrex connection to different PostgreSQL backend processes and discards named
queries after the transactions closes. To force unnamed prepared queries:

```elixir
Postgrex.start_link(prepare: :unnamed)
```

## Contributing

To contribute you need to compile Postgrex from source and test it:

```
$ git clone https://github.com/elixir-ecto/postgrex.git
$ cd postgrex
$ mix test
```

The tests requires some modifications to your [hba file](http://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html). The path to it can be found by running `$ psql -U postgres -c "SHOW hba_file"` in your shell. Put the following above all other configurations (so that they override):

```
host    all             postgrex_md5_pw         127.0.0.1/32    md5
host    all             postgrex_cleartext_pw   127.0.0.1/32    password
```

The server needs to be restarted for the changes to take effect. Additionally you need to setup a Postgres user with the same username as the local user and give it trust or ident in your hba file. Or you can export $PGUSER and $PGPASSWORD before running tests.

### Testing hstore on 9.0

Postgres versions 9.0 does not have the `CREATE EXTENSION` commands. This means we have to locate the postgres installation and run the `hstore.sql` in `contrib` to install `hstore`. Below is an example command to test 9.0 on OS X with homebrew installed postgres:

```
$ PGVERSION=9.0 PGPATH=/usr/local/share/postgresql9/ mix test
```

## License

Copyright 2013 Eric Meadows-Jönsson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# MIME

A library that maps mime types to extensions and vice-versa.

## Installation

The package can be installed as:

1. Add mime to your list of dependencies in `mix.exs`:

  ```elixir
  def deps do
    [{:mime, "~> 1.1"}]
  end
  ```

2. If there is an `applications` key in your `mix.exs`, add `:mime` to the list. This step is not necessary if you have `extra_applications` instead.

  ```elixir
  def application do
    [applications: [:mime]]
  end
  ```
  
## Usage

MIME types can be extended in your application `config/config.exs` as follows:

```elixir
config :mime, :types, %{
  "application/vnd.api+json" => ["json-api"]
}
```

And then run `mix deps.clean --build mime` to force mime to be recompiled across all environments.

## License

MIME source code is released under Apache 2 License.

Check LICENSE file for more information.
# DBConnection

Database connection behaviour and database connection pool designed for
handling transaction, prepare/execute, cursors and client process
describe/encode/decode.

Four pool implementations are provided: `DBConnection.Connection`
(default/single connection), `DBConnection.Poolboy` (poolboy pool),
`DBConnection.Sojourn` (sbroker pool) and `DBConnection.Ownership`
(ownership pool).

Examples of using the `DBConnection` behaviour are available in
`./examples/db_agent/` and `./examples/tcp_connection/`.

## License

Copyright 2015 James Fish

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# Decimal

[![Build Status](https://travis-ci.org/ericmj/decimal.svg?branch=master)](https://travis-ci.org/ericmj/decimal)

Arbitrary precision decimal arithmetic for Elixir.

Documentation: http://hexdocs.pm/decimal/

## Usage

Add Decimal as a dependency in your `mix.exs` file.

```elixir
def deps do
  [{:decimal, "~> 1.0"}]
end
```

After you are done, run `mix deps.get` in your shell to fetch and compile Decimal. Start an interactive Elixir shell with `iex -S mix`.

```elixir
iex> alias Decimal, as: D
nil
iex> D.add(D.new(6), D.new(7))
#Decimal<13>
iex> D.div(D.new(1), D.new(3))
#Decimal<0.333333333>
```

## Examples

### Using the context

The context specifies the maximum precision of the result of calculations and
the rounding algorithm if the result has a higher precision than the specified
maximum. It also holds the list of set of trap enablers and the currently set
flags.

The context is stored in the process dictionary, this means that you don't have
to pass the context around explicitly and the flags will be updated
automatically.

The context is accessed with `Decimal.get_context/0` and set with
`Decimal.set_context/1`. It can also be temporarily set with
`Decimal.with_context/2`.

```elixir
iex> D.get_context
%Decimal.Context{flags: [:rounded, :inexact], precision: 9, rounding: :half_up,
 traps: [:invalid_operation, :division_by_zero]}
iex> D.with_context %D.Context{precision: 2}, fn -> IO.inspect D.get_context end
%Decimal.Context{flags: [], precision: 2, rounding: :half_up,
 traps: [:invalid_operation, :division_by_zero]}
%Decimal.Context{flags: [], precision: 2, rounding: :half_up,
 traps: [:invalid_operation, :division_by_zero]}
iex> D.set_context(%D.Context{D.get_context | traps: []})
:ok
iex> Decimal.get_context
%Decimal.Context{flags: [:rounded, :inexact], precision: 9, rounding: :half_up,
 traps: []}
```

### Precision and rounding

The precision is used to limit the amount of decimal digits in the coefficient:

```elixir
iex> D.set_context(%D.Context{D.get_context | precision: 9})
:ok
iex> D.div(D.new(1), D.new(3))
#Decimal<0.333333333>
iex> D.set_context(%D.Context{D.get_context | precision: 2})
:ok
iex> D.div(D.new(1), D.new(3))
#Decimal<0.33>
```

The rounding algorithm specifies how the result of an operation shall be rounded
when it get be represented with the current precision:

```elixir
iex> D.set_context(%D.Context{D.get_context | rounding: :half_up})
:ok
iex> D.div(D.new(31), D.new(2))
#Decimal<16>
iex> D.set_context(%D.Context{D.get_context | rounding: :floor})
:ok
iex> D.div(D.new(31), D.new(2))
#Decimal<15>
```

### Flags and trap enablers

When an exceptional condition is signalled its flag is set in the context and if
if the trap enabler is set `Decimal.Error` will be raised.

```elixir
iex> D.set_context(%D.Context{D.get_context | rounding: :floor, precision: 2})
:ok
iex> D.get_context.traps
[:invalid_operation, :division_by_zero]
iex> D.get_context.flags
[]
iex> D.div(D.new(31), D.new(2))
#Decimal<15>
iex> D.get_context.flags
[:inexact, :rounded]
```

`:inexact` and `:rounded` were signaled above because the result of the
operation was inexact given the context's precision and had to be rounded to fit
the precision. `Decimal.Error` was not raised because the signals' trap enablers
weren't set. We can, however, set the trap enabler if we what this condition to
raise.

```elixir
iex> D.set_context(%D.Context{D.get_context | traps: D.get_context.traps ++ [:inexact]})
:ok
iex> D.div(D.new(31), D.new(2))
** (Decimal.Error)
```

The default trap enablers, such as `:division_by_zero` can be unset:

```elixir
iex> D.get_context.traps
[:invalid_operation, :division_by_zero]
iex> D.div(D.new(42), D.new(0))
** (Decimal.Error)
iex>  D.set_context(%D.Context{D.get_context | traps: [], flags: []})
:ok
iex> D.div(D.new(42), D.new(0))
#Decimal<Infinity>
iex> D.get_context.flags
[:division_by_zero]
```

### Mitigating rounding errors

TODO

## License

   Copyright 2013 Eric Meadows-Jönsson

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
# Ecto

[![Build Status](https://travis-ci.org/elixir-ecto/ecto.svg?branch=master)](https://travis-ci.org/elixir-ecto/ecto)
[![Inline docs](http://inch-ci.org/github/elixir-ecto/ecto.svg?branch=master&style=flat)](http://inch-ci.org/github/elixir-ecto/ecto)
[![Ebert](https://ebertapp.io/github/elixir-ecto/ecto.svg)](https://ebertapp.io/github/elixir-ecto/ecto)

Ecto is a domain specific language for writing queries and interacting with databases in Elixir. Here is an example:

```elixir
# In your config/config.exs file
config :my_app, ecto_repos: [Sample.Repo]

config :my_app, Sample.Repo,
  adapter: Ecto.Adapters.Postgres,
  database: "ecto_simple",
  username: "postgres",
  password: "postgres",
  hostname: "localhost",
  port: "5432"

# In your application code
defmodule Sample.Repo do
  use Ecto.Repo,
    otp_app: :my_app
end

defmodule Sample.Weather do
  use Ecto.Schema

  schema "weather" do
    field :city     # Defaults to type :string
    field :temp_lo, :integer
    field :temp_hi, :integer
    field :prcp,    :float, default: 0.0
  end
end

defmodule Sample.App do
  import Ecto.Query
  alias Sample.Weather
  alias Sample.Repo

  def keyword_query do
    query = from w in Weather,
         where: w.prcp > 0 or is_nil(w.prcp),
         select: w
    Repo.all(query)
  end

  def pipe_query do
    Weather
    |> where(city: "Kraków")
    |> order_by(:temp_lo)
    |> limit(10)
    |> Repo.all
  end
end
```

See the [getting started guide](http://hexdocs.pm/ecto/getting-started.html) and the [online documentation](http://hexdocs.pm/ecto).

Also checkout the ["What's new in Ecto 2.0"](http://pages.plataformatec.com.br/ebook-whats-new-in-ecto-2-0) free ebook to learn more about many features in Ecto 2.0 such as `many_to_many`, schemaless queries, concurrent testing and more.

## Usage

You need to add both Ecto and the database adapter as a dependency to your `mix.exs` file. The supported databases and their adapters are:

Database   | Ecto Adapter           | Dependency                   | Ecto 2.0 compatible?
:----------| :--------------------- | :----------------------------| :-------------------
PostgreSQL | Ecto.Adapters.Postgres | [postgrex][postgrex]         | Yes
MySQL      | Ecto.Adapters.MySQL    | [mariaex][mariaex]           | Yes
MSSQL      | Tds.Ecto               | [tds_ecto][tds_ecto]         | No
SQLite3    | Sqlite.Ecto            | [sqlite_ecto][sqlite_ecto]   | No
MongoDB    | Mongo.Ecto             | [mongodb_ecto][mongodb_ecto] | No

[postgrex]: http://github.com/ericmj/postgrex
[mariaex]: http://github.com/xerions/mariaex
[tds_ecto]: https://github.com/livehelpnow/tds_ecto
[sqlite_ecto]: https://github.com/jazzyb/sqlite_ecto
[mongodb_ecto]: https://github.com/michalmuskala/mongodb_ecto

For example, if you want to use PostgreSQL, add to your `mix.exs` file:

```elixir
defp deps do
  [{:postgrex, ">= 0.0.0"},
   {:ecto, "~> 2.1"}]
end
```

and update your applications list to include both projects:

```elixir
def application do
  [applications: [:postgrex, :ecto]]
end
```

Then run `mix deps.get` in your shell to fetch the dependencies. If you want to use another database, just choose the proper dependency from the table above.

Finally, in the repository configuration, you will need to specify the `adapter:` respective to the chosen dependency. For PostgreSQL it is:

```elixir
config :my_app, Repo,
  adapter: Ecto.Adapters.Postgres,
  ...
```

We are currently looking for contributions to add support for other SQL databases and folks interested in exploring non-relational databases too.

## Important links

  * [Documentation](http://hexdocs.pm/ecto)
  * [Mailing list](https://groups.google.com/forum/#!forum/elixir-ecto)
  * [Examples](https://github.com/elixir-ecto/ecto/tree/master/examples)

## Contributing

Contributions are welcome! In particular, remember to:

* Do not use the issues tracker for help or support requests (try Stack Overflow, IRC or mailing lists, etc).
* For proposing a new feature, please start a discussion on [elixir-ecto](https://groups.google.com/forum/#!forum/elixir-ecto).
* For bugs, do a quick search in the issues tracker and make sure the bug has not yet been reported.
* Finally, be nice and have fun! Remember all interactions in this project follow the same [Code of Conduct as Elixir](https://github.com/elixir-lang/elixir/blob/master/CODE_OF_CONDUCT.md).

### Running tests

Clone the repo and fetch its dependencies:

```
$ git clone https://github.com/elixir-ecto/ecto.git
$ cd ecto
$ mix deps.get
$ mix test
```

Besides the unit tests above, it is recommended to run the adapter integration tests too:

```
# Run only PostgreSQL tests (PostgreSQL >= 9.5 is preferred for testing all Postgres features)
MIX_ENV=pg mix test

# Run all tests (unit and all adapters)
mix test.all
```

### Building docs

```
$ MIX_ENV=docs mix docs
```

## Copyright and License

Copyright (c) 2012, Plataformatec.

Ecto source code is licensed under the [Apache 2 License](LICENSE.md).
# Plug

[![Build Status](https://travis-ci.org/elixir-lang/plug.svg?branch=master)](https://travis-ci.org/elixir-lang/plug)
[![Inline docs](http://inch-ci.org/github/elixir-lang/plug.svg?branch=master)](http://inch-ci.org/github/elixir-lang/plug)

Plug is:

1. A specification for composable modules between web applications
2. Connection adapters for different web servers in the Erlang VM

[Documentation for Plug is available online](http://hexdocs.pm/plug/).

## Hello world

```elixir
defmodule MyPlug do
  import Plug.Conn

  def init(options) do
    # initialize options

    options
  end

  def call(conn, _opts) do
    conn
    |> put_resp_content_type("text/plain")
    |> send_resp(200, "Hello world")
  end
end
```

The snippet above shows a very simple example on how to use Plug. Save that snippet to a file and run it inside the plug application with:

    $ iex -S mix
    iex> c "path/to/file.ex"
    [MyPlug]
    iex> {:ok, _} = Plug.Adapters.Cowboy.http MyPlug, []
    {:ok, #PID<...>}

Access "http://localhost:4000/" and we are done! For now, we have directly started the server in our terminal but, for production deployments, you likely want to start it in your supervision tree. See the "Supervised handlers" section below.

## Installation

You can use plug in your projects in two steps:

1. Add plug and your webserver of choice (currently cowboy) to your `mix.exs` dependencies:

    ```elixir
    def deps do
      [{:cowboy, "~> 1.0.0"},
       {:plug, "~> 1.0"}]
    end
    ```

2. List both `:cowboy` and `:plug` as your application dependencies:

    ```elixir
    def application do
      [applications: [:cowboy, :plug]]
    end
    ```

## The Plug.Conn

In the hello world example, we defined our first plug. What is a plug after all?

A plug takes two shapes. A function plug receives a connection and a set of options as arguments and returns the connection:

```elixir
def hello_world_plug(conn, _opts) do
  conn
  |> put_resp_content_type("text/plain")
  |> send_resp(200, "Hello world")
end
```

A module plug implements an `init/1` function to initialize the options and a `call/2` function which receives the connection and initialized options and returns the connection:

```elixir
defmodule MyPlug do
  def init([]), do: false
  def call(conn, _opts), do: conn
end
```

As per the specification above, a connection is represented by the `Plug.Conn` struct:

```elixir
%Plug.Conn{host: "www.example.com",
           path_info: ["bar", "baz"],
           ...}
```

Data can be read directly from the connection and also pattern matched on. Manipulating the connection often happens with the use of the functions defined in the `Plug.Conn` module. In our example, both `put_resp_content_type/2` and `send_resp/3` are defined in `Plug.Conn`.

Remember that, as everything else in Elixir, **a connection is immutable**, so every manipulation returns a new copy of the connection:

```elixir
conn = put_resp_content_type(conn, "text/plain")
conn = send_resp(conn, 200, "ok")
conn
```

Finally, keep in mind that a connection is a **direct interface to the underlying web server**. When you call `send_resp/3` above, it will immediately send the given status and body back to the client. This makes features like streaming a breeze to work with.

## The Plug Router

In practice, developers rarely write their own plugs. For example, Plug ships with a router that allows developers to quickly match on incoming requests and perform some action:

```elixir
defmodule MyRouter do
  use Plug.Router

  plug :match
  plug :dispatch

  get "/hello" do
    send_resp(conn, 200, "world")
  end

  forward "/users", to: UsersRouter

  match _ do
    send_resp(conn, 404, "oops")
  end
end
```

The router is a plug and, not only that, it contains its own plug pipeline too. The example above says that when the router is invoked, it will invoke the `:match` plug, represented by a local `match/2` function, and then call the `:dispatch` plug which will execute the matched code.

Plug ships with many plugs that you can add to the router plug pipeline, allowing you to plug something before a route matches or before a route is dispatched to. For example, if you want to add logging to the router, just do:

```elixir
plug Plug.Logger
plug :match
plug :dispatch
```

Note `Plug.Router` compiles all of your routes into a single function and relies on the Erlang VM to optimize the underlying routes into a tree lookup, instead of a linear lookup that would instead match route-per-route. This means route lookups are extremely fast in Plug!

This also means that a catch all `match` is recommended to be defined, as in the example above, otherwise routing fails with a function clause error (as it would in any regular Elixir function).

Each route needs to return the connection as per the Plug specification. See `Plug.Router` docs for more information.

## Supervised handlers

On a production system, you likely want to start your Plug application under your application's supervision tree. Plug provides the `child_spec/3` function to do just that. Start a new Elixir project with the `--sup` flag:

```elixir
$ mix new my_app --sup
```

and then update `lib/my_app.ex` as follows:

```elixir
defmodule MyApp do
  use Application

  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  def start(_type, _args) do
    import Supervisor.Spec

    children = [
      # Define workers and child supervisors to be supervised
      Plug.Adapters.Cowboy.child_spec(:http, MyRouter, [], [port: 4001])
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: MyApp.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

## Testing plugs

Plug ships with a `Plug.Test` module that makes testing your plugs easy. Here is how we can test the router from above (or any other plug):

```elixir
defmodule MyPlugTest do
  use ExUnit.Case, async: true
  use Plug.Test

  @opts AppRouter.init([])

  test "returns hello world" do
    # Create a test connection
    conn = conn(:get, "/hello")

    # Invoke the plug
    conn = AppRouter.call(conn, @opts)

    # Assert the response and status
    assert conn.state == :sent
    assert conn.status == 200
    assert conn.resp_body == "world"
  end
end
```

### Available Plugs

This project aims to ship with different plugs that can be re-used across applications:

  * `Plug.CSRFProtection` - adds Cross-Site Request Forgery protection to your application. Typically required if you are using `Plug.Session`;
  * `Plug.Head` - converts HEAD requests to GET requests;
  * `Plug.Logger` - logs requests;
  * `Plug.MethodOverride` - overrides a request method with one specified in headers;
  * `Plug.Parsers` - responsible for parsing the request body given its content-type;
  * `Plug.RequestId` - sets up a request ID to be used in logs;
  * `Plug.Session` - handles session management and storage;
  * `Plug.SSL` - enforce requests through SSL;
  * `Plug.Static` - serves static files;

You can go into more details about each of them [in our docs](http://hexdocs.pm/plug/).

### Helper modules

Modules that can be used after you use `Plug.Router` or `Plug.Builder` to help development:

  * `Plug.Debugger` - shows a helpful debugging page every time there is a failure in a request;
  * `Plug.ErrorHandler` - allows developers to customize error pages in case of crashes instead of sending a blank one;

## Contributing

We welcome everyone to contribute to Plug and help us tackle existing issues!

Use the [issue tracker][issues] for bug reports or feature requests. You may also start a discussion on the [mailing list][ML] or the **[#elixir-lang][IRC]** channel on [Freenode][freenode] IRC. Open a [pull request][pulls] when you are ready to contribute.

When submitting a pull request you should not update the `CHANGELOG.md`.

If you are planning to contribute documentation, [please check our best practices for writing documentation][writing-docs].

Finally, remember all interactions in our official spaces follow our [Code of Conduct][code-of-conduct].

## License

Plug source code is released under Apache 2 License.
Check LICENSE file for more information.

  [issues]: https://github.com/elixir-lang/plug/issues
  [pulls]: https://github.com/elixir-lang/plug/pulls
  [ML]: https://groups.google.com/group/elixir-lang-core
  [code-of-conduct]: https://github.com/elixir-lang/elixir/blob/master/CODE_OF_CONDUCT.md
  [writing-docs]: http://elixir-lang.org/docs/stable/elixir/writing-documentation.html
  [IRC]: https://webchat.freenode.net/?channels=#elixir-lang
  [freenode]: http://www.freenode.net
Cowlib
======

Cowlib is a support library for manipulating Web protocols.

Goals
-----

Cowlib provides libraries for parsing and building messages
for various Web protocols, including SPDY, HTTP and Websocket.

It is optimized for completeness rather than speed. No value
is ignored, they are all returned.

Support
-------

 *  Official IRC Channel: #ninenines on irc.freenode.net
 *  [Mailing Lists](http://lists.ninenines.eu)
 *  [Commercial Support](http://ninenines.eu/support)
Cowboy
======

Cowboy is a small, fast and modular HTTP server written in Erlang.

Goals
-----

Cowboy aims to provide a **complete** HTTP stack in a **small** code base.
It is optimized for **low latency** and **low memory usage**, in part
because it uses **binary strings**.

Cowboy provides **routing** capabilities, selectively dispatching requests
to handlers written in Erlang.

Because it uses Ranch for managing connections, Cowboy can easily be
**embedded** in any other application.

No parameterized module. No process dictionary. **Clean** Erlang code.

Sponsors
--------

The SPDY implementation was sponsored by
[LeoFS Cloud Storage](http://www.leofs.org).

The project is currently sponsored by
[Kato.im](https://kato.im).

Online documentation
--------------------

 *  [User guide](http://ninenines.eu/docs/en/cowboy/HEAD/guide)
 *  [Function reference](http://ninenines.eu/docs/en/cowboy/HEAD/manual)

Offline documentation
---------------------

 *  While still online, run `make docs`
 *  Function reference man pages available in `doc/man3/` and `doc/man7/`
 *  Run `make install-docs` to install man pages on your system
 *  Full documentation in Markdown available in `doc/markdown/`
 *  Examples available in `examples/`

Getting help
------------

 *  Official IRC Channel: #ninenines on irc.freenode.net
 *  [Mailing Lists](http://lists.ninenines.eu)
 *  [Commercial Support](http://ninenines.eu/support)
= Ranch

Ranch is a socket acceptor pool for TCP protocols.

== Goals

Ranch aims to provide everything you need to accept TCP connections with
a **small** code base and **low latency** while being easy to use directly
as an application or to **embed** into your own.

Ranch provides a **modular** design, letting you choose which transport
and protocol are going to be used for a particular listener. Listeners
accept and manage connections on one port, and include facilities to
limit the number of **concurrent** connections. Connections are sorted
into **pools**, each pool having a different configurable limit.

Ranch also allows you to **upgrade** the acceptor pool without having
to close any of the currently opened sockets.

== Online documentation

* http://ninenines.eu/docs/en/ranch/1.3/guide[User guide]
* http://ninenines.eu/docs/en/ranch/1.3/manual[Function reference]

== Offline documentation

* While still online, run `make docs`
* User guide available in `doc/` in PDF and HTML formats
* Function reference man pages available in `doc/man3/` and `doc/man7/`
* Run `make install-docs` to install man pages on your system
* Full documentation in Asciidoc available in `doc/src/`
* Examples available in `examples/`

== Support

* Official IRC Channel: #ninenines on irc.freenode.net
* https://github.com/ninenines/ranch/issues[Issues tracker]
* http://ninenines.eu/services[Commercial Support]
JaSerializer
============

[![Build Status](https://travis-ci.org/vt-elixir/ja_serializer.svg?branch=master)](https://travis-ci.org/vt-elixir/ja_serializer)
[![Hex Version](https://img.shields.io/hexpm/v/ja_serializer.svg)](https://hex.pm/packages/ja_serializer)
[![Deps Status](https://beta.hexfaktor.org/badge/all/github/vt-elixir/ja_serializer.svg)](https://beta.hexfaktor.org/github/vt-elixir/ja_serializer)
[![Inline docs](http://inch-ci.org/github/vt-elixir/ja_serializer.svg)](http://inch-ci.org/github/vt-elixir/ja_serializer)

jsonapi.org formatting of Elixir data structures suitable for serialization by
libraries such as Poison.

## Questions/Help

Please open an issue or message/mention @alanpeabody in the [Elixir Slack](https://elixir-slackin.herokuapp.com/).

## Usage

See [documentation](http://hexdocs.pm/ja_serializer/) on hexdoc for full
serialization and usage details.

## Installation
Add JaSerializer to your application

mix.deps

```elixir
defp deps do
  [
    # ...
      {:ja_serializer, "~> x.x.x"}
    # ...
  ]
end
```

## Serializer Behaviour and DSL

```elixir
defmodule MyApp.ArticleSerializer do
  use JaSerializer

  location "/articles/:id"
  attributes [:title, :tags, :body, :excerpt]

  has_one :author,
    serializer: PersonSerializer,
    include: true,
    field: :authored_by

  has_many :comments,
    links: [
      related: "/articles/:id/comments",
      self: "/articles/:id/relationships/comments"
    ]

  def comments(article, _conn) do
    Comment.for_article(article)
  end

  def excerpt(article, _conn) do
    [first | _ ] = String.split(article.body, ".")
    first
  end
end
```

### Attributes

Attributes are defined as a list in the serializer module.
The serializer will use the given atom as the key by default.
You can also specify a custom method of attribute retrieval by defining a
<attribute_name>/2 method. The method will be passed the struct
and the connection.

### Relationships

Valid relationships are: `has_one`, `has_many`.
Use `has_one` for `belongs_to` type of relationships.
For each relationship, you can define the name and a variety of options.
Just like attributes, the serializer will use the given atom
to look up the relationship, unless you specify a custom retrieval method
OR provide a `field` option

#### Relationship options

* serializer - The serializer to use when serializing this resource
* include - boolean - true to always side-load this relationship
* field - custom field to use for relationship retrieval
* links - custom links to use in the `relationships` hash

### Direct Usage of Serializer

```elixir
MyApp.ArticleSerializer
|> JaSerializer.format(struct, conn)
|> Poison.encode!
```

### Formatting options

The `format/4` method is able to take in options that can customize the
serialized payload.

#### Include

By specifying the `include` option, the serializer will only side-load
the relationships specified. This option should be a comma separated
list of relationships. Each relationship should be a dot separated path.

Example: `include: "author,comments.author"`

The format of this string should exactly match the one specified by the
[JSON-API spec](http://jsonapi.org/format/#fetching-includes)

Note: If specifying the `include` option, all "default" includes will
be ignored, and only the specified relationships included, per spec.

#### Fields

The `fields` option satisfies the [sparse fieldset](http://jsonapi.org/format/#fetching-sparse-fieldsets) portion of the spec. This options should
be a map of resource types whose value is a comma separated list of fields
to include.

Example: `fields: %{"articles" => "title,body", "comments" => "body"}`

If you're using Plug, you should be able to call `fetch_query_params(conn)`
and pass the result of `conn.query_params["fields"]` as this option.

## Phoenix Usage

Simply `use JaSerializer.PhoenixView` in your view (or in the Web module) and
define your serializer as above.

The `render("index.json-api", data)` and `render("show.json-api", data)` are defined
for you. You can just call render as normal from your controller.

By specifying `include`s when calling the render function, you can override
the `include: false` in the ArticleView.

```elixir
defmodule PhoenixExample.ArticlesController do
  use PhoenixExample.Web, :controller

  def index(conn, _params) do
    render conn, "index.json-api", data: Repo.all(Article)
  end

  def show(conn, %{"id" => id}) do
    article = Repo.get(Article, id) |> Repo.preload([:comments])
    render conn, "show.json-api", data: article,
      opts: [include: "comments"]
  end

  def create(conn, %{"data" => data}) do
    attrs = JaSerializer.Params.to_attributes(data)
    changeset = Article.changeset(%Article{}, attrs)
    case Repo.insert(changeset) do
      {:ok, article} ->
        conn
        |> put_status(201)
        |> render("show.json-api", data: article)
      {:error, changeset} ->
        conn
        |> put_status(422)
        |> render(:errors, data: changeset)
    end
  end
end

defmodule PhoenixExample.ArticlesView do
  use PhoenixExample.Web, :view
  use JaSerializer.PhoenixView # Or use in web/web.ex

  attributes [:title]

  has_many :comments,
    serializer: PhoenixExample.CommentsView,
    include: false,
    identifiers: :when_included
  #has_many, etc.
end
```

## Configuration

To use the Phoenix `accepts` plug you must configure Plug to handle the
"application/vnd.api+json" mime type and Phoenix to serialize json-api with
Poison.

Depending on your version of Plug add the following to `config.exs`:

Plug ~> "1.2.0"
```elixir
config :phoenix, :format_encoders,
  "json-api": Poison

config :mime, :types, %{
  "application/vnd.api+json" => ["json-api"]
}
```

And then re-compile mime: (per: https://hexdocs.pm/mime/MIME.html)

```shell
mix deps.clean mime --build
mix deps.get
```

Plug < "1.2.0"
```elixir
config :phoenix, :format_encoders,
  "json-api": Poison

config :plug, :mimes, %{
  "application/vnd.api+json" => ["json-api"]
}
```

And then re-compile plug: (per: https://hexdocs.pm/plug/1.1.3/Plug.MIME.html)

```shell
mix deps.clean plug --build
mix deps.get
```

And then add json api to your plug pipeline.

```elixir
pipeline :api do
  plug :accepts, ["json-api"]
end
```

For strict content-type/accept enforcement and to auto add the proper
content-type to responses add the JaSerializer.ContentTypeNegotiation plug.

To normalize attributes to underscores include the JaSerializer.Deserializer
plug.

```elixir
pipeline :api do
  plug :accepts, ["json-api"]
  plug JaSerializer.ContentTypeNegotiation
  plug JaSerializer.Deserializer
end
```

If you're rendering JSON API errors, like `404.json-api`, then you _must_ add `json-api`
to the `accepts` of your `render_errors` within your existing configuration in `config.exs`, like so:

```elixir
config :phoenix, PhoenixExample.Endpoint,
  render_errors: [view: PhoenixExample.ErrorView, accepts: ~w(html json json-api)]
```

## Testing controllers

Set the right headers in `setup` and when passing parameters to put and post requests,
you should pass them as a binary. That is because for map and list parameters,
the content-type will be automatically changed to multipart.

```elixir
defmodule Sample.SomeControllerTest do
  use Sample.ConnCase

  setup %{conn: conn} do
    conn =
      conn
      |> put_req_header("accept", "application/vnd.api+json")
      |> put_req_header("content-type", "application/vnd.api+json")

    {:ok, conn: conn}
  end

  test "create action", %{conn: conn} do
    params = Poison.encode!(%{data: %{attributes: @valid_attrs}})
    conn = post conn, "/some_resource", params

    ...
  end

  ...
end
```

## JSON API Generator

Use our built in generator to get up and running quickly. It uses the same format as the phoenix json generator.

```elixir
mix ja_serializer.gen.phoenix_api Checkbox checkboxes description:string checked:boolean list_id:references:lists
```

Want to tweak our templates? Insert your own under 'priv/templates/ja_serializer.gen.phoenix_api/' and we'll use yours instead.

## Pagination

JaSerializer provides page based pagination integration with
[Scrivener](https://github.com/drewolson/scrivener) or custom pagination
by passing your owns links in.

### Custom

JaSerializer allows custom pagination via the `page` option. The `page` option
expects to receive a `Map` with URL values for `first`, `next`, `prev`,
and `last`.

For example:

```elixir
page = [
  first: "http://example.com/api/v1/posts?page[cursor]=1&page[per]=20",
  prev: nil
  next: "http://example.com/api/v1/posts?page[cursor]=20&page[per]=20",
  last: "http://example.com/api/v1/posts?page[cursor]=60&page[per]=20"
]

# Direct call
JaSerializer.format(MySerializer, collection, conn, page: page)

# In Phoenix Controller
render conn, data: collection, opts: [page: page]
```

### Scrivener Integration

If you are using Scrivener for pagination, all you need to do is pass the
results of `paginate/2` to your serializer.

```elixir
page = MyRepo.paginate(MyModel, params.page)

# Direct call
JaSerializer.format(MySerializer, page, conn, [])

# In Phoenix controller
render conn, data: page
```

When integrating with Scrivener, the URLs generated will be based on the
`Plug.Conn`'s path. This can be overridden by passing in the `page[:base_url]`
option.

```elixir
render conn, data: page, opts: [page: [base_url: "http://example.com/foos"]]
```

You can also configure `ja_serializer` to use a global default URL
base for all links.

```elixir
config :ja_serializer,
  scrivener_base_url: "http://example.com:4000/v1/"
```

*Note*: The resulting URLs will use the JSON-API recommended `page` query
param.

Example URL:
`http://example.com:4000/v1/posts?page[page]=2&page[page-size]=50`

### Meta Data

JaSerializer allows adding top level meta information via the `meta` option. The `meta` option
expects to receive a `Map` containing the data which will be rendered under the top level meta key.

```elixir
meta_data = %{
  "key" => "value"
}

# Direct call
JaSerializer.format(MySerializer, data, conn, meta: meta_data)

# In Phoenix controller
render conn, data: data, opts: [meta: meta_data]
```

## Customization

### Key Format (for Attribute, Relationship and Query Param)

By default keys are `dash-erized` as per the jsonapi.org recommendation, but
keys can be customized via config.

In your `config.exs` file:

```elixir
config :ja_serializer,
  key_format: :underscored
```

You may also pass custom function for serialization and a second optional one for deserialization. Both accept a single binary argument:

```elixir
defmodule MyStringModule do
  def camelize(key), do: key #...
  def underscore(key), do: key #...
end

config :ja_serializer,
  key_format: {:custom, MyStringModule, :camelize, :underscore}
```

If you've already compiled your code, be sure to run `mix deps.clean ja_serializer && mix deps.get`

### Custom Attribute Value Formatters

When serializing attribute values more complex than string, numbers, atoms or
list of those things it is recommended to implement a custom formatter.

To implement a custom formatter:

```elixir
defimpl JaSerializer.Formatter, for: [MyStruct] do
  def format(struct), do: struct
end
```

## Complimentary Libraries

* [JaResource](https://github.com/vt-elixir/ja_resource) - WIP behaviour for creating JSON-API controllers in Phoenix.
* [voorhees](https://github.com/danmcclain/voorhees) - Testing tool for JSON API responses
* [inquisitor](https://github.com/DockYard/inquisitor) - Composable query builder for Ecto
* [scrivener](https://github.com/drewolson/scrivener) - Ecto pagination

## License

JaSerializer source code is released under Apache 2 License. Check LICENSE
file for more information.
Elixir UUID
===========

[![hex.pm version](https://img.shields.io/hexpm/v/uuid.svg?style=flat)](https://hex.pm/packages/uuid)
[![hex.pm downloads](https://img.shields.io/hexpm/dt/uuid.svg?style=flat)](https://hex.pm/packages/uuid)
[![travis.ci build status](https://img.shields.io/travis/zyro/elixir-uuid.svg?style=flat)](https://travis-ci.org/zyro/elixir-uuid)

UUID generator and utilities for [Elixir](http://elixir-lang.org/). See [RFC 4122](http://www.ietf.org/rfc/rfc4122.txt).

### Installation

The latest version is `1.1.7` and requires Elixir `~> 1.0`. New releases may change this minimum compatible version depending on breaking language changes. The [changelog](https://github.com/zyro/elixir-uuid/blob/master/CHANGELOG.md) lists every available release and its corresponding language version requirement.

Releases are published through [hex.pm](https://hex.pm/packages/uuid). Add as a dependency in your `mix.exs` file:
```elixir
defp deps do
  [ { :uuid, "~> 1.1" } ]
end
```

### UUID v1

Generated using a combination of time since the west adopted the gregorian calendar and the node id MAC address.

```elixir
iex> UUID.uuid1()
"5976423a-ee35-11e3-8569-14109ff1a304"
```

### UUID v3

Generated using the MD5 hash of a name and either a namespace atom or an existing UUID. Valid namespaces are: `:dns`, `:url`, `:oid`, `:x500`, `:nil`.

```elixir
iex> UUID.uuid3(:dns, "my.domain.com")
"03bf0706-b7e9-33b8-aee5-c6142a816478"

iex> UUID.uuid3("5976423a-ee35-11e3-8569-14109ff1a304", "my.domain.com")
"0609d667-944c-3c2d-9d09-18af5c58c8fb"
```

### UUID v4

Generated based on pseudo-random bytes.

```elixir
iex> UUID.uuid4()
"fcfe5f21-8a08-4c9a-9f97-29d2fd6a27b9"
```

### UUID v5

Generated using the SHA1 hash of a name and either a namespace atom or an existing UUID. Valid namespaces are: `:dns`, `:url`, `:oid`, `:x500`, `:nil`.

```elixir
iex> UUID.uuid5(:dns, "my.domain.com")
"016c25fd-70e0-56fe-9d1a-56e80fa20b82"

iex> UUID.uuid5("fcfe5f21-8a08-4c9a-9f97-29d2fd6a27b9", "my.domain.com")
"b8e85535-761a-586f-9c04-0fb0df2cbe84"
```

### Formatting

All UUID generator functions have an optional format parameter as the last argument.

Possible values: `:default`, `:hex`, `:urn`. Default value is `:default` and can be omitted.

`:default` is a standard UUID representation:
```elixir
iex> UUID.uuid1()
"3c69679f-774b-4fb1-80c1-7b29c6e7d0a0"

iex> UUID.uuid4(:default)
"3c69679f-774b-4fb1-80c1-7b29c6e7d0a0"

iex> UUID.uuid3(:dns, "my.domain.com")
"03bf0706-b7e9-33b8-aee5-c6142a816478"

iex> UUID.uuid5(:dns, "my.domain.com", :default)
"016c25fd-70e0-56fe-9d1a-56e80fa20b82"
```

`:hex` is a valid hex string, corresponding to the standard UUID without the `-` (dash) characters:
```elixir
iex> UUID.uuid4(:hex)
"19be859d0c1f4a7f95ddced995037350"

iex> UUID.uuid4(:weak, :hex)
"ebeff765ddc843e486c287fb668d5d37"
```

`:urn` is a standard UUID representation prefixed with the UUID URN:
```elixir
iex> UUID.uuid1(:urn)
"urn:uuid:b7483bde-ee35-11e3-8daa-14109ff1a304"
```

### Utility functions

Use `UUID.info!/1` to get a [keyword list](http://elixir-lang.org/getting_started/7.html#toc_1) containing information about the given UUID. An `ArgumentError` is raised if the argument is not a valid UUID string.
```elixir
iex> UUID.info!("870df8e8-3107-4487-8316-81e089b8c2cf")
[uuid: "870df8e8-3107-4487-8316-81e089b8c2cf",
 binary: <<135, 13, 248, 232, 49, 7, 68, 135, 131, 22, 129, 224, 137, 184, 194, 207>>,
 type: :default,
 version: 4,
 variant: :rfc4122]

iex> UUID.info!("8ea1513df8a14dea9bea6b8f4b5b6e73")
[uuid: "8ea1513df8a14dea9bea6b8f4b5b6e73",
 binary: <<142, 161, 81, 61, 248, 161, 77, 234, 155, 234, 107, 143, 75, 91, 110, 115>>,
 type: :hex,
 version: 4,
 variant: :rfc4122]

iex> UUID.info!("urn:uuid:ef1b1a28-ee34-11e3-8813-14109ff1a304")
[uuid: "urn:uuid:ef1b1a28-ee34-11e3-8813-14109ff1a304",
 binary: <<239, 27, 26, 40, 238, 52, 17, 227, 136, 19, 20, 16, 159, 241, 163, 4>>,
 type: :urn,
 version: 1,
 variant: :rfc4122]
```

Use `UUID.string_to_binary!/1` to convert a valid UUID string to its raw binary equivalent. An `ArgumentError` is raised if the argument is not a valid UUID string.
```elixir
iex> UUID.string_to_binary!("870df8e8-3107-4487-8316-81e089b8c2cf")
<<135, 13, 248, 232, 49, 7, 68, 135, 131,
            22, 129, 224, 137, 184, 194, 207>>

iex> UUID.string_to_binary!("8ea1513df8a14dea9bea6b8f4b5b6e73")
<<142, 161, 81, 61, 248, 161, 77, 234, 155,
            234, 107, 143, 75, 91, 110, 115>>


iex> UUID.string_to_binary!("urn:uuid:ef1b1a28-ee34-11e3-8813-14109ff1a304")
<<239, 27, 26, 40, 238, 52, 17, 227, 136,
            19, 20, 16, 159, 241, 163, 4>>
```

Use `UUID.binary_to_string!/2` to convert valid UUID binary data to a String representation, with an optional format similar to the generator functions above. An `ArgumentError` is raised if the argument is not valid UUID binary data.
```elixir
iex> UUID.binary_to_string!(<<135, 13, 248, 232, 49, 7, 68, 135, 131,
            22, 129, 224, 137, 184, 194, 207>>)
"870df8e8-3107-4487-8316-81e089b8c2cf"

iex> UUID.binary_to_string!(<<142, 161, 81, 61, 248, 161, 77, 234, 155,
            234, 107, 143, 75, 91, 110, 115>>, :hex)
"8ea1513df8a14dea9bea6b8f4b5b6e73"

iex> UUID.binary_to_string!(<<239, 27, 26, 40, 238, 52, 17, 227, 136,
            19, 20, 16, 159, 241, 163, 4>>, :urn)
"urn:uuid:ef1b1a28-ee34-11e3-8813-14109ff1a304"
```

### Attribution

Some code ported from [avtobiff/erlang-uuid](https://github.com/avtobiff/erlang-uuid).

Some helper functions from [rjsamson/hexate](https://github.com/rjsamson/hexate).

### License

```
Copyright 2014-2016 Andrei Mihu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
Connection
==========

`Connection` behaviour for connection processes. The API is superset of the
GenServer API. There are 2 additional callbacks `connect/2` and `disconnect/2`:

```elixir
  @callback init(any) ::
    {:ok, any} | {:ok, any, timeout | :hibernate} |
    {:connect, any, any} |
    {:backoff, timeout, any} | {:backoff, timeout, any, timeout | :hibernate} |
    :ignore | {:stop, any}

  @callback connect(any, any) ::
    {:ok, any} | {:ok, any, timeout | :hibernate} |
    {:backoff, timeout, any} | {:backoff, timeout, any, timeout | :hibernate} |
    {:stop, any, any}

  @callback disconnect(any, any) ::
    {:connect, any, any} |
    {:backoff, timeout, any} | {:backoff, timeout, any, timeout | :hibernate} |
    {:noconnect, any} | {:noconnect, any, timeout | :hibernate}
    {:stop, any, any}

  @callback handle_call(any, {pid, any}, any) ::
    {:reply, any, any} | {:reply, any, any, timeout | :hibernate} |
    {:noreply, any} | {:noreply, any, timeout | :hibernate} |
    {:disconnect | :connect, any, any} |
    {:disconnect | :connect, any, any, any} |
    {:stop, any, any} | {:stop, any, any, any}

  @callback handle_cast(any, any) ::
    {:noreply, any} | {:noreply, any, timeout | :hibernate} |
    {:disconnect | :connect, any, any} |
    {:stop, any, any}

  @callback handle_info(any, any) ::
    {:noreply, any} | {:noreply, any, timeout | :hibernate} |
    {:disconnect | :connect, any, any} |
    {:stop, any, any}

  @callback code_change(any, any, any) :: {:ok, any}

  @callback terminate(any, any) :: any
```
There is an example of a simple TCP connection process in
`examples/tcp_connection/`.
# Poison

[![Travis](https://img.shields.io/travis/devinus/poison.svg?style=flat-square)](https://travis-ci.org/devinus/poison)
[![Hex.pm](https://img.shields.io/hexpm/v/poison.svg?style=flat-square)](https://hex.pm/packages/poison)
[![Hex.pm](https://img.shields.io/hexpm/dt/poison.svg?style=flat-square)](https://hex.pm/packages/poison)
[![Gratipay](https://img.shields.io/gratipay/devinus.svg?style=flat-square)](https://gratipay.com/devinus)

Poison is a new JSON library for Elixir focusing on wicked-fast **speed**
without sacrificing **simplicity**, **completeness**, or **correctness**.

Poison takes several approaches to be the fastest JSON library for Elixir.

Poison uses extensive [sub binary matching][1], a **hand-rolled parser** using
several techniques that are [known to benefit HiPE][2] for native compilation,
[IO list][3] encoding and **single-pass** decoding.

Preliminary benchmarking has sometimes put Poison's performance closer to
`jiffy`, and almost always faster than existing Elixir libraries.

## Installation

First, add Poison to your `mix.exs` dependencies:

```elixir
def deps do
  [{:poison, "~> 2.0"}]
end
```

Then, update your dependencies:

```sh-session
$ mix deps.get
```

## Usage

```elixir
defmodule Person do
  @derive [Poison.Encoder]
  defstruct [:name, :age]
end

Poison.encode!(%Person{name: "Devin Torres", age: 27})
#=> "{\"name\":\"Devin Torres\",\"age\":27}"

Poison.decode!(~s({"name": "Devin Torres", "age": 27}), as: %Person{})
#=> %Person{name: "Devin Torres", age: 27}

Poison.decode!(~s({"people": [{"name": "Devin Torres", "age": 27}]}),
  as: %{"people" => [%Person{}]})
#=> %{"people" => [%Person{age: 27, name: "Devin Torres"}]}
```

Every component of Poison -- the encoder, decoder, and parser -- are all usable
on their own without buying into other functionality. For example, if you were
interested purely in the speed of parsing JSON without a decoding step, you
could simply call `Poison.Parser.parse`.

If you use Poison 1.x, you have to set a module to `as` option in order to
decode into a struct. e.g. `as: Person` instead of `as: %Person{}`. The change was
introduced at 2.0.0.

## Parser

```iex
iex> Poison.Parser.parse!(~s({"name": "Devin Torres", "age": 27}))
%{"name" => "Devin Torres", "age" => 27}
iex> Poison.Parser.parse!(~s({"name": "Devin Torres", "age": 27}), keys: :atoms!)
%{name: "Devin Torres", age: 27}
```

Note that `keys: :atoms!` reuses existing atoms, i.e. if `:name` was not
allocated before the call, you will encounter an `argument error` message.

You can use the `keys: :atoms` variant to make sure all atoms are created as
needed.  However, unless you absolutely know what you're doing, do **not** do
it.  Atoms are not garbage-collected, see
[Erlang Efficiency Guide](http://www.erlang.org/doc/efficiency_guide/commoncaveats.html)
for more info:

> Atoms are not garbage-collected. Once an atom is created, it will never be
> removed. The emulator will terminate if the limit for the number of atoms
> (1048576 by default) is reached.

## Encoder

```iex
iex> IO.puts Poison.Encoder.encode([1, 2, 3], [])
"[1,2,3]"
```

Anything implementing the Encoder protocol is expected to return an
[IO list][4] to be embedded within any other Encoder's implementation and
passable to any IO subsystem without conversion.

```elixir
defimpl Poison.Encoder, for: Person do
  def encode(%{name: name, age: age}, options) do
    Poison.Encoder.BitString.encode("#{name} (#{age})", options)
  end
end
```

For maximum performance, make sure you `@derive [Poison.Encoder]` for any struct
you plan on encoding.

### Encoding only some attributes

When deriving structs for encoding, it is possible to select or exclude specific attributes. This is achieved by deriving `Poison.Encoder` with the `:only` or `:except` options set:

```elixir
defmodule PersonOnlyName do
  @derive {Poison.Encoder, only: [:name]}
  defstruct [:name, :age]
end

defmodule PersonWithoutName do
  @derive {Poison.Encoder, except: [:name]}
  defstruct [:name, :age]
end
```

In case both `:only` and `:except` keys are defined, the `:except` option is ignored.

## Benchmarking

```sh-session
$ mix deps.get
$ MIX_ENV=bench mix compile
$ MIX_ENV=bench mix bench
```

## License

Poison is released into the public domain (see `UNLICENSE`).
Poison is also optionally available under the ISC License (see `LICENSE`),
meant especially for jurisdictions that do not recognize public domain works.

[1]: http://www.erlang.org/euc/07/papers/1700Gustafsson.pdf
[2]: http://www.erlang.org/workshop/2003/paper/p36-sagonas.pdf
[3]: http://jlouisramblings.blogspot.com/2013/07/problematic-traits-in-erlang.html
[4]: http://prog21.dadgum.com/70.html
# JOSE

[![Build Status](https://travis-ci.org/potatosalad/erlang-jose.svg?branch=master)](https://travis-ci.org/potatosalad/erlang-jose) [![Hex.pm](https://img.shields.io/hexpm/v/jose.svg)](https://hex.pm/packages/jose)

JSON Object Signing and Encryption (JOSE) for Erlang and Elixir.

## Installation

Add `jose` to your project's dependencies in `mix.exs`

```elixir
defp deps do
  [
    {:jose, "~> 1.8"}
  ]
end
```

If you are using deployment tools (`exrm`, etc.) and your app depends
on `jose` directly, you will need to include `jose` in your
applications list in `mix.exs` to ensure they get compiled into your
release:

```elixir
def application do
  [mod: {YourApp, []},
   applications: [:jose]]
end
```

Add `jose` to your project's dependencies in your `Makefile` for [`erlang.mk`](https://github.com/ninenines/erlang.mk) or the following to your `rebar.config`

```erlang
{deps, [
  {jose, ".*", {git, "git://github.com/potatosalad/erlang-jose.git", {branch, "master"}}}
]}.
```

#### JSON Encoder/Decoder

You will also need to specify either [jiffy](https://github.com/davisp/jiffy), [jsone](https://github.com/sile/jsone), [jsx](https://github.com/talentdeficit/jsx), or [Poison](https://github.com/devinus/poison) as a dependency.

For example, with Elixir and `mix.exs`

```elixir
defp deps do
  [
    {:jose, "~> 1.8"},
    {:poison, "~> 2.2"}
  ]
end
```

Or with Erlang and `rebar.config`

```erlang
{deps, [
  {jose, ".*", {git, "git://github.com/potatosalad/erlang-jose.git", {branch, "master"}}},
  {jsx, ".*", {git, "git://github.com/talentdeficit/jsx.git", {branch, "master"}}}
]}.
```

`jose` will attempt to find a suitable JSON encoder/decoder and will default to Poison on Elixir and jiffy, jsone, or jsx on Erlang.  If more than one are present, it will default to Poison.

You may also specify a different `json_module` as an application environment variable to `jose` or by using `jose:json_module/1` or `JOSE.json_module/1`.

#### ChaCha20/Poly1305 Support

ChaCha20/Poly1305 encryption and one-time message authentication functions are experimentally supported based on [RFC 7539](https://tools.ietf.org/html/rfc7539).

Fallback support for `ChaCha20/Poly1305` encryption and `Poly1305` signing is also provided.  See [`crypto_fallback`](#cryptographic-algorithm-fallback) below.

External support is also provided by the following libraries:

 * [libsodium](https://github.com/potatosalad/erlang-libsodium) - `ChaCha20/Poly1305` encryption and `Poly1305` signing

Other modules which implement the `jose_chacha20_poly1305` behavior may also be used as follows:

```elixir
# ChaCha20/Poly1305
JOSE.chacha20_poly1305_module(:libsodium)                  # uses a fast Erlang port driver for libsodium
JOSE.chacha20_poly1305_module(:jose_jwa_chacha20_poly1305) # uses the pure Erlang implementation (slow)
```

#### Curve25519 and Curve448 Support

Curve25519 and Curve448 and their associated signing/key exchange functions are experimentally supported while [CFRG ECDH and signatures in JOSE](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves) is still a draft.

Fallback support for `Ed25519`, `Ed25519ph`, `Ed448`, `Ed448ph`, `X25519`, and `X448` is provided.  See [`crypto_fallback`](#cryptographic-algorithm-fallback) below.

External support is also provided by the following libraries:

 * [libdecaf](https://github.com/potatosalad/erlang-libdecaf) - `Ed25519`, `Ed25519ph`, `Ed448`, `Ed448ph`, `X25519`, `X448`
 * [libsodium](https://github.com/potatosalad/erlang-libsodium) - `Ed25519`, `Ed25519ph`, `X25519`

If both libraries are present, libdecaf will be used by default.  Other modules which implement the `jose_curve25519` or `jose_curve448` behaviors may also be used as follows:

```elixir
# Curve25519
JOSE.curve25519_module(:libdecaf)            # uses a fast Erlang NIF for libdecaf
JOSE.curve25519_module(:jose_jwa_curve25519) # uses the pure Erlang implementation (slow)

# Curve448
JOSE.curve448_module(:libdecaf)          # uses a fast Erlang NIF for libdecaf
JOSE.curve448_module(:jose_jwa_curve448) # uses the pure Erlang implementation (slow)
```

#### SHA-3 Support

SHA-3 is experimentally supported for use with `Ed448` and `Ed448ph` signing functions.

Fallback support for SHA-3 is provided.  See [`crypto_fallback`](#cryptographic-algorithm-fallback) below.

External support for SHA-3 is provided by the [keccakf1600](https://github.com/potatosalad/erlang-keccakf1600) and [libdecaf](https://github.com/potatosalad/erlang-libdecaf) libraries.  If present, keccakf1600 will be used by default.  Other modules which implement the `jose_sha3` behaviors may also be used as follows:

```elixir
JOSE.sha3_module(:keccakf1600)   # uses a NIF written in C with timeslice reductions
JOSE.sha3_module(:jose_jwa_sha3) # uses the pure Erlang implementation (slow)
```

#### Cryptographic Algorithm Fallback

`jose` strives to support [all](#algorithm-support) of the cryptographic algorithms specified in the [JOSE RFCs](https://tools.ietf.org/wg/jose/).

However, not all of the required algorithms are supported natively by Erlang/Elixir.  For algorithms unsupported by the native [`crypto`](http://www.erlang.org/doc/man/crypto.html) and [`public_key`](http://www.erlang.org/doc/man/public_key.html), `jose` has a pure Erlang implementation that may be used as a fallback.

See [ALGORITHMS.md](https://github.com/potatosalad/erlang-jose/blob/master/ALGORITHMS.md) for more information about algorithm support for specific OTP versions.

By default, the algorithm fallback is disabled, but can be enabled by setting the `crypto_fallback` application environment variable for `jose` to `true` or by calling `jose:crypto_fallback/1` or `JOSE.crypto_fallback/1` with `true`.

You may also review which algorithms are currently supported with the `jose_jwa:supports/0` or `JOSE.JWA.supports/0` functions.  For example, on Elixir 1.0.5 and OTP 18:

```elixir
# crypto_fallback defaults to false
JOSE.JWA.supports

[{:jwe,
  {:alg,
   ["A128GCMKW", "A128KW", "A192GCMKW", "A192KW", "A256GCMKW", "A256KW",
    "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A192KW", "ECDH-ES+A256KW",
    "PBES2-HS256+A128KW", "PBES2-HS384+A192KW", "PBES2-HS512+A256KW",
    "RSA-OAEP", "RSA1_5", "dir"]},
  {:enc,
   ["A128CBC-HS256", "A128GCM", "A192CBC-HS384", "A192GCM", "A256CBC-HS512",
    "A256GCM"]}, {:zip, ["DEF"]}},
 {:jwk, {:kty, ["EC", "OKP", "RSA", "oct"]}, {:kty_OKP_crv, []}},
 {:jws,
  {:alg,
   ["ES256", "ES384", "ES512", "HS256", "HS384", "HS512", "RS256", "RS384",
    "RS512"]}}]

# setting crypto_fallback to true
JOSE.crypto_fallback(true)

# additional algorithms are now available for use
JOSE.JWA.supports

[{:jwe,
  {:alg,
   ["A128GCMKW", "A128KW", "A192GCMKW", "A192KW", "A256GCMKW", "A256KW",
    "ECDH-ES", "ECDH-ES+A128KW", "ECDH-ES+A192KW", "ECDH-ES+A256KW",
    "PBES2-HS256+A128KW", "PBES2-HS384+A192KW", "PBES2-HS512+A256KW",
    "RSA-OAEP", "RSA-OAEP-256", "RSA1_5", "dir"]},
  {:enc,
   ["A128CBC-HS256", "A128GCM", "A192CBC-HS384", "A192GCM", "A256CBC-HS512",
    "A256GCM", "ChaCha20/Poly1305"]}, {:zip, ["DEF"]}},
 {:jwk, {:kty, ["EC", "OKP", "RSA", "oct"]},
  {:kty_OKP_crv,
   ["Ed25519", "Ed25519ph", "Ed448", "Ed448ph", "X25519", "X448"]}},
 {:jws,
  {:alg,
   ["ES256", "ES384", "ES512", "Ed25519", "Ed25519ph", "Ed448", "Ed448ph",
    "HS256", "HS384", "HS512", "PS256", "PS384", "PS512", "Poly1305", "RS256",
    "RS384", "RS512"]}}]
```

#### Unsecured Signing Vulnerability

The [`"none"`](https://tools.ietf.org/html/rfc7515#appendix-A.5) signing algorithm is disabled by default to prevent accidental verification of empty signatures (read about the vulnerability [here](https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/)).

If you want to further restrict the signature algorithms allowed for a token, use `JOSE.JWT.verify_strict/3`:

```elixir
# Signed Compact JSON Web Token (JWT) with HS256
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzMDA4MTkzODAsImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlLCJpc3MiOiJqb2UifQ.shLcxOl_HBBsOTvPnskfIlxHUibPN7Y9T4LhPB-iBwM"

# JSON Web Key (JWK)
jwk = %{
  "kty" => "oct",
  "k" => :base64url.encode("symmetric key")
}

{verified, _, _} = JOSE.JWT.verify_strict(jwk, ["HS256"], token)
# {true, _, _}

{verified, _, _} = JOSE.JWT.verify_strict(jwk, ["RS256"], token)
# {false, _, _}
```

If you need to inspect the contents of a JSON Web token (JWT) prior to verifying it, use `JOSE.JWT.peek_payload/1` or `JOSE.JWT.peek_protected/1`:

```elixir
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzMDA4MTkzODAsImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlLCJpc3MiOiJqb2UifQ.shLcxOl_HBBsOTvPnskfIlxHUibPN7Y9T4LhPB-iBwM"

payload = JOSE.JWT.peek_payload(token)
# %JOSE.JWT{fields: %{"exp" => 1300819380, "http://example.com/is_root" => true,
#    "iss" => "joe"}}

protected = JOSE.JWT.peek_protected(token)
# %JOSE.JWS{alg: {:jose_jws_alg_hmac, {:jose_jws_alg_hmac, :sha256}},
#  b64: :undefined, fields: %{"typ" => "JWT"}}

# If you want to inspect the JSON, you can convert it back to a regular map:
{_, protected_map} = JOSE.JWS.to_map(protected)
# {_, %{"alg" => "HS256", "typ" => "JWT"}}
```

You may also enable the `"none"` algorithm as an application environment variable for `jose` or by using `jose:unsecured_signing/1` or `JOSE.unsecured_signing/1`.

```elixir
# unsecured_signing defaults to false
JOSE.JWA.supports[:jws]

{:alg,
 ["ES256", "ES384", "ES512", "Ed25519", "Ed25519ph", "Ed448", "Ed448ph",
  "HS256", "HS384", "HS512", "PS256", "PS384", "PS512", "Poly1305", "RS256",
  "RS384", "RS512"]}

# setting unsecured_signing to true
JOSE.unsecured_signing(true)

# the "none" algorithm is now available for use
JOSE.JWA.supports[:jws]

{:alg,
 ["ES256", "ES384", "ES512", "Ed25519", "Ed25519ph", "Ed448", "Ed448ph",
  "HS256", "HS384", "HS512", "PS256", "PS384", "PS512", "Poly1305", "RS256",
  "RS384", "RS512", "none"]}
```

## Usage

##### JSON Web Signature (JWS) of JSON Web Token (JWT) using HMAC using SHA-256 (HS256) with JSON Web Key (JWK)

_Elixir_

```elixir
# JSON Web Key (JWK)
jwk = %{
  "kty" => "oct",
  "k" => :base64url.encode("symmetric key")
}

# JSON Web Signature (JWS)
jws = %{
  "alg" => "HS256"
}

# JSON Web Token (JWT)
jwt = %{
  "iss" => "joe",
  "exp" => 1300819380,
  "http://example.com/is_root" => true
}

signed = JOSE.JWT.sign(jwk, jws, jwt)
# {%{alg: :jose_jws_alg_hmac},
#  %{"payload" => "eyJleHAiOjEzMDA4MTkzODAsImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlLCJpc3MiOiJqb2UifQ",
#    "protected" => "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
#    "signature" => "shLcxOl_HBBsOTvPnskfIlxHUibPN7Y9T4LhPB-iBwM"}}

compact_signed = JOSE.JWS.compact(signed)
# {%{alg: :jose_jws_alg_hmac},
#  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzMDA4MTkzODAsImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlLCJpc3MiOiJqb2UifQ.shLcxOl_HBBsOTvPnskfIlxHUibPN7Y9T4LhPB-iBwM"}

verified = JOSE.JWT.verify(jwk, compact_signed)
# {true,
#  %JOSE.JWT{fields: %{"exp" => 1300819380, "http://example.com/is_root" => true,
#     "iss" => "joe"}},
#  %JOSE.JWS{alg: {:jose_jws_alg_hmac, :HS256}, b64: :undefined,
#   fields: %{"typ" => "JWT"}}}

verified == JOSE.JWT.verify(jwk, signed)
# true
```

_Erlang_

```erlang
% JSON Web Key (JWK)
JWK = #{
  <<"kty">> => <<"oct">>,
  <<"k">> => base64url:encode(<<"symmetric key">>)
}.

% JSON Web Signature (JWS)
JWS = #{
  <<"alg">> => <<"HS256">>
}.

% JSON Web Token (JWT)
JWT = #{
  <<"iss">> => <<"joe">>,
  <<"exp">> => 1300819380,
  <<"http://example.com/is_root">> => true
}.

Signed = jose_jwt:sign(JWK, JWS, JWT).
% {#{alg => jose_jws_alg_hmac},
%  #{<<"payload">> => <<"eyJleHAiOjEzMDA4MTkzODAsImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlLCJpc3MiOiJqb2UifQ">>,
%    <<"protected">> => <<"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9">>,
%    <<"signature">> => <<"shLcxOl_HBBsOTvPnskfIlxHUibPN7Y9T4LhPB-iBwM">>}}

CompactSigned = jose_jws:compact(Signed).
% {#{alg => jose_jws_alg_hmac},
%  <<"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjEzMDA4MTkzODAsImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlLCJpc3MiOiJqb2UifQ.shLcxOl_HBBsOTvPnskfIlxHUibPN7Y9T4LhPB-iBwM">>}

Verified = jose_jwt:verify(JWK, CompactSigned).
% {true,
%     #jose_jwt{
%         fields =
%             #{<<"exp">> => 1300819380,
%               <<"http://example.com/is_root">> => true,
%               <<"iss">> => <<"joe">>}},
%     #jose_jws{
%         alg = {jose_jws_alg_hmac,'HS256'},
%         b64 = undefined,
%         fields = #{<<"typ">> => <<"JWT">>}}}

Verified =:= jose_jwt:verify(JWK, Signed).
% true
```

##### Reading JSON Web Keys (JWK) from PEM files

The examples below use three keys created with `openssl`:

```bash
# RSA Private Key
openssl genrsa -out rsa-2048.pem 2048

# EC Private Key (Alice)
openssl ecparam -name secp256r1 -genkey -noout -out ec-secp256r1-alice.pem

# EC Private Key (Bob)
openssl ecparam -name secp256r1 -genkey -noout -out ec-secp256r1-bob.pem
```

_Elixir_

```elixir
# RSA examples
rsa_private_jwk = JOSE.JWK.from_pem_file("rsa-2048.pem")
rsa_public_jwk  = JOSE.JWK.to_public(rsa_private_jwk)

## Sign and Verify (defaults to PS256)
message = "my message"
signed = JOSE.JWK.sign(message, rsa_private_jwk)
{true, ^message, _} = JOSE.JWK.verify(signed, rsa_public_jwk)

## Sign and Verify (specify RS256)
signed = JOSE.JWK.sign(message, %{ "alg" => "RS256" }, rsa_private_jwk)
{true, ^message, _} = JOSE.JWK.verify(signed, rsa_public_jwk)

## Encrypt and Decrypt (defaults to RSA-OAEP with A128CBC-HS256)
plain_text = "my plain text"
encrypted = JOSE.JWK.block_encrypt(plain_text, rsa_public_jwk)
{^plain_text, _} = JOSE.JWK.block_decrypt(encrypted, rsa_private_jwk)

## Encrypt and Decrypt (specify RSA-OAEP-256 with A128GCM)
encrypted = JOSE.JWK.block_encrypt(plain_text, %{ "alg" => "RSA-OAEP-256", "enc" => "A128GCM" }, rsa_public_jwk)
{^plain_text, _} = JOSE.JWK.block_decrypt(encrypted, rsa_private_jwk)

# EC examples
alice_private_jwk = JOSE.JWK.from_pem_file("ec-secp256r1-alice.pem")
alice_public_jwk  = JOSE.JWK.to_public(alice_private_jwk)
bob_private_jwk   = JOSE.JWK.from_pem_file("ec-secp256r1-bob.pem")
bob_public_jwk    = JOSE.JWK.to_public(bob_private_jwk)

## Sign and Verify (defaults to ES256)
message = "my message"
signed = JOSE.JWK.sign(message, alice_private_jwk)
{true, ^message, _} = JOSE.JWK.verify(signed, alice_public_jwk)

## Encrypt and Decrypt (defaults to ECDH-ES with A128GCM)
### Alice sends Bob a secret message using Bob's public key and Alice's private key
alice_to_bob = "For Bob's eyes only."
encrypted = JOSE.JWK.box_encrypt(alice_to_bob, bob_public_jwk, alice_private_jwk)
### Only Bob can decrypt the message using his private key (Alice's public key is embedded in the JWE header)
{^alice_to_bob, _} = JOSE.JWK.box_decrypt(encrypted, bob_private_jwk)
```

_Erlang_

```erlang
% RSA examples
RSAPrivateJWK = jose_jwk:from_pem_file("rsa-2048.pem"),
RSAPublicJWK  = jose_jwk:to_public(RSAPrivateJWK).

%% Sign and Verify (defaults to PS256)
Message = <<"my message">>,
SignedPS256 = jose_jwk:sign(Message, RSAPrivateJWK),
{true, Message, _} = jose_jwk:verify(SignedPS256, RSAPublicJWK).

%% Sign and Verify (specify RS256)
SignedRS256 = jose_jwk:sign(Message, #{ <<"alg">> => <<"RS256">> }, RSAPrivateJWK),
{true, Message, _} = jose_jwk:verify(SignedRS256, RSAPublicJWK).

%% Encrypt and Decrypt (defaults to RSA-OAEP with A128CBC-HS256)
PlainText = <<"my plain text">>,
EncryptedRSAOAEP = jose_jwk:block_encrypt(PlainText, RSAPublicJWK),
{PlainText, _} = jose_jwk:block_decrypt(EncryptedRSAOAEP, RSAPrivateJWK).

%% Encrypt and Decrypt (specify RSA-OAEP-256 with A128GCM)
EncryptedRSAOAEP256 = jose_jwk:block_encrypt(PlainText, #{ <<"alg">> => <<"RSA-OAEP-256">>, <<"enc">> => <<"A128GCM">> }, RSAPublicJWK),
{PlainText, _} = jose_jwk:block_decrypt(EncryptedRSAOAEP256, RSAPrivateJWK).

% EC examples
AlicePrivateJWK = jose_jwk:from_pem_file("ec-secp256r1-alice.pem"),
AlicePublicJWK  = jose_jwk:to_public(AlicePrivateJWK),
BobPrivateJWK   = jose_jwk:from_pem_file("ec-secp256r1-bob.pem"),
BobPublicJWK    = jose_jwk:to_public(BobPrivateJWK).

%% Sign and Verify (defaults to ES256)
Message = <<"my message">>,
SignedES256 = jose_jwk:sign(Message, AlicePrivateJWK),
{true, Message, _} = jose_jwk:verify(SignedES256, AlicePublicJWK).

%% Encrypt and Decrypt (defaults to ECDH-ES with A128GCM)
%%% Alice sends Bob a secret message using Bob's public key and Alice's private key
AliceToBob = <<"For Bob's eyes only.">>,
EncryptedECDHES = jose_jwk:box_encrypt(AliceToBob, BobPublicJWK, AlicePrivateJWK),
%%% Only Bob can decrypt the message using his private key (Alice's public key is embedded in the JWE header)
{AliceToBob, _} = jose_jwk:box_decrypt(EncryptedECDHES, BobPrivateJWK).
```

## Algorithm Support

### JSON Web Encryption (JWE) [RFC 7516](https://tools.ietf.org/html/rfc7516)

#### `"alg"` [RFC 7518 Section 4](https://tools.ietf.org/html/rfc7518#section-4)

- [X] `A128GCMKW` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `A192GCMKW` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `A256GCMKW` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `A128KW` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `A192KW` <sup>[OTP-17](#footnote-otp-17), [OTP-18](#footnote-otp-18)</sup>
- [X] `A256KW` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `dir`
- [X] `ECDH-ES`
- [X] `ECDH-ES+A128KW`
- [X] `ECDH-ES+A192KW`
- [X] `ECDH-ES+A256KW`
- [X] `PBES2-HS256+A128KW` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `PBES2-HS384+A192KW` <sup>[OTP-17](#footnote-otp-17), [OTP-18](#footnote-otp-18)</sup>
- [X] `PBES2-HS512+A256KW` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `RSA1_5`
- [X] `RSA-OAEP`
- [X] `RSA-OAEP-256` <sup>[OTP-17](#footnote-otp-17), [OTP-18](#footnote-otp-18), [OTP-19](#footnote-otp-19)</sup>

#### `"enc"` [RFC 7518 Section 5](https://tools.ietf.org/html/rfc7518#section-5)

- [X] `A128CBC-HS256`
- [X] `A192CBC-HS384` <sup>[OTP-17](#footnote-otp-17), [OTP-18](#footnote-otp-18)</sup>
- [X] `A256CBC-HS512`
- [X] `A128GCM` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `A192GCM` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `A256GCM` <sup>[OTP-17](#footnote-otp-17)</sup>
- [X] `ChaCha20/Poly1305` <sup>experimental</sup>

#### `"zip"` [RFC 7518 Section 7.3](https://tools.ietf.org/html/rfc7518#section-7.3)

- [X] `DEF`

### JSON Web Key (JWK) [RFC 7517](https://tools.ietf.org/html/rfc7517)

#### `"alg"` [RFC 7518 Section 6](https://tools.ietf.org/html/rfc7518#section-6)

- [X] `EC`
- [X] `oct`
- [X] `OKP` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves)</sup>
- [X] `OKP` with `{"crv":"Ed25519"}` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.1)</sup>
- [X] `OKP` with `{"crv":"Ed25519ph"}` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.1)</sup>
- [X] `OKP` with `{"crv":"Ed448"}` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.2)</sup>
- [X] `OKP` with `{"crv":"Ed448ph"}` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.2)</sup>
- [X] `OKP` with `{"crv":"X25519"}` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [RFC 7748](https://tools.ietf.org/html/rfc7748#section-5)</sup>
- [X] `OKP` with `{"crv":"X448"}` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [RFC 7748](https://tools.ietf.org/html/rfc7748#section-5)</sup>
- [X] `RSA`

### JSON Web Signature (JWS) [RFC 7515](https://tools.ietf.org/html/rfc7515)

#### `"alg"` [RFC 7518 Section 3](https://tools.ietf.org/html/rfc7518#section-3)

- [X] `Ed25519` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.1)</sup>
- [X] `Ed25519ph` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.1)</sup>
- [X] `Ed448` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.2)</sup>
- [X] `Ed448ph` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa#section-5.2)</sup>
- [X] `EdDSA` <sup>[draft-ietf-jose-cfrg-curves](https://tools.ietf.org/html/draft-ietf-jose-cfrg-curves), [draft-irtf-cfrg-eddsa](https://tools.ietf.org/html/draft-irtf-cfrg-eddsa)</sup>
- [X] `ES256`
- [X] `ES384`
- [X] `ES512`
- [X] `HS256`
- [X] `HS384`
- [X] `HS512`
- [X] `Poly1305` <sup>experimental</sup>
- [X] `PS256` <sup>[OTP-17](#footnote-otp-17), [OTP-18](#footnote-otp-18), [OTP-19](#footnote-otp-19)</sup>
- [X] `PS384` <sup>[OTP-17](#footnote-otp-17), [OTP-18](#footnote-otp-18), [OTP-19](#footnote-otp-19)</sup>
- [X] `PS512` <sup>[OTP-17](#footnote-otp-17), [OTP-18](#footnote-otp-18), [OTP-19](#footnote-otp-19)</sup>
- [X] `RS256`
- [X] `RS384`
- [X] `RS512`
- [X] `none` <sup>[unsecured](#footnote-unsecured)</sup>

### Additional Specifications

- [X] JSON Web Key (JWK) Thumbprint [RFC 7638](https://tools.ietf.org/html/rfc7638)
- [X] JWS Unencoded Payload Option [draft-ietf-jose-jws-signing-input-options-04](https://tools.ietf.org/html/draft-ietf-jose-jws-signing-input-options-04)

<sup><a name="footnote-otp-17">OTP-17</a></sup> Native algorithm not supported by OTP-17.  Use the [`crypto_fallback`](#cryptographic-algorithm-fallback) setting to enable the non-native implementation.  See [ALGORITHMS.md](https://github.com/potatosalad/erlang-jose/blob/master/ALGORITHMS.md) for more information about algorithm support for specific OTP versions.

<sup><a name="footnote-otp-18">OTP-18</a></sup> Native algorithm not supported by OTP-18.  Use the [`crypto_fallback`](#cryptographic-algorithm-fallback) setting to enable the non-native implementation.  See [ALGORITHMS.md](https://github.com/potatosalad/erlang-jose/blob/master/ALGORITHMS.md) for more information about algorithm support for specific OTP versions.

<sup><a name="footnote-otp-19">OTP-19</a></sup> Native algorithm not supported by OTP-19.  Use the [`crypto_fallback`](#cryptographic-algorithm-fallback) setting to enable the non-native implementation.  See [ALGORITHMS.md](https://github.com/potatosalad/erlang-jose/blob/master/ALGORITHMS.md) for more information about algorithm support for specific OTP versions.

<sup><a name="footnote-unsecured">unsecured</a></sup> This algorithm is disabled by default due to the unsecured signing vulnerability.  Use the [`unsecured_signing`](#unsecured-signing-vulnerability) setting to enable this algorithm.
# Inflex[![Build Status](https://travis-ci.org/nurugger07/inflex.png?branch=master)](https://travis-ci.org/nurugger07/inflex)

An Elixir library for handling word inflections.

## Getting Started

You can add Inflex as a dependency in your `mix.exs` file. Since it only requires Elixir and Erlang there are no other dependencies.

```elixir
def deps do
  [ { :inflex, "~> 1.8.0" } ]
end
```

If you are not using [hex](http://hex.pm) you can add the dependency using the github repo.

``` elixir

  def deps do
    [ { :inflex, github: "nurugger07/inflex" } ]
  end

```

Then run `mix deps.get` in the shell to fetch and compile the dependencies.

To incorporate Inflex in your modules, use `import`.

``` elixir

  defmodule YourModule do
    import Inflex

    def make_singular(word), do: singularize(word)

  end

```

## Examples

### Singularize & Pluralize

Here are some basic examples from `iex`:

``` elixir

iex(1)> Inflex.singularize("dogs")
"dog"

iex(2)> Inflex.pluralize("dog")
"dogs"

iex(3)> Inflex.singularize("people")
"person"

iex(4)> Inflex.pluralize("person")
"people"

```

Some other special cases are handled for nouns ending in -o and  -y

```elixir


iex(1)> Inflex.pluralize("piano")
"pianos"

iex(2)> Inflex.pluralize("hero")
"heroes"

iex(3)> Inflex.pluralize("butterfly")
"butterflies"

iex(4)> Inflex.pluralize("monkey")
"monkeys"

```

### Inflect

``` elixir
iex(1)> Inflex.inflect("child", 1)
"child"

iex(2)> Inflex.inflect("child", 2)
"children"
```

### Camelize & Pascalize

Inflex also camelizes or pascalizes strings and atoms.

```elixir

iex(1)> Inflex.camelize(:upper_camel_case)
"UpperCamelCase"

iex(2)> Inflex.camelize("pascal-case", :lower)
"pascalCase"

```

### Parameterize

Strings can be parameterized easily.

```elixir

iex(1)> Inflex.parameterize("String for parameter")
"string-for-parameter"

iex(2)> Inflex.parameterize("String with underscore", "_")
"string_with_underscore"

```

### Underscore

Makes an underscored, lowercase form from a string or atom.

```elixir

iex(1)> Inflex.underscore("UpperCamelCase")
"upper_camel_case"

iex(2)> Inflex.underscore("pascalCase")
"pascal_case"

iex(3)> Inflex.underscore(UpperCamelCase)
"upper_camel_case"

iex(4)> Inflex.underscore(:pascalCase)
"pascal_case"

```

## Contributing

All pull requests will be reviewed for inclusion but must include tests.
# PlugBenchPhoenix

To start your Phoenix app:

  * Install dependencies with `mix deps.get`
  * Create and migrate your database with `mix ecto.create && mix ecto.migrate`
  * Start Phoenix endpoint with `mix phoenix.server`

Now you can visit [`localhost:4000`](http://localhost:4000) from your browser.

Ready to run in production? Please [check our deployment guides](http://www.phoenixframework.org/docs/deployment).

## Learn more

  * Official website: http://www.phoenixframework.org/
  * Guides: http://phoenixframework.org/docs/overview
  * Docs: https://hexdocs.pm/phoenix
  * Mailing list: http://groups.google.com/group/phoenix-talk
  * Source: https://github.com/phoenixframework/phoenix
A project for live-reload functionality for [Phoenix](http://github.com/phoenixframework/phoenix) during development.

## Usage

You can use `phoenix_live_reload` in your projects by adding it to your `mix.exs` dependencies:

```elixir
def deps do
  [{:phoenix_live_reload, "~> 1.0"}]
end
```

## Backends

This project uses [`fs`](https://github.com/synrc/fs) as a dependency to watch your filesystem whenever there is a change and it supports the following operating systems:

* Linux via [inotify](https://github.com/rvoicilas/inotify-tools/wiki) (installation required)
* Windows via [inotify-win](https://github.com/thekid/inotify-win) (no installation required)
* Mac OS X via fsevents (no installation required)


## Skipping remote CSS reload

All stylesheets are reloaded without a page refresh anytime a style is detected as having changed. In certain cases such as serving stylesheets from a remote host, you may wish to prevent unnecessary reload of these stylesheets during development. For this, you can include a `data-no-reload` attribute on the link tag, ie:

    <link rel="stylesheet" href="http://example.com/style.css" data-no-reload>


## License

[Same license as Phoenix](https://github.com/phoenixframework/phoenix/blob/master/LICENSE.md).
## Phoenix.HTML

Collection of helpers to generate and manipulate HTML contents.

Although this project was originally extracted from Phoenix,
it does not depend on Phoenix and can be used with any Plug
application.

See the [docs](https://hexdocs.pm/phoenix_html/) for more information.

### Building phoenix_html.js

```bash
$ npm install
$ npm install -g brunch
$ brunch watch
```

## License

Copyright (c) 2014 Chris McCord

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Poolboy - A hunky Erlang worker pool factory

[![Build Status](https://api.travis-ci.org/devinus/poolboy.svg?branch=master)](https://travis-ci.org/devinus/poolboy)

[![Support via Gratipay](https://cdn.rawgit.com/gratipay/gratipay-badge/2.3.0/dist/gratipay.png)](https://gratipay.com/devinus/)

Poolboy is a **lightweight**, **generic** pooling library for Erlang with a
focus on **simplicity**, **performance**, and **rock-solid** disaster recovery.

## Usage

```erl-sh
1> Worker = poolboy:checkout(PoolName).
<0.9001.0>
2> gen_server:call(Worker, Request).
ok
3> poolboy:checkin(PoolName, Worker).
ok
```

## Example

This is an example application showcasing database connection pools using
Poolboy and [epgsql](https://github.com/epgsql/epgsql).

### example.app

```erlang
{application, example, [
    {description, "An example application"},
    {vsn, "0.1"},
    {applications, [kernel, stdlib, sasl, crypto, ssl]},
    {modules, [example, example_worker]},
    {registered, [example]},
    {mod, {example, []}},
    {env, [
        {pools, [
            {pool1, [
                {size, 10},
                {max_overflow, 20}
			], [
                {hostname, "127.0.0.1"},
                {database, "db1"},
                {username, "db1"},
                {password, "abc123"}
            ]},
            {pool2, [
                {size, 5},
                {max_overflow, 10}
			], [
                {hostname, "127.0.0.1"},
                {database, "db2"},
                {username, "db2"},
                {password, "abc123"}
            ]}
        ]}
    ]}
]}.
```

### example.erl

```erlang
-module(example).
-behaviour(application).
-behaviour(supervisor).

-export([start/0, stop/0, squery/2, equery/3]).
-export([start/2, stop/1]).
-export([init/1]).

start() ->
    application:start(?MODULE).

stop() ->
    application:stop(?MODULE).

start(_Type, _Args) ->
    supervisor:start_link({local, example_sup}, ?MODULE, []).

stop(_State) ->
    ok.

init([]) ->
    {ok, Pools} = application:get_env(example, pools),
    PoolSpecs = lists:map(fun({Name, SizeArgs, WorkerArgs}) ->
        PoolArgs = [{name, {local, Name}},
            		{worker_module, example_worker}] ++ SizeArgs,
        poolboy:child_spec(Name, PoolArgs, WorkerArgs)
    end, Pools),
    {ok, {{one_for_one, 10, 10}, PoolSpecs}}.

squery(PoolName, Sql) ->
    poolboy:transaction(PoolName, fun(Worker) ->
        gen_server:call(Worker, {squery, Sql})
    end).

equery(PoolName, Stmt, Params) ->
    poolboy:transaction(PoolName, fun(Worker) ->
        gen_server:call(Worker, {equery, Stmt, Params})
    end).
```

### example_worker.erl

```erlang
-module(example_worker).
-behaviour(gen_server).
-behaviour(poolboy_worker).

-export([start_link/1]).
-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2,
         code_change/3]).

-record(state, {conn}).

start_link(Args) ->
    gen_server:start_link(?MODULE, Args, []).

init(Args) ->
    process_flag(trap_exit, true),
    Hostname = proplists:get_value(hostname, Args),
    Database = proplists:get_value(database, Args),
    Username = proplists:get_value(username, Args),
    Password = proplists:get_value(password, Args),
    {ok, Conn} = epgsql:connect(Hostname, Username, Password, [
        {database, Database}
    ]),
    {ok, #state{conn=Conn}}.

handle_call({squery, Sql}, _From, #state{conn=Conn}=State) ->
    {reply, epgsql:squery(Conn, Sql), State};
handle_call({equery, Stmt, Params}, _From, #state{conn=Conn}=State) ->
    {reply, epgsql:equery(Conn, Stmt, Params), State};
handle_call(_Request, _From, State) ->
    {reply, ok, State}.

handle_cast(_Msg, State) ->
    {noreply, State}.

handle_info(_Info, State) ->
    {noreply, State}.

terminate(_Reason, #state{conn=Conn}) ->
    ok = epgsql:close(Conn),
    ok.

code_change(_OldVsn, State, _Extra) ->
    {ok, State}.
```

## Options

- `name`: the pool name
- `worker_module`: the module that represents the workers
- `size`: maximum pool size
- `max_overflow`: maximum number of workers created if pool is empty
- `strategy`: `lifo` or `fifo`, determines whether checked in workers should be
  placed first or last in the line of available workers. Default is `lifo`.

## Authors

- Devin Torres (devinus) <devin@devintorres.com>
- Andrew Thompson (Vagabond) <andrew@hijacked.us>
- Kurt Williams (onkel-dirtus) <kurt.r.williams@gmail.com>

## License

Poolboy is available in the public domain (see `UNLICENSE`).
Poolboy is also optionally available under the ISC license (see `LICENSE`),
meant especially for jurisdictions that do not recognize public domain works.
# Postgrex

[![Build Status](https://travis-ci.org/elixir-ecto/postgrex.svg?branch=master)](https://travis-ci.org/elixir-ecto/postgrex)

PostgreSQL driver for Elixir.

Documentation: http://hexdocs.pm/postgrex/

## Example

```iex
iex> {:ok, pid} = Postgrex.start_link(hostname: "localhost", username: "postgres", password: "postgres", database: "postgres")
{:ok, #PID<0.69.0>}
iex> Postgrex.query!(pid, "SELECT user_id, text FROM comments", [])
%Postgrex.Result{command: :select, empty?: false, columns: ["user_id", "text"], rows: [[3,"hey"],[4,"there"]], size: 2}}
iex> Postgrex.query!(pid, "INSERT INTO comments (user_id, text) VALUES (10, 'heya')", [])
%Postgrex.Result{command: :insert, columns: nil, rows: nil, num_rows: 1}}
```

## Features

  * Automatic decoding and encoding of Elixir values to and from PostgreSQL's binary format
  * User defined extensions for encoding and decoding any PostgreSQL type
  * Supports transactions, prepared queries and multiple pools via [DBConnection](https://github.com/elixir-ecto/db_connection)
  * Supports PostgreSQL 8.4 and 9.0-9.6 (hstore is not supported on 8.4)

## Data representation

    PostgreSQL      Elixir
    ----------      ------
    NULL            nil
    bool            true | false
    char            "é"
    int             42
    float           42.0
    text            "eric"
    bytea           <<42>>
    numeric         #Decimal<42.0> *
    date            %Postgrex.Date{year: 2013, month: 10, day: 12}
    time(tz)        %Postgrex.Time{hour: 0, min: 37, sec: 14, usec: 0} **
    timestamp(tz)   %Postgrex.Timestamp{year: 2013 month: 10, day: 12, hour: 0, min: 37, sec: 14, usec: 0} **
    interval        %Postgrex.Interval{months: 14, days: 40, secs: 10920}
    array           [1, 2, 3]
    composite type  {42, "title", "content"}
    range           %Postgrex.Range{lower: 1, upper: 5}
    uuid            <<160,238,188,153,156,11,78,248,187,109,107,185,189,56,10,17>>
    hstore          %{"foo" => "bar"}
    oid types       42
    enum            "ok" ***
    bit             << 1::1, 0::1 >>
    varbit          << 1::1, 0::1 >>
    tsvector        [%Postgrex.Lexeme{positions: [{1, :A}], word: "a"}]

\* [Decimal](http://github.com/ericmj/decimal)

\*\* Timezones will always be normalized to UTC or assumed to be UTC when no information is available, either by PostgreSQL or Postgrex

\*\*\* Enumerated types (enum) are custom named database types with strings as values.

Postgrex does not automatically cast between types. For example, you can't pass a string where a date is expected. To add type casting, support new types, or change how any of the types above are encoded/decoded, you can use extensions.

## Extensions

Extensions are used to extend Postgrex' built-in type encoding/decoding.

Here is a [JSON extension](https://github.com/elixir-ecto/postgrex/blob/master/lib/postgrex/extensions/json.ex) that supports encoding/decoding Elixir maps to the Postgres' JSON type.

Extensions can be specified and configured when building custom type modules. For example, if you want to different a JSON encoder/decode, you can define a new type module as below.

```elixir
# Postgrex.Types.define(module_name, extra_extensions, options)
Postgrex.Types.define(MyApp.PostgrexTypes, [], json: AnotherJSONLib)
```

`Postgrex.Types.define/3` must be called on its own file, outside of any module and function, as it only needs to be defined once during compilation.

Once a type module is defined, you must specify it on `start_link`:

```elixir
Postgrex.start_link(types: MyApp.PostgrexTypes)
```

## OID type encoding

PostgreSQL's wire protocol supports encoding types either as text or as binary. Unlike most client libraries Postgrex uses the binary protocol, not the text protocol. This allows for efficient encoding of types (e.g. 4-byte integers are encoded as 4 bytes, not as a string of digits) and automatic support for arrays and composite types.

Unfortunately the PostgreSQL binary protocol transports [OID types](http://www.postgresql.org/docs/current/static/datatype-oid.html#DATATYPE-OID-TABLE) as integers while the text protocol transports them as string of their name, if one exists, and otherwise as integer.

This means you either need to supply oid types as integers or perform an explicit cast (which would be automatic when using the text protocol) in the query.

```elixir
# Fails since $1 is regclass not text.
query("select nextval($1)", ["some_sequence"])

# Perform an explicit cast, this would happen automatically when using a
# client library that uses the text protocol.
query("select nextval($1::text::regclass)", ["some_sequence"])

# Determine the oid once and store it for later usage. This is the most
# efficient way, since PostgreSQL only has to perform the lookup once. Client
# libraries using the text protocol do not support this.
%{rows: [{sequence_oid}]} = query("select $1::text::regclass", ["some_sequence"])
query("select nextval($1)", [sequence_oid])
```

## PgBouncer

When using PgBouncer with transaction or statement pooling named prepared
queries can not be used because the bouncer may route requests from the same
postgrex connection to different PostgreSQL backend processes and discards named
queries after the transactions closes. To force unnamed prepared queries:

```elixir
Postgrex.start_link(prepare: :unnamed)
```

## Contributing

To contribute you need to compile Postgrex from source and test it:

```
$ git clone https://github.com/elixir-ecto/postgrex.git
$ cd postgrex
$ mix test
```

The tests requires some modifications to your [hba file](http://www.postgresql.org/docs/9.3/static/auth-pg-hba-conf.html). The path to it can be found by running `$ psql -U postgres -c "SHOW hba_file"` in your shell. Put the following above all other configurations (so that they override):

```
host    all             postgrex_md5_pw         127.0.0.1/32    md5
host    all             postgrex_cleartext_pw   127.0.0.1/32    password
```

The server needs to be restarted for the changes to take effect. Additionally you need to setup a Postgres user with the same username as the local user and give it trust or ident in your hba file. Or you can export $PGUSER and $PGPASSWORD before running tests.

### Testing hstore on 9.0

Postgres versions 9.0 does not have the `CREATE EXTENSION` commands. This means we have to locate the postgres installation and run the `hstore.sql` in `contrib` to install `hstore`. Below is an example command to test 9.0 on OS X with homebrew installed postgres:

```
$ PGVERSION=9.0 PGPATH=/usr/local/share/postgresql9/ mix test
```

## License

Copyright 2013 Eric Meadows-Jönsson

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# MIME

A library that maps mime types to extensions and vice-versa.

## Installation

The package can be installed as:

1. Add mime to your list of dependencies in `mix.exs`:

  ```elixir
  def deps do
    [{:mime, "~> 1.1"}]
  end
  ```

2. If there is an `applications` key in your `mix.exs`, add `:mime` to the list. This step is not necessary if you have `extra_applications` instead.

  ```elixir
  def application do
    [applications: [:mime]]
  end
  ```
  
## Usage

MIME types can be extended in your application `config/config.exs` as follows:

```elixir
config :mime, :types, %{
  "application/vnd.api+json" => ["json-api"]
}
```

And then run `mix deps.clean --build mime` to force mime to be recompiled across all environments.

## License

MIME source code is released under Apache 2 License.

Check LICENSE file for more information.
A project that integrates [Phoenix](http://github.com/phoenixframework/phoenix) with [Ecto](http://github.com/elixir-lang/ecto), implementing all relevant protocols.

## Usage

You can use `phoenix_ecto` in your projects in two steps:

1. Add it to your `mix.exs` dependencies:

    ```elixir
    def deps do
      [{:phoenix_ecto, "~> 3.0"}]
    end
    ```

2. List it as your application dependency:

    ```elixir
    def application do
      [applications: [:logger, :phoenix_ecto]]
    end
    ```

## Concurrent browser tests

This library also provides a plug called `Phoenix.Ecto.SQL.Sandbox` that allows developers to run acceptance tests powered by headless browsers such as Phantom.js and Selenium concurrently. If you are not familiar with Ecto's SQL sandbox, we recommend you to first get acquainted with it by [reading `Ecto.Adapters.SQL.Sandbox` documentation](https://hexdocs.pm/ecto/Ecto.Adapters.SQL.Sandbox.html).

To enable concurrent acceptance tests, make sure you are using PostgreSQL and follow the instructions below:

  1. Set a flag to enable the sandbox in `config/test.exs`:

    ```elixir
    config :your_app, sql_sandbox: true
    ```

  2. And use the flag to conditionally add the plug to `lib/your_app/endpoint.ex`:

    ```elixir
    if Application.get_env(:your_app, :sql_sandbox) do
      plug Phoenix.Ecto.SQL.Sandbox
    end
    ```

    Make sure that this is placed **before** the line `plug YourApp.Router` (or any other plug that may access the database).

You can now checkout a sandboxed connection and pass the connection information to an acceptance testing tool like [Hound](https://github.com/hashnuke/hound) or [Wallaby](https://github.com/keathley/wallaby).

### Hound

To write concurrent acceptance tests with Hound, first add it as a dependency to your `mix.exs`:

```elixir
{:hound, "~> 1.0"}
```

Make sure to start it at the top of your `test/test_helper.exs`:

```elixir
{:ok, _} = Application.ensure_all_started(:hound)
```

Then add the following to your test case (or to your case template):

```elixir
use Hound.Helpers

setup do
  :ok = Ecto.Adapters.SQL.Sandbox.checkout(YourApp.Repo)
  metadata = Phoenix.Ecto.SQL.Sandbox.metadata_for(YourApp.Repo, self())
  Hound.start_session(metadata: metadata)
end
```

Hound supports multiple drivers like Chrome, Firefox, etc but it does not support concurrent tests under PhantomJS (the default).

### Wallaby

To write concurrent acceptance tests with Wallaby, first add it as a dependency to your `mix.exs`:

```elixir
{:wallaby, "~> 0.6"}
```

Make sure to start it at the top of your `test/test_helper.exs`:

```elixir
{:ok, _} = Application.ensure_all_started(:wallaby)
```

Then add the following to your test case (or to your case template):

```elixir
use Wallaby.DSL

setup do
  :ok = Ecto.Adapters.SQL.Sandbox.checkout(YourApp.Repo)
  metadata = Phoenix.Ecto.SQL.Sandbox.metadata_for(YourApp.Repo, self())
  {:ok, session} = Wallaby.start_session(metadata: metadata)
end
```

Wallaby currently supports PhantomJS (including concurrent tests). Support for other drivers may be added in the future.

## The Phoenix <-> Ecto integration

Thanks to Elixir protocols, the integration between Phoenix and Ecto is simply a matter of implementing a handful of protocols. We provide the following implementations:

  * `Phoenix.HTML.FormData` protocol for `Ecto.Changeset`
  * `Phoenix.HTML.Safe` protocol for `Decimal`, `Ecto.Date`, `Ecto.Time` and `Ecto.DateTime`
  * `Plug.Exception` protocol for the relevant Ecto exceptions

## License

Same license as Phoenix.
# DBConnection

Database connection behaviour and database connection pool designed for
handling transaction, prepare/execute, cursors and client process
describe/encode/decode.

Four pool implementations are provided: `DBConnection.Connection`
(default/single connection), `DBConnection.Poolboy` (poolboy pool),
`DBConnection.Sojourn` (sbroker pool) and `DBConnection.Ownership`
(ownership pool).

Examples of using the `DBConnection` behaviour are available in
`./examples/db_agent/` and `./examples/tcp_connection/`.

## License

Copyright 2015 James Fish

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# Decimal

[![Build Status](https://travis-ci.org/ericmj/decimal.svg?branch=master)](https://travis-ci.org/ericmj/decimal)

Arbitrary precision decimal arithmetic for Elixir.

Documentation: http://hexdocs.pm/decimal/

## Usage

Add Decimal as a dependency in your `mix.exs` file.

```elixir
def deps do
  [{:decimal, "~> 1.0"}]
end
```

After you are done, run `mix deps.get` in your shell to fetch and compile Decimal. Start an interactive Elixir shell with `iex -S mix`.

```elixir
iex> alias Decimal, as: D
nil
iex> D.add(D.new(6), D.new(7))
#Decimal<13>
iex> D.div(D.new(1), D.new(3))
#Decimal<0.333333333>
```

## Examples

### Using the context

The context specifies the maximum precision of the result of calculations and
the rounding algorithm if the result has a higher precision than the specified
maximum. It also holds the list of set of trap enablers and the currently set
flags.

The context is stored in the process dictionary, this means that you don't have
to pass the context around explicitly and the flags will be updated
automatically.

The context is accessed with `Decimal.get_context/0` and set with
`Decimal.set_context/1`. It can also be temporarily set with
`Decimal.with_context/2`.

```elixir
iex> D.get_context
%Decimal.Context{flags: [:rounded, :inexact], precision: 9, rounding: :half_up,
 traps: [:invalid_operation, :division_by_zero]}
iex> D.with_context %D.Context{precision: 2}, fn -> IO.inspect D.get_context end
%Decimal.Context{flags: [], precision: 2, rounding: :half_up,
 traps: [:invalid_operation, :division_by_zero]}
%Decimal.Context{flags: [], precision: 2, rounding: :half_up,
 traps: [:invalid_operation, :division_by_zero]}
iex> D.set_context(%D.Context{D.get_context | traps: []})
:ok
iex> Decimal.get_context
%Decimal.Context{flags: [:rounded, :inexact], precision: 9, rounding: :half_up,
 traps: []}
```

### Precision and rounding

The precision is used to limit the amount of decimal digits in the coefficient:

```elixir
iex> D.set_context(%D.Context{D.get_context | precision: 9})
:ok
iex> D.div(D.new(1), D.new(3))
#Decimal<0.333333333>
iex> D.set_context(%D.Context{D.get_context | precision: 2})
:ok
iex> D.div(D.new(1), D.new(3))
#Decimal<0.33>
```

The rounding algorithm specifies how the result of an operation shall be rounded
when it get be represented with the current precision:

```elixir
iex> D.set_context(%D.Context{D.get_context | rounding: :half_up})
:ok
iex> D.div(D.new(31), D.new(2))
#Decimal<16>
iex> D.set_context(%D.Context{D.get_context | rounding: :floor})
:ok
iex> D.div(D.new(31), D.new(2))
#Decimal<15>
```

### Flags and trap enablers

When an exceptional condition is signalled its flag is set in the context and if
if the trap enabler is set `Decimal.Error` will be raised.

```elixir
iex> D.set_context(%D.Context{D.get_context | rounding: :floor, precision: 2})
:ok
iex> D.get_context.traps
[:invalid_operation, :division_by_zero]
iex> D.get_context.flags
[]
iex> D.div(D.new(31), D.new(2))
#Decimal<15>
iex> D.get_context.flags
[:inexact, :rounded]
```

`:inexact` and `:rounded` were signaled above because the result of the
operation was inexact given the context's precision and had to be rounded to fit
the precision. `Decimal.Error` was not raised because the signals' trap enablers
weren't set. We can, however, set the trap enabler if we what this condition to
raise.

```elixir
iex> D.set_context(%D.Context{D.get_context | traps: D.get_context.traps ++ [:inexact]})
:ok
iex> D.div(D.new(31), D.new(2))
** (Decimal.Error)
```

The default trap enablers, such as `:division_by_zero` can be unset:

```elixir
iex> D.get_context.traps
[:invalid_operation, :division_by_zero]
iex> D.div(D.new(42), D.new(0))
** (Decimal.Error)
iex>  D.set_context(%D.Context{D.get_context | traps: [], flags: []})
:ok
iex> D.div(D.new(42), D.new(0))
#Decimal<Infinity>
iex> D.get_context.flags
[:division_by_zero]
```

### Mitigating rounding errors

TODO

## License

   Copyright 2013 Eric Meadows-Jönsson

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
# Ecto

[![Build Status](https://travis-ci.org/elixir-ecto/ecto.svg?branch=master)](https://travis-ci.org/elixir-ecto/ecto)
[![Inline docs](http://inch-ci.org/github/elixir-ecto/ecto.svg?branch=master&style=flat)](http://inch-ci.org/github/elixir-ecto/ecto)
[![Ebert](https://ebertapp.io/github/elixir-ecto/ecto.svg)](https://ebertapp.io/github/elixir-ecto/ecto)

Ecto is a domain specific language for writing queries and interacting with databases in Elixir. Here is an example:

```elixir
# In your config/config.exs file
config :my_app, ecto_repos: [Sample.Repo]

config :my_app, Sample.Repo,
  adapter: Ecto.Adapters.Postgres,
  database: "ecto_simple",
  username: "postgres",
  password: "postgres",
  hostname: "localhost",
  port: "5432"

# In your application code
defmodule Sample.Repo do
  use Ecto.Repo,
    otp_app: :my_app
end

defmodule Sample.Weather do
  use Ecto.Schema

  schema "weather" do
    field :city     # Defaults to type :string
    field :temp_lo, :integer
    field :temp_hi, :integer
    field :prcp,    :float, default: 0.0
  end
end

defmodule Sample.App do
  import Ecto.Query
  alias Sample.Weather
  alias Sample.Repo

  def keyword_query do
    query = from w in Weather,
         where: w.prcp > 0 or is_nil(w.prcp),
         select: w
    Repo.all(query)
  end

  def pipe_query do
    Weather
    |> where(city: "Kraków")
    |> order_by(:temp_lo)
    |> limit(10)
    |> Repo.all
  end
end
```

See the [getting started guide](http://hexdocs.pm/ecto/getting-started.html) and the [online documentation](http://hexdocs.pm/ecto).

Also checkout the ["What's new in Ecto 2.0"](http://pages.plataformatec.com.br/ebook-whats-new-in-ecto-2-0) free ebook to learn more about many features in Ecto 2.0 such as `many_to_many`, schemaless queries, concurrent testing and more.

## Usage

You need to add both Ecto and the database adapter as a dependency to your `mix.exs` file. The supported databases and their adapters are:

Database   | Ecto Adapter           | Dependency                   | Ecto 2.0 compatible?
:----------| :--------------------- | :----------------------------| :-------------------
PostgreSQL | Ecto.Adapters.Postgres | [postgrex][postgrex]         | Yes
MySQL      | Ecto.Adapters.MySQL    | [mariaex][mariaex]           | Yes
MSSQL      | Tds.Ecto               | [tds_ecto][tds_ecto]         | No
SQLite3    | Sqlite.Ecto            | [sqlite_ecto][sqlite_ecto]   | No
MongoDB    | Mongo.Ecto             | [mongodb_ecto][mongodb_ecto] | No

[postgrex]: http://github.com/ericmj/postgrex
[mariaex]: http://github.com/xerions/mariaex
[tds_ecto]: https://github.com/livehelpnow/tds_ecto
[sqlite_ecto]: https://github.com/jazzyb/sqlite_ecto
[mongodb_ecto]: https://github.com/michalmuskala/mongodb_ecto

For example, if you want to use PostgreSQL, add to your `mix.exs` file:

```elixir
defp deps do
  [{:postgrex, ">= 0.0.0"},
   {:ecto, "~> 2.1"}]
end
```

and update your applications list to include both projects:

```elixir
def application do
  [applications: [:postgrex, :ecto]]
end
```

Then run `mix deps.get` in your shell to fetch the dependencies. If you want to use another database, just choose the proper dependency from the table above.

Finally, in the repository configuration, you will need to specify the `adapter:` respective to the chosen dependency. For PostgreSQL it is:

```elixir
config :my_app, Repo,
  adapter: Ecto.Adapters.Postgres,
  ...
```

We are currently looking for contributions to add support for other SQL databases and folks interested in exploring non-relational databases too.

## Important links

  * [Documentation](http://hexdocs.pm/ecto)
  * [Mailing list](https://groups.google.com/forum/#!forum/elixir-ecto)
  * [Examples](https://github.com/elixir-ecto/ecto/tree/master/examples)

## Contributing

Contributions are welcome! In particular, remember to:

* Do not use the issues tracker for help or support requests (try Stack Overflow, IRC or mailing lists, etc).
* For proposing a new feature, please start a discussion on [elixir-ecto](https://groups.google.com/forum/#!forum/elixir-ecto).
* For bugs, do a quick search in the issues tracker and make sure the bug has not yet been reported.
* Finally, be nice and have fun! Remember all interactions in this project follow the same [Code of Conduct as Elixir](https://github.com/elixir-lang/elixir/blob/master/CODE_OF_CONDUCT.md).

### Running tests

Clone the repo and fetch its dependencies:

```
$ git clone https://github.com/elixir-ecto/ecto.git
$ cd ecto
$ mix deps.get
$ mix test
```

Besides the unit tests above, it is recommended to run the adapter integration tests too:

```
# Run only PostgreSQL tests (PostgreSQL >= 9.5 is preferred for testing all Postgres features)
MIX_ENV=pg mix test

# Run all tests (unit and all adapters)
mix test.all
```

### Building docs

```
$ MIX_ENV=docs mix docs
```

## Copyright and License

Copyright (c) 2012, Plataformatec.

Ecto source code is licensed under the [Apache 2 License](LICENSE.md).
# Plug

[![Build Status](https://travis-ci.org/elixir-lang/plug.svg?branch=master)](https://travis-ci.org/elixir-lang/plug)
[![Inline docs](http://inch-ci.org/github/elixir-lang/plug.svg?branch=master)](http://inch-ci.org/github/elixir-lang/plug)

Plug is:

1. A specification for composable modules between web applications
2. Connection adapters for different web servers in the Erlang VM

[Documentation for Plug is available online](http://hexdocs.pm/plug/).

## Hello world

```elixir
defmodule MyPlug do
  import Plug.Conn

  def init(options) do
    # initialize options

    options
  end

  def call(conn, _opts) do
    conn
    |> put_resp_content_type("text/plain")
    |> send_resp(200, "Hello world")
  end
end
```

The snippet above shows a very simple example on how to use Plug. Save that snippet to a file and run it inside the plug application with:

    $ iex -S mix
    iex> c "path/to/file.ex"
    [MyPlug]
    iex> {:ok, _} = Plug.Adapters.Cowboy.http MyPlug, []
    {:ok, #PID<...>}

Access "http://localhost:4000/" and we are done! For now, we have directly started the server in our terminal but, for production deployments, you likely want to start it in your supervision tree. See the "Supervised handlers" section below.

## Installation

You can use plug in your projects in two steps:

1. Add plug and your webserver of choice (currently cowboy) to your `mix.exs` dependencies:

    ```elixir
    def deps do
      [{:cowboy, "~> 1.0.0"},
       {:plug, "~> 1.0"}]
    end
    ```

2. List both `:cowboy` and `:plug` as your application dependencies:

    ```elixir
    def application do
      [applications: [:cowboy, :plug]]
    end
    ```

## The Plug.Conn

In the hello world example, we defined our first plug. What is a plug after all?

A plug takes two shapes. A function plug receives a connection and a set of options as arguments and returns the connection:

```elixir
def hello_world_plug(conn, _opts) do
  conn
  |> put_resp_content_type("text/plain")
  |> send_resp(200, "Hello world")
end
```

A module plug implements an `init/1` function to initialize the options and a `call/2` function which receives the connection and initialized options and returns the connection:

```elixir
defmodule MyPlug do
  def init([]), do: false
  def call(conn, _opts), do: conn
end
```

As per the specification above, a connection is represented by the `Plug.Conn` struct:

```elixir
%Plug.Conn{host: "www.example.com",
           path_info: ["bar", "baz"],
           ...}
```

Data can be read directly from the connection and also pattern matched on. Manipulating the connection often happens with the use of the functions defined in the `Plug.Conn` module. In our example, both `put_resp_content_type/2` and `send_resp/3` are defined in `Plug.Conn`.

Remember that, as everything else in Elixir, **a connection is immutable**, so every manipulation returns a new copy of the connection:

```elixir
conn = put_resp_content_type(conn, "text/plain")
conn = send_resp(conn, 200, "ok")
conn
```

Finally, keep in mind that a connection is a **direct interface to the underlying web server**. When you call `send_resp/3` above, it will immediately send the given status and body back to the client. This makes features like streaming a breeze to work with.

## The Plug Router

In practice, developers rarely write their own plugs. For example, Plug ships with a router that allows developers to quickly match on incoming requests and perform some action:

```elixir
defmodule MyRouter do
  use Plug.Router

  plug :match
  plug :dispatch

  get "/hello" do
    send_resp(conn, 200, "world")
  end

  forward "/users", to: UsersRouter

  match _ do
    send_resp(conn, 404, "oops")
  end
end
```

The router is a plug and, not only that, it contains its own plug pipeline too. The example above says that when the router is invoked, it will invoke the `:match` plug, represented by a local `match/2` function, and then call the `:dispatch` plug which will execute the matched code.

Plug ships with many plugs that you can add to the router plug pipeline, allowing you to plug something before a route matches or before a route is dispatched to. For example, if you want to add logging to the router, just do:

```elixir
plug Plug.Logger
plug :match
plug :dispatch
```

Note `Plug.Router` compiles all of your routes into a single function and relies on the Erlang VM to optimize the underlying routes into a tree lookup, instead of a linear lookup that would instead match route-per-route. This means route lookups are extremely fast in Plug!

This also means that a catch all `match` is recommended to be defined, as in the example above, otherwise routing fails with a function clause error (as it would in any regular Elixir function).

Each route needs to return the connection as per the Plug specification. See `Plug.Router` docs for more information.

## Supervised handlers

On a production system, you likely want to start your Plug application under your application's supervision tree. Plug provides the `child_spec/3` function to do just that. Start a new Elixir project with the `--sup` flag:

```elixir
$ mix new my_app --sup
```

and then update `lib/my_app.ex` as follows:

```elixir
defmodule MyApp do
  use Application

  # See https://hexdocs.pm/elixir/Application.html
  # for more information on OTP Applications
  def start(_type, _args) do
    import Supervisor.Spec

    children = [
      # Define workers and child supervisors to be supervised
      Plug.Adapters.Cowboy.child_spec(:http, MyRouter, [], [port: 4001])
    ]

    # See https://hexdocs.pm/elixir/Supervisor.html
    # for other strategies and supported options
    opts = [strategy: :one_for_one, name: MyApp.Supervisor]
    Supervisor.start_link(children, opts)
  end
end
```

## Testing plugs

Plug ships with a `Plug.Test` module that makes testing your plugs easy. Here is how we can test the router from above (or any other plug):

```elixir
defmodule MyPlugTest do
  use ExUnit.Case, async: true
  use Plug.Test

  @opts AppRouter.init([])

  test "returns hello world" do
    # Create a test connection
    conn = conn(:get, "/hello")

    # Invoke the plug
    conn = AppRouter.call(conn, @opts)

    # Assert the response and status
    assert conn.state == :sent
    assert conn.status == 200
    assert conn.resp_body == "world"
  end
end
```

### Available Plugs

This project aims to ship with different plugs that can be re-used across applications:

  * `Plug.CSRFProtection` - adds Cross-Site Request Forgery protection to your application. Typically required if you are using `Plug.Session`;
  * `Plug.Head` - converts HEAD requests to GET requests;
  * `Plug.Logger` - logs requests;
  * `Plug.MethodOverride` - overrides a request method with one specified in headers;
  * `Plug.Parsers` - responsible for parsing the request body given its content-type;
  * `Plug.RequestId` - sets up a request ID to be used in logs;
  * `Plug.Session` - handles session management and storage;
  * `Plug.SSL` - enforce requests through SSL;
  * `Plug.Static` - serves static files;

You can go into more details about each of them [in our docs](http://hexdocs.pm/plug/).

### Helper modules

Modules that can be used after you use `Plug.Router` or `Plug.Builder` to help development:

  * `Plug.Debugger` - shows a helpful debugging page every time there is a failure in a request;
  * `Plug.ErrorHandler` - allows developers to customize error pages in case of crashes instead of sending a blank one;

## Contributing

We welcome everyone to contribute to Plug and help us tackle existing issues!

Use the [issue tracker][issues] for bug reports or feature requests. You may also start a discussion on the [mailing list][ML] or the **[#elixir-lang][IRC]** channel on [Freenode][freenode] IRC. Open a [pull request][pulls] when you are ready to contribute.

When submitting a pull request you should not update the `CHANGELOG.md`.

If you are planning to contribute documentation, [please check our best practices for writing documentation][writing-docs].

Finally, remember all interactions in our official spaces follow our [Code of Conduct][code-of-conduct].

## License

Plug source code is released under Apache 2 License.
Check LICENSE file for more information.

  [issues]: https://github.com/elixir-lang/plug/issues
  [pulls]: https://github.com/elixir-lang/plug/pulls
  [ML]: https://groups.google.com/group/elixir-lang-core
  [code-of-conduct]: https://github.com/elixir-lang/elixir/blob/master/CODE_OF_CONDUCT.md
  [writing-docs]: http://elixir-lang.org/docs/stable/elixir/writing-documentation.html
  [IRC]: https://webchat.freenode.net/?channels=#elixir-lang
  [freenode]: http://www.freenode.net
Cowlib
======

Cowlib is a support library for manipulating Web protocols.

Goals
-----

Cowlib provides libraries for parsing and building messages
for various Web protocols, including SPDY, HTTP and Websocket.

It is optimized for completeness rather than speed. No value
is ignored, they are all returned.

Support
-------

 *  Official IRC Channel: #ninenines on irc.freenode.net
 *  [Mailing Lists](http://lists.ninenines.eu)
 *  [Commercial Support](http://ninenines.eu/support)
# Phoenix.PubSub
> Distributed PubSub and Presence platform for the Phoenix Framework

[![Build Status](https://api.travis-ci.org/phoenixframework/phoenix_pubsub.svg)](https://travis-ci.org/phoenixframework/phoenix_pubsub)


## Installation


  1. Add phoenix_pubsub to your list of dependencies in `mix.exs`:

  ```elixir
  def deps do
    [{:phoenix_pubsub, "~> 1.0"}]
  end
  ```

  2. Ensure phoenix_pubsub is started before your application:

  ```elixir
  def application do
    [applications: [:phoenix_pubsub]]
  end
  ```


## Testing

Testing by default spawns nodes internally for distributed tests.
To run tests that do not require clustering, exclude  the `clustered` tag:

    $ mix test --exclude clustered

If you have issues running the clustered tests try running:

    $ epmd -daemon

before running the tests.
Cowboy
======

Cowboy is a small, fast and modular HTTP server written in Erlang.

Goals
-----

Cowboy aims to provide a **complete** HTTP stack in a **small** code base.
It is optimized for **low latency** and **low memory usage**, in part
because it uses **binary strings**.

Cowboy provides **routing** capabilities, selectively dispatching requests
to handlers written in Erlang.

Because it uses Ranch for managing connections, Cowboy can easily be
**embedded** in any other application.

No parameterized module. No process dictionary. **Clean** Erlang code.

Sponsors
--------

The SPDY implementation was sponsored by
[LeoFS Cloud Storage](http://www.leofs.org).

The project is currently sponsored by
[Kato.im](https://kato.im).

Online documentation
--------------------

 *  [User guide](http://ninenines.eu/docs/en/cowboy/HEAD/guide)
 *  [Function reference](http://ninenines.eu/docs/en/cowboy/HEAD/manual)

Offline documentation
---------------------

 *  While still online, run `make docs`
 *  Function reference man pages available in `doc/man3/` and `doc/man7/`
 *  Run `make install-docs` to install man pages on your system
 *  Full documentation in Markdown available in `doc/markdown/`
 *  Examples available in `examples/`

Getting help
------------

 *  Official IRC Channel: #ninenines on irc.freenode.net
 *  [Mailing Lists](http://lists.ninenines.eu)
 *  [Commercial Support](http://ninenines.eu/support)
= Ranch

Ranch is a socket acceptor pool for TCP protocols.

== Goals

Ranch aims to provide everything you need to accept TCP connections with
a **small** code base and **low latency** while being easy to use directly
as an application or to **embed** into your own.

Ranch provides a **modular** design, letting you choose which transport
and protocol are going to be used for a particular listener. Listeners
accept and manage connections on one port, and include facilities to
limit the number of **concurrent** connections. Connections are sorted
into **pools**, each pool having a different configurable limit.

Ranch also allows you to **upgrade** the acceptor pool without having
to close any of the currently opened sockets.

== Online documentation

* http://ninenines.eu/docs/en/ranch/1.3/guide[User guide]
* http://ninenines.eu/docs/en/ranch/1.3/manual[Function reference]

== Offline documentation

* While still online, run `make docs`
* User guide available in `doc/` in PDF and HTML formats
* Function reference man pages available in `doc/man3/` and `doc/man7/`
* Run `make install-docs` to install man pages on your system
* Full documentation in Asciidoc available in `doc/src/`
* Examples available in `examples/`

== Support

* Official IRC Channel: #ninenines on irc.freenode.net
* https://github.com/ninenines/ranch/issues[Issues tracker]
* http://ninenines.eu/services[Commercial Support]
# Gettext

[![Build Status](https://travis-ci.org/elixir-lang/gettext.svg)](https://travis-ci.org/elixir-lang/gettext)

`gettext` is an internationalization (i18n) and localization (l10n) system commonly used for writing multilingual programs. Gettext is a standard for i18n in different communities, meaning there is a great set of tooling for developers and translators.

## Installation

  1. Add `:gettext` to your list of dependencies in mix.exs:

    ```elixir
    def deps do
      [{:gettext, "~> 0.13"}]
    end
    ```

  2. Ensure `:gettext` is started before your application:

    ```elixir
    def application do
      [applications: [:gettext, :logger]]
    end
    ```

  3. Optional: add the `:gettext` compiler so your backends
    are recompiled when `.po` files change:

    ```elixir
    def project do
      [compilers: [:gettext] ++ Mix.compilers]
    end
    ```

[Documentation for `Gettext` is available on Hex][docs-gettext].

## Usage

To use gettext, you must define a gettext module:

```elixir
defmodule MyApp.Gettext do
  use Gettext, otp_app: :my_app
end
```

And invoke the gettext API, based on the `*gettext` functions:

```elixir
import MyApp.Gettext

# Simple translation
gettext "Here is one string to translate"

# Plural translation
number_of_apples = 4
ngettext "The apple is ripe",
         "The apples are ripe",
         number_of_apples
#=> "The apples are ripe"

# Domain-based translation
dgettext "errors", "Here is an error message to translate"
```

Translations in gettext are stored in Portable Object files (`.po`). Such files must be placed at `priv/gettext/en/LC_MESSAGES/domain.po`, where `en` is the locale and `domain` is the domain (the default domain is called `default`).

For example, the translation to `pt_BR` of the first two `*gettext` calls in the snippet above must be placed in the `priv/gettext/pt_BR/LC_MESSAGES/default.po` file with contents:

```pot
msgid "Here is one string to translate"
msgstr "Aqui está um texto para traduzir"

msgid "Here is the string to translate"
msgid_plural "Here are the strings to translate"
msgstr[0] "Aqui está o texto para traduzir"
msgstr[1] "Aqui estão os textos para traduzir"
```

`.po` are text based and can be edited directly by translators. Some may even use existing tools for managing them, such as [Poedit][poedit] or [poeditor.com][poeditor.com].

Finally, because translations are based on strings, your source code does not lose readability as you still see literal strings, like `gettext "here is an example"`, instead of paths like `translate "some.path.convention"`.

Read the [documentation for the `Gettext` module][docs-gettext-module] for more information on locales, interpolation, pluralization and other features.

## Workflow

`gettext` is able to automatically extract translations from your source code, alleviating developers and translators from the repetitive and error-prone work of maintaining translation files.

When extracted from source, translations are placed into `.pot` files, which are template files. Those templates files can then be merged into translation files for each specific locale your application is being currently translated to.

In other words, the typical workflow looks like this:

  1. Add `gettext` calls to your source code. No need to touch translation files
     at this point as gettext will return the given string if no translation is
     available:

        gettext "Welcome back!"

  2. Once changes to the source are complete, run `mix gettext.extract` to automatically sync all existing entries to `.pot` (template files) in `priv/gettext`:

        mix gettext.extract

  3. `.pot` files can then be merged into locale-specific `.po` files with `mix gettext.merge`:

        # Merge .pot into all locales
        mix gettext.merge priv/gettext

        # Merge .pot into one specific locale
        mix gettext.merge priv/gettext --locale en

It is also possible to execute both the extract and merge operations in one step with `mix gettext.extract --merge`.

## License

Copyright 2015 Plataformatec

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.

[docs-gettext]: http://hexdocs.pm/gettext
[docs-gettext-module]: http://hexdocs.pm/gettext/Gettext.html
[poedit]: http://poedit.net/
[poeditor.com]: https://poeditor.com
![phoenix logo](https://raw.githubusercontent.com/phoenixframework/phoenix/master/priv/static/phoenix.png)
> ### Productive. Reliable. Fast.
> A productive web framework that does not compromise speed and maintainability.

[![Build Status](https://api.travis-ci.org/phoenixframework/phoenix.svg)](https://travis-ci.org/phoenixframework/phoenix)
[![Inline docs](http://inch-ci.org/github/phoenixframework/phoenix.svg)](http://inch-ci.org/github/phoenixframework/phoenix)

## Getting started

See the official site at http://www.phoenixframework.org/

## Documentation

API documentation is available at [https://hexdocs.pm/phoenix](https://hexdocs.pm/phoenix)

## Contributing

We appreciate any contribution to Phoenix. Check our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) and [CONTRIBUTING.md](CONTRIBUTING.md) guides for more information. We usually keep a list of features and bugs [in the issue tracker][4].

### Generating a Phoenix project from unreleased versions

In order to create a new project using the latest Phoenix source installer (the `phoenix.new` Mix task) you will need to ensure two things.

1. Remove any previously installed `phoenix_new` archives so that Mix will pick up the local source code. This can be done with `mix archive.uninstall phoenix_new.ez` or by simply deleting the file, which is usually in `~/.mix/archives/`.
2. Run the command from within the `installer` directory and provide a subdirectory within the installer to generate your dev project. The command below will create a new project using your current Phoenix checkout, thanks to the `--dev` flag.

```bash
$ cd installer
$ mix phoenix.new dev_app --dev
```

This will produce a new project that has `:phoenix` configured as a relative dependency:

```
defp deps do
  [{:phoenix, path: "../..", override: true},
```

The command must be run from the `installer` directory. See the discussion in [PR 1224](https://github.com/phoenixframework/phoenix/pull/1224) for more information.

### Building phoenix.js

```bash
$ npm install
$ npm install -g brunch
$ brunch watch
```

### Building docs from source

```bash
$ MIX_ENV=docs mix docs
```

## Important links

* [#elixir-lang][1] on [Freenode][2] IRC
* [elixir-lang slack channel][3]
* [Issue tracker][4]
* [phoenix-talk Mailing list (questions)][5]
* [phoenix-core Mailing list (development)][6]
* Privately disclose security vulnerabilities to phoenix-security@googlegroups.com

  [1]: https://webchat.freenode.net/?channels=#elixir-lang
  [2]: http://www.freenode.net/
  [3]: https://elixir-slackin.herokuapp.com/
  [4]: https://github.com/phoenixframework/phoenix/issues
  [5]: http://groups.google.com/group/phoenix-talk
  [6]: http://groups.google.com/group/phoenix-core

## Copyright and License

Copyright (c) 2014, Chris McCord.

Phoenix source code is licensed under the [MIT License](LICENSE.md).
JaSerializer
============

[![Build Status](https://travis-ci.org/vt-elixir/ja_serializer.svg?branch=master)](https://travis-ci.org/vt-elixir/ja_serializer)
[![Hex Version](https://img.shields.io/hexpm/v/ja_serializer.svg)](https://hex.pm/packages/ja_serializer)
[![Deps Status](https://beta.hexfaktor.org/badge/all/github/vt-elixir/ja_serializer.svg)](https://beta.hexfaktor.org/github/vt-elixir/ja_serializer)
[![Inline docs](http://inch-ci.org/github/vt-elixir/ja_serializer.svg)](http://inch-ci.org/github/vt-elixir/ja_serializer)

jsonapi.org formatting of Elixir data structures suitable for serialization by
libraries such as Poison.

## Questions/Help

Please open an issue or message/mention @alanpeabody in the [Elixir Slack](https://elixir-slackin.herokuapp.com/).

## Usage

See [documentation](http://hexdocs.pm/ja_serializer/) on hexdoc for full
serialization and usage details.

## Installation
Add JaSerializer to your application

mix.deps

```elixir
defp deps do
  [
    # ...
      {:ja_serializer, "~> x.x.x"}
    # ...
  ]
end
```

## Serializer Behaviour and DSL

```elixir
defmodule MyApp.ArticleSerializer do
  use JaSerializer

  location "/articles/:id"
  attributes [:title, :tags, :body, :excerpt]

  has_one :author,
    serializer: PersonSerializer,
    include: true,
    field: :authored_by

  has_many :comments,
    links: [
      related: "/articles/:id/comments",
      self: "/articles/:id/relationships/comments"
    ]

  def comments(article, _conn) do
    Comment.for_article(article)
  end

  def excerpt(article, _conn) do
    [first | _ ] = String.split(article.body, ".")
    first
  end
end
```

### Attributes

Attributes are defined as a list in the serializer module.
The serializer will use the given atom as the key by default.
You can also specify a custom method of attribute retrieval by defining a
<attribute_name>/2 method. The method will be passed the struct
and the connection.

### Relationships

Valid relationships are: `has_one`, `has_many`.
Use `has_one` for `belongs_to` type of relationships.
For each relationship, you can define the name and a variety of options.
Just like attributes, the serializer will use the given atom
to look up the relationship, unless you specify a custom retrieval method
OR provide a `field` option

#### Relationship options

* serializer - The serializer to use when serializing this resource
* include - boolean - true to always side-load this relationship
* field - custom field to use for relationship retrieval
* links - custom links to use in the `relationships` hash

### Direct Usage of Serializer

```elixir
MyApp.ArticleSerializer
|> JaSerializer.format(struct, conn)
|> Poison.encode!
```

### Formatting options

The `format/4` method is able to take in options that can customize the
serialized payload.

#### Include

By specifying the `include` option, the serializer will only side-load
the relationships specified. This option should be a comma separated
list of relationships. Each relationship should be a dot separated path.

Example: `include: "author,comments.author"`

The format of this string should exactly match the one specified by the
[JSON-API spec](http://jsonapi.org/format/#fetching-includes)

Note: If specifying the `include` option, all "default" includes will
be ignored, and only the specified relationships included, per spec.

#### Fields

The `fields` option satisfies the [sparse fieldset](http://jsonapi.org/format/#fetching-sparse-fieldsets) portion of the spec. This options should
be a map of resource types whose value is a comma separated list of fields
to include.

Example: `fields: %{"articles" => "title,body", "comments" => "body"}`

If you're using Plug, you should be able to call `fetch_query_params(conn)`
and pass the result of `conn.query_params["fields"]` as this option.

## Phoenix Usage

Simply `use JaSerializer.PhoenixView` in your view (or in the Web module) and
define your serializer as above.

The `render("index.json-api", data)` and `render("show.json-api", data)` are defined
for you. You can just call render as normal from your controller.

By specifying `include`s when calling the render function, you can override
the `include: false` in the ArticleView.

```elixir
defmodule PhoenixExample.ArticlesController do
  use PhoenixExample.Web, :controller

  def index(conn, _params) do
    render conn, "index.json-api", data: Repo.all(Article)
  end

  def show(conn, %{"id" => id}) do
    article = Repo.get(Article, id) |> Repo.preload([:comments])
    render conn, "show.json-api", data: article,
      opts: [include: "comments"]
  end

  def create(conn, %{"data" => data}) do
    attrs = JaSerializer.Params.to_attributes(data)
    changeset = Article.changeset(%Article{}, attrs)
    case Repo.insert(changeset) do
      {:ok, article} ->
        conn
        |> put_status(201)
        |> render("show.json-api", data: article)
      {:error, changeset} ->
        conn
        |> put_status(422)
        |> render(:errors, data: changeset)
    end
  end
end

defmodule PhoenixExample.ArticlesView do
  use PhoenixExample.Web, :view
  use JaSerializer.PhoenixView # Or use in web/web.ex

  attributes [:title]

  has_many :comments,
    serializer: PhoenixExample.CommentsView,
    include: false,
    identifiers: :when_included
  #has_many, etc.
end
```

## Configuration

To use the Phoenix `accepts` plug you must configure Plug to handle the
"application/vnd.api+json" mime type and Phoenix to serialize json-api with
Poison.

Depending on your version of Plug add the following to `config.exs`:

Plug ~> "1.2.0"
```elixir
config :phoenix, :format_encoders,
  "json-api": Poison

config :mime, :types, %{
  "application/vnd.api+json" => ["json-api"]
}
```

And then re-compile mime: (per: https://hexdocs.pm/mime/MIME.html)

```shell
mix deps.clean mime --build
mix deps.get
```

Plug < "1.2.0"
```elixir
config :phoenix, :format_encoders,
  "json-api": Poison

config :plug, :mimes, %{
  "application/vnd.api+json" => ["json-api"]
}
```

And then re-compile plug: (per: https://hexdocs.pm/plug/1.1.3/Plug.MIME.html)

```shell
mix deps.clean plug --build
mix deps.get
```

And then add json api to your plug pipeline.

```elixir
pipeline :api do
  plug :accepts, ["json-api"]
end
```

For strict content-type/accept enforcement and to auto add the proper
content-type to responses add the JaSerializer.ContentTypeNegotiation plug.

To normalize attributes to underscores include the JaSerializer.Deserializer
plug.

```elixir
pipeline :api do
  plug :accepts, ["json-api"]
  plug JaSerializer.ContentTypeNegotiation
  plug JaSerializer.Deserializer
end
```

If you're rendering JSON API errors, like `404.json-api`, then you _must_ add `json-api`
to the `accepts` of your `render_errors` within your existing configuration in `config.exs`, like so:

```elixir
config :phoenix, PhoenixExample.Endpoint,
  render_errors: [view: PhoenixExample.ErrorView, accepts: ~w(html json json-api)]
```

## Testing controllers

Set the right headers in `setup` and when passing parameters to put and post requests,
you should pass them as a binary. That is because for map and list parameters,
the content-type will be automatically changed to multipart.

```elixir
defmodule Sample.SomeControllerTest do
  use Sample.ConnCase

  setup %{conn: conn} do
    conn =
      conn
      |> put_req_header("accept", "application/vnd.api+json")
      |> put_req_header("content-type", "application/vnd.api+json")

    {:ok, conn: conn}
  end

  test "create action", %{conn: conn} do
    params = Poison.encode!(%{data: %{attributes: @valid_attrs}})
    conn = post conn, "/some_resource", params

    ...
  end

  ...
end
```

## JSON API Generator

Use our built in generator to get up and running quickly. It uses the same format as the phoenix json generator.

```elixir
mix ja_serializer.gen.phoenix_api Checkbox checkboxes description:string checked:boolean list_id:references:lists
```

Want to tweak our templates? Insert your own under 'priv/templates/ja_serializer.gen.phoenix_api/' and we'll use yours instead.

## Pagination

JaSerializer provides page based pagination integration with
[Scrivener](https://github.com/drewolson/scrivener) or custom pagination
by passing your owns links in.

### Custom

JaSerializer allows custom pagination via the `page` option. The `page` option
expects to receive a `Map` with URL values for `first`, `next`, `prev`,
and `last`.

For example:

```elixir
page = [
  first: "http://example.com/api/v1/posts?page[cursor]=1&page[per]=20",
  prev: nil
  next: "http://example.com/api/v1/posts?page[cursor]=20&page[per]=20",
  last: "http://example.com/api/v1/posts?page[cursor]=60&page[per]=20"
]

# Direct call
JaSerializer.format(MySerializer, collection, conn, page: page)

# In Phoenix Controller
render conn, data: collection, opts: [page: page]
```

### Scrivener Integration

If you are using Scrivener for pagination, all you need to do is pass the
results of `paginate/2` to your serializer.

```elixir
page = MyRepo.paginate(MyModel, params.page)

# Direct call
JaSerializer.format(MySerializer, page, conn, [])

# In Phoenix controller
render conn, data: page
```

When integrating with Scrivener, the URLs generated will be based on the
`Plug.Conn`'s path. This can be overridden by passing in the `page[:base_url]`
option.

```elixir
render conn, data: page, opts: [page: [base_url: "http://example.com/foos"]]
```

You can also configure `ja_serializer` to use a global default URL
base for all links.

```elixir
config :ja_serializer,
  scrivener_base_url: "http://example.com:4000/v1/"
```

*Note*: The resulting URLs will use the JSON-API recommended `page` query
param.

Example URL:
`http://example.com:4000/v1/posts?page[page]=2&page[page-size]=50`

### Meta Data

JaSerializer allows adding top level meta information via the `meta` option. The `meta` option
expects to receive a `Map` containing the data which will be rendered under the top level meta key.

```elixir
meta_data = %{
  "key" => "value"
}

# Direct call
JaSerializer.format(MySerializer, data, conn, meta: meta_data)

# In Phoenix controller
render conn, data: data, opts: [meta: meta_data]
```

## Customization

### Key Format (for Attribute, Relationship and Query Param)

By default keys are `dash-erized` as per the jsonapi.org recommendation, but
keys can be customized via config.

In your `config.exs` file:

```elixir
config :ja_serializer,
  key_format: :underscored
```

You may also pass custom function for serialization and a second optional one for deserialization. Both accept a single binary argument:

```elixir
defmodule MyStringModule do
  def camelize(key), do: key #...
  def underscore(key), do: key #...
end

config :ja_serializer,
  key_format: {:custom, MyStringModule, :camelize, :underscore}
```

If you've already compiled your code, be sure to run `mix deps.clean ja_serializer && mix deps.get`

### Custom Attribute Value Formatters

When serializing attribute values more complex than string, numbers, atoms or
list of those things it is recommended to implement a custom formatter.

To implement a custom formatter:

```elixir
defimpl JaSerializer.Formatter, for: [MyStruct] do
  def format(struct), do: struct
end
```

## Complimentary Libraries

* [JaResource](https://github.com/vt-elixir/ja_resource) - WIP behaviour for creating JSON-API controllers in Phoenix.
* [voorhees](https://github.com/danmcclain/voorhees) - Testing tool for JSON API responses
* [inquisitor](https://github.com/DockYard/inquisitor) - Composable query builder for Ecto
* [scrivener](https://github.com/drewolson/scrivener) - Ecto pagination

## License

JaSerializer source code is released under Apache 2 License. Check LICENSE
file for more information.
FS Listener
===========

Backends
--------

* Mac [fsevent](https://github.com/thibaudgg/rb-fsevent)
* Linux [inotify](https://github.com/rvoicilas/inotify-tools/wiki)
* Windows [inotify-win](https://github.com/thekid/inotify-win)

NOTE: On Linux you need to install inotify-tools.

### Subscribe to Notifications

```erlang
> fs:subscribe(). % the pid will receive events as messages
> flush(). 
Shell got {<0.47.0>,
           {fs,file_event},
           {"/Users/5HT/synrc/fs/src/README.md",[closed,modified]}}
```

### List Events from Backend

```erlang
> fs:known_events(). % returns events known by your current backend
[mustscansubdirs,userdropped,kerneldropped,eventidswrapped,
 historydone,rootchanged,mount,unmount,created,removed,
 inodemetamod,renamed,modified,finderinfomod,changeowner,
 xattrmod,isfile,isdir,issymlink,ownevent]
```

### Sample Subscriber

```erlang
> fs:start_logger(). % starts a sample process that logs events with error_logger
=INFO REPORT==== 28-Aug-2013::19:36:26 ===
file_event: "/tank/proger/erlfsmon/src/4913" [closed,modified]
```

Credits
-------

* Vladimir Kirillov
* Maxim Sokhatsky

OM A HUM
Connection
==========

`Connection` behaviour for connection processes. The API is superset of the
GenServer API. There are 2 additional callbacks `connect/2` and `disconnect/2`:

```elixir
  @callback init(any) ::
    {:ok, any} | {:ok, any, timeout | :hibernate} |
    {:connect, any, any} |
    {:backoff, timeout, any} | {:backoff, timeout, any, timeout | :hibernate} |
    :ignore | {:stop, any}

  @callback connect(any, any) ::
    {:ok, any} | {:ok, any, timeout | :hibernate} |
    {:backoff, timeout, any} | {:backoff, timeout, any, timeout | :hibernate} |
    {:stop, any, any}

  @callback disconnect(any, any) ::
    {:connect, any, any} |
    {:backoff, timeout, any} | {:backoff, timeout, any, timeout | :hibernate} |
    {:noconnect, any} | {:noconnect, any, timeout | :hibernate}
    {:stop, any, any}

  @callback handle_call(any, {pid, any}, any) ::
    {:reply, any, any} | {:reply, any, any, timeout | :hibernate} |
    {:noreply, any} | {:noreply, any, timeout | :hibernate} |
    {:disconnect | :connect, any, any} |
    {:disconnect | :connect, any, any, any} |
    {:stop, any, any} | {:stop, any, any, any}

  @callback handle_cast(any, any) ::
    {:noreply, any} | {:noreply, any, timeout | :hibernate} |
    {:disconnect | :connect, any, any} |
    {:stop, any, any}

  @callback handle_info(any, any) ::
    {:noreply, any} | {:noreply, any, timeout | :hibernate} |
    {:disconnect | :connect, any, any} |
    {:stop, any, any}

  @callback code_change(any, any, any) :: {:ok, any}

  @callback terminate(any, any) :: any
```
There is an example of a simple TCP connection process in
`examples/tcp_connection/`.
# Poison

[![Travis](https://img.shields.io/travis/devinus/poison.svg?style=flat-square)](https://travis-ci.org/devinus/poison)
[![Hex.pm](https://img.shields.io/hexpm/v/poison.svg?style=flat-square)](https://hex.pm/packages/poison)
[![Hex.pm](https://img.shields.io/hexpm/dt/poison.svg?style=flat-square)](https://hex.pm/packages/poison)
[![Gratipay](https://img.shields.io/gratipay/devinus.svg?style=flat-square)](https://gratipay.com/devinus)

Poison is a new JSON library for Elixir focusing on wicked-fast **speed**
without sacrificing **simplicity**, **completeness**, or **correctness**.

Poison takes several approaches to be the fastest JSON library for Elixir.

Poison uses extensive [sub binary matching][1], a **hand-rolled parser** using
several techniques that are [known to benefit HiPE][2] for native compilation,
[IO list][3] encoding and **single-pass** decoding.

Preliminary benchmarking has sometimes put Poison's performance closer to
`jiffy`, and almost always faster than existing Elixir libraries.

## Installation

First, add Poison to your `mix.exs` dependencies:

```elixir
def deps do
  [{:poison, "~> 2.0"}]
end
```

Then, update your dependencies:

```sh-session
$ mix deps.get
```

## Usage

```elixir
defmodule Person do
  @derive [Poison.Encoder]
  defstruct [:name, :age]
end

Poison.encode!(%Person{name: "Devin Torres", age: 27})
#=> "{\"name\":\"Devin Torres\",\"age\":27}"

Poison.decode!(~s({"name": "Devin Torres", "age": 27}), as: %Person{})
#=> %Person{name: "Devin Torres", age: 27}

Poison.decode!(~s({"people": [{"name": "Devin Torres", "age": 27}]}),
  as: %{"people" => [%Person{}]})
#=> %{"people" => [%Person{age: 27, name: "Devin Torres"}]}
```

Every component of Poison -- the encoder, decoder, and parser -- are all usable
on their own without buying into other functionality. For example, if you were
interested purely in the speed of parsing JSON without a decoding step, you
could simply call `Poison.Parser.parse`.

If you use Poison 1.x, you have to set a module to `as` option in order to
decode into a struct. e.g. `as: Person` instead of `as: %Person{}`. The change was
introduced at 2.0.0.

## Parser

```iex
iex> Poison.Parser.parse!(~s({"name": "Devin Torres", "age": 27}))
%{"name" => "Devin Torres", "age" => 27}
iex> Poison.Parser.parse!(~s({"name": "Devin Torres", "age": 27}), keys: :atoms!)
%{name: "Devin Torres", age: 27}
```

Note that `keys: :atoms!` reuses existing atoms, i.e. if `:name` was not
allocated before the call, you will encounter an `argument error` message.

You can use the `keys: :atoms` variant to make sure all atoms are created as
needed.  However, unless you absolutely know what you're doing, do **not** do
it.  Atoms are not garbage-collected, see
[Erlang Efficiency Guide](http://www.erlang.org/doc/efficiency_guide/commoncaveats.html)
for more info:

> Atoms are not garbage-collected. Once an atom is created, it will never be
> removed. The emulator will terminate if the limit for the number of atoms
> (1048576 by default) is reached.

## Encoder

```iex
iex> IO.puts Poison.Encoder.encode([1, 2, 3], [])
"[1,2,3]"
```

Anything implementing the Encoder protocol is expected to return an
[IO list][4] to be embedded within any other Encoder's implementation and
passable to any IO subsystem without conversion.

```elixir
defimpl Poison.Encoder, for: Person do
  def encode(%{name: name, age: age}, options) do
    Poison.Encoder.BitString.encode("#{name} (#{age})", options)
  end
end
```

For maximum performance, make sure you `@derive [Poison.Encoder]` for any struct
you plan on encoding.

### Encoding only some attributes

When deriving structs for encoding, it is possible to select or exclude specific attributes. This is achieved by deriving `Poison.Encoder` with the `:only` or `:except` options set:

```elixir
defmodule PersonOnlyName do
  @derive {Poison.Encoder, only: [:name]}
  defstruct [:name, :age]
end

defmodule PersonWithoutName do
  @derive {Poison.Encoder, except: [:name]}
  defstruct [:name, :age]
end
```

In case both `:only` and `:except` keys are defined, the `:except` option is ignored.

## Benchmarking

```sh-session
$ mix deps.get
$ MIX_ENV=bench mix compile
$ MIX_ENV=bench mix bench
```

## License

Poison is released into the public domain (see `UNLICENSE`).
Poison is also optionally available under the ISC License (see `LICENSE`),
meant especially for jurisdictions that do not recognize public domain works.

[1]: http://www.erlang.org/euc/07/papers/1700Gustafsson.pdf
[2]: http://www.erlang.org/workshop/2003/paper/p36-sagonas.pdf
[3]: http://jlouisramblings.blogspot.com/2013/07/problematic-traits-in-erlang.html
[4]: http://prog21.dadgum.com/70.html
# Inflex[![Build Status](https://travis-ci.org/nurugger07/inflex.png?branch=master)](https://travis-ci.org/nurugger07/inflex)

An Elixir library for handling word inflections.

## Getting Started

You can add Inflex as a dependency in your `mix.exs` file. Since it only requires Elixir and Erlang there are no other dependencies.

```elixir
def deps do
  [ { :inflex, "~> 1.8.0" } ]
end
```

If you are not using [hex](http://hex.pm) you can add the dependency using the github repo.

``` elixir

  def deps do
    [ { :inflex, github: "nurugger07/inflex" } ]
  end

```

Then run `mix deps.get` in the shell to fetch and compile the dependencies.

To incorporate Inflex in your modules, use `import`.

``` elixir

  defmodule YourModule do
    import Inflex

    def make_singular(word), do: singularize(word)

  end

```

## Examples

### Singularize & Pluralize

Here are some basic examples from `iex`:

``` elixir

iex(1)> Inflex.singularize("dogs")
"dog"

iex(2)> Inflex.pluralize("dog")
"dogs"

iex(3)> Inflex.singularize("people")
"person"

iex(4)> Inflex.pluralize("person")
"people"

```

Some other special cases are handled for nouns ending in -o and  -y

```elixir


iex(1)> Inflex.pluralize("piano")
"pianos"

iex(2)> Inflex.pluralize("hero")
"heroes"

iex(3)> Inflex.pluralize("butterfly")
"butterflies"

iex(4)> Inflex.pluralize("monkey")
"monkeys"

```

### Inflect

``` elixir
iex(1)> Inflex.inflect("child", 1)
"child"

iex(2)> Inflex.inflect("child", 2)
"children"
```

### Camelize & Pascalize

Inflex also camelizes or pascalizes strings and atoms.

```elixir

iex(1)> Inflex.camelize(:upper_camel_case)
"UpperCamelCase"

iex(2)> Inflex.camelize("pascal-case", :lower)
"pascalCase"

```

### Parameterize

Strings can be parameterized easily.

```elixir

iex(1)> Inflex.parameterize("String for parameter")
"string-for-parameter"

iex(2)> Inflex.parameterize("String with underscore", "_")
"string_with_underscore"

```

### Underscore

Makes an underscored, lowercase form from a string or atom.

```elixir

iex(1)> Inflex.underscore("UpperCamelCase")
"upper_camel_case"

iex(2)> Inflex.underscore("pascalCase")
"pascal_case"

iex(3)> Inflex.underscore(UpperCamelCase)
"upper_camel_case"

iex(4)> Inflex.underscore(:pascalCase)
"pascal_case"

```

## Contributing

All pull requests will be reviewed for inclusion but must include tests.
