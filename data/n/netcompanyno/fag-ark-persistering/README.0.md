# PrisonerRepo

## Start

### Start opp en neo4j server på docker

Velg et neo4j docker image, og kjør det. Jeg har ikke funnet noe offisielt Neo4j image, men dette imaget virker bra:

docker run -itd -e NEO4J_AUTH=none --name neo4j -p 7474:7474 ahmetkizilay/docker-neo4j

### Start opp rest-serveren

For å kjøre docker containeren (husk å velge port):

docker run -itd -p <din port>:8080 marstran/persistering-neo4j

Det kan ta litt tid før rest-endepunktet er oppe. Ser ut som docker bruker tid på å starte en "SecureRandom instance" (mellom 60 og 200 sekunder).

Hvis du bruker boot2docker, så må du forwarde porten hvis du vil aksessere endepunktet fra maskinen din (f.eks. hvis du vil bruke Postman) Dette gjøres med:

VBoxManage controlvm boot2docker-vm natpf1 "PrisonerRepoPort,tcp,127.0.0.1,8080,,8080"

Testet ut på mac.

# REST API

## POST /prisoner/insert

Setter inn en fange. Fangen må ha et navn.
Dersom ID finnes fra før, så vil fangen bli oppdatert.
Dersom ID ikke er gitt, så vil den bli generert. Innsatt fange vil bli
returnert.

### Body-eksempel
```json
{
	"id": "1",
	"name": "Billy the Kid",
	"health": 100,
	"isDangerous": true,
	"hunger": 50,
	"thirst": 20,
	"aggression": 100,
	"sosializable": 0
}
```
## GET /prisoner/findById?nodeId=\<nodeId\>

Henter en fange på ID.

## GET /prisoner/findByName?name=\<name\>

Henter en fange på navn.

## GET /prisoner/findAll

Henter alle fanger.

## POST /prisoner/addFriendship

Legger til et vennskap. Dersom fangen ikke finnes, vil
den bli lagt til (?).

### Body-eksempel
```json
{
	"friend1": {
					"id": "1",
					"name": "Billy the Kid",
					"health": 100,
					"isDangerous": true,
					"hunger": 50,
					"thirst": 20,
					"aggression": 100,
					"sosializable": 0
				},
	"friend2": {
					"id": "2",
					"name": "Lucky Lule",
					"health": 100,
					"isDangerous": false,
					"hunger": 0,
					"thirst": 0,
					"aggression": 20,
					"sosializable": 100
				}
}
```

## GET /prisoner/getFriendsById?nodeId=\<nodeId\>

Returnerer en liste av fanger som er venn med fangen med den gitte ID'en.

## POST /prisoner/addEnemies

Legger til et fiendeskap. Se addFriendship (samme requestbody, men med enemy1 og 2 i stedetfor friend1 og 2).

## GET /prisoner/getEnemiesById?nodeId=\<nodeId\>

Returnerer en liste av fanger som er fiende med fangen med den gitte ID'en.

# Spring data Neo4j

http://docs.spring.io/spring-data/data-neo4j/docs/3.2.2.RELEASE/reference/html/#tutorial_running