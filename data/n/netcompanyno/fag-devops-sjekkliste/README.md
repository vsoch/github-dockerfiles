# Sjekkliste

[![](https://badge.imagelayers.io/monsendag/sjekkliste:latest.svg)](https://imagelayers.io/?images=monsendag/sjekkliste:latest 'Get your own badge on imagelayers.io')

Applikasjonen er veldig enkel. Det er en Todoliste. Den har et RESTful API, er laget med [Spring Boot](http://projects.spring.io/spring-boot/) og benytter SQL Server i Azure.

### For å kjøre i docker

1. Installer Docker og Docker Compose

2. `docker-compose up -d`

3. Gå til `http://localhost:8080`


### Det som trengs
- [Java 7](http://www.oracle.com/technetwork/java/javase/downloads/index.html) eller nyere.
- [Maven](http://maven.apache.org/), følg installasjonsbeskrivelsen på nedlastingssiden.

### Kjør applikasjonen:
- fra kommandolinja med kommandoen: `mvn spring-boot:run`
- fra IDE ved å kjøre TodoApplication.java som inneholder main metoden.

### Hva applikasjonen kan gjøre
Da det ikke er noe GUI så benytt gjerne en REST-klient. Det gjør lagring av data enklere.

#### List alle Todos
`GET /api/todo`

#### Legg til en Todo
`POST /api/todo`

Forventet input:

```json
    {
      "title": "eksempeltittel",
      "content": "beskrivelse for todo"
    }
```
    
#### Endre en Todo
`PUT /api/todo`

Forventet input:

```json
    {
      "id": 1,
      "title": "ny tittel",
      "content": "nytt innhold",
      "completed": true
    }
```

#### Slette en Todo
`DELETE /api/todo/{id}`

#### Fremprovosere exception
Denne brukes for enkelt å få en stack trace og se hvordan det logges i Azure.

`GET /api/throwexception`


#### Ytelsestesting

##### Regn ut Pi med `n` desimaler

 `GET /api/pi/{n}`

##### Sorter et array med lengde `n`

`GET /api/sort/{n}`

#### Health service

##### Se hvilket versjonsnummer som ligger ute, og når det ble bygget

`GET /api/health`
