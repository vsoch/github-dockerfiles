Docker compose file to run a project with Rails, Webpacker and PostgreSQL

Your database.yml should look like this :

```yaml
default: &default
  adapter: postgresql
  database: rails_app
  host: <%= ENV["PG_HOST"] %>
  user: <%= ENV["PG_USER"] %>
  password: <%= ENV["PG_PWD"] %>
```

Your config/webpacker.yml like this : 

```yaml
development:
  <<: *default
  compile: true
  dev_server:
    https: false
    host: webpacker
    port: 3035
    public: 0.0.0.0:3035
    hmr: true
    # Inline should be set to true if using HMR
    inline: true
    quiet: false
    headers:
      'Access-Control-Allow-Origin': '*'
 ```

Tip : Use Rails debug console with this config in `config/environments/development.rb`
`  config.web_console.whitelisted_ips = "0.0.0.0/0"`

Ensure `db/postgres_data` folder is present both in `.gitignore` and `.dockerignore` files since it embbeds PostgreSQL container's data (to persist them between containers recreations)

With webpacker enabled, you also may want to disable classic pipeline functionalities :
```rb
# config/application.rb
config.assets.enabled = false
config.generators do |g|
  g.assets false
end
```
