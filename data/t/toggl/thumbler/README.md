# Thumbler

## Environment setup

### Install MongoDB

Also, if you'd like a GUI to inspect data with, you can try [RoboMongo](https://robomongo.org/download).

### Install NodeJS from http://nodejs.org/. Npm should come with it.

### Cd into project directory and issue

`$ yarn install`

### 6. Configure database connection

Add db_config.json to the project folder.

Sample config:

```
{
  "url": "mongodb://localhost/thumbler"
}
```

OR specify the DB connection url via DB_URL environment variable.

`DB_URL=mongodb://localhost/thumbler yarn gulp`

### 7. Run the dev environment + server

`$ mongod --dbpath path_to_db`
`$ yarn gulp --debug=thumbler:*`

This watches app directory and restarts the server every time it detects a change in code.
Also supports chrome livereload plugin so you don't have to refresh the browser manually.
Get the plugin here: https://chrome.google.com/webstore/detail/livereload/jnihajbhpnppcggbcgedagnkighmdlei?hl=en

### 8. Test Driven Development

To simply run the tests

`$ yarn gulp test`

To watch for file changes and run the tests every time something changes

`$ yarn gulp tdd --debug=thumbler*`

### 9. Deploy

`$ NODE_ENV=staging yarn deploy`

To deploy you need a deploy config. Create a folder called `local_config/` and add an deploy_config.json in it.

Sample config:

```json
{
  "targets": {
    "staging": {
      "host": "<ip>",
      "user": "toggl",
      "port": "22",
      "root": "/home/toggl/toggl_thumbler/"
    },
    "production": {
      "host": "<ip>",
      "port": "22",
      "user": "toggl",
      "root": "/home/toggl/toggl_thumbler/"
    }
  }
}
```

### 10. Enjoy

## Useful info

App runs on `http://localhost:7501`

View list of thumbs at `http://localhost:7501/thumbs/list`

Get a summary of yesterday's thumbs for a service at `http://localhost:7501/thumbs/summary?serviceId=your-service-id`

If you have a db dump from someone, do this to import it:

`mongorestore -d thumbler path/to/thumbs.bson`

## Hooks

You can specify some hooks to customize the app. Just add an `hooks.coffee` under `./local_config` and let it export an object
containing any of the following keys mapping to values or functions:

### corsWhitelist

Return an array of domains to whitelist for CORS

Example:

```javascript
module.exports = {
  corsWhitelist: () => [
    'https://support.toggl.com',
    'https://support.teamweek.com'
  ]
}
```

### displaySubjectId(thumb)

Return a subject id for display in the thumbs list. This let's you convert the subject id into a slightly more human-readable form.

Example:

```javascript
module.exports = {
  displaySubjectId: thumb => thumb.subjectId.split('|').join('-')
}
```

### displaySubjectLink(thumb)

Return a link to the subject. This let's you generate a link to the subject, given the subject id.

Example:

```javascript
module.exports = {
  displaySubjectLink: (thumb) ->
    subjectId = thumb.subjectId.split('|')
    switch subjectId[0]
      when 'kb-toggl'
        return `https://support.toggl.com/${subjectId[1]}`
      when 'kb-tw'
        return `https://support.teamweek.com/${subjectId[1]}`
      else
        return 'javascript:void(0)'
}
```

## Some util commands

Displays a fortune. Often comes in handy.

`$ fortune`

If you're missing this crucial tool you can install it by running `sudo apt-get install fortune` on linux or `brew install fortune` on osx (using brew).
