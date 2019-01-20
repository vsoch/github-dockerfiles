# EPPSA KSM Game

The KSM game web application.

## Development
```
npm install
npm run watch
```

## Production
```
npm install
PORT=<PORT> npm start
```
# EPPSA KSM Dashboard

The dashboard provides general game statistics.

## Development
```
npm install
npm run watch
```

## Production
```
npm install
PORT=<PORT> npm start
```
# Mongo access service

## export_collection.sh
exports the collections `games` and `challenge-1` to `challenge-11` into ./export as json files.

```
HOST=<MongoDB_HOST> DB=<MongoDB_NAME(EPPSA_KSM)> ./export_collections.sh
```
# Game Server

Serves as data connector between client and backend.
# Multi Client Tester

Puppeteer script to simulate multiple clients.

## Usage
```
GAME_URL=https://game.<environment>.eppsa.de MAX_CLIENTS=<number_of_clients> npm start
```