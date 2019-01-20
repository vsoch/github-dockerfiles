# Touk-URL shortener

### Developing
Requirements: [stack](https://github.com/commercialhaskell/stack), libgmp, libpq5, running PostgreSQL server

``` bash
git clone https://github.com/TouK/touk-url
cd touk-url
stack install cabal-install yesod-bin --install-ghc
stack build

# Set up local database
docker run -p 5432:5423 -e POSTGRES_USER=touk-url -e POSTGRES_PASSWORD=touk-url --name database postgres:9.4

# Run devel server
stack exec -- yesod devel
firefox http://localhost:3000/
```

### Configuration
Application can be configured via environmental variables:
- APPROOT - URL used to create root path, i. e. http://production.pl
- APPPORT - port used by application, i. e. 80
- LOGFILE - if specified, logs will be saved in file with path provided on this variable, i. e. /var/log/touk-url.log

Database credentials can be set using:
- PGHOST
- PGPORT
- PGUSER
- PGPASS
- PGDATABASE
- PGPOOLSIZE

### Pages
These are pages which response with readable HTML content:
- /
- /stats

All shortened urls are created using /global/*Text* route

### API

#### Shortening URL
##### POST /
```
{
  "url": "urltoshorten"
}
```

Possible responses:
```
{
  "classyEncoded": "url1",
  "funEncoded: "url2"
}
```
```
{
  "error": "error message"
}
```
```
{
  "jsonError": "error with parsing json"
}
```

#### Accessing entries from database
##### GET /stats/api/urls
Returns data about each short url created \
Example response:
```
[
  {
    "original":      "http://www.touk.pl",
    "classyEncoded": "ynicpc",
    "funEncoded":    "digestive-bike-unbans-haskell",
    "dateCreated":   "2015-09-11 06:33:37.027546 UTC"
  }
]
```

##### GET /stats/api/visits
Returns data about each short url expansion \
Example response:
```
[
  {
    "originalUrl": "http://www.touk.pl",
    "ip":          "10.0.42.1:41372",
    "date":        "2015-09-11 06:33:38.095106 UTC",
    "encoded":     "ynicpc"
  }
]
```

