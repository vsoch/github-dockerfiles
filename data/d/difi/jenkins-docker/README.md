# Jenkins i Docker-konteiner

Dette er en prekonfigurert Jenkins-instans som benytter pipeline-as-code-konseptet.

## Tilgjengelige verktøy

Følgende verktøy er tilgjengelig for byggejobber direkte fra `PATH`:
* Java Development Kit 8 (`java`)
* Maven 3.5.2 (`mvn`)
* Docker klient 17.06.1-ce (`docker`)
* Docker Machine 0.12.2 (`docker-machine`)
* AWS CLI (`aws`)

## Hvordan kjøre applikasjonen

Følgende krav stilles til vertsmaskinen:
* Docker Engine (17.09 eller nyere) er installert.
* Det finnes en bruker med uid 1797.
* Docker Engine kjører i sverm-modus
* En node i svermen er merket _jenkins-master=true_
* Svermen har en [konfigurasjon](https://docs.docker.com/engine/reference/commandline/config/) som heter _pipeline-jobs_,
som definerer hvilke jobber som skal kjøres (beskrevet under).
* Svermen har definert de hemmelighetene som kreves i `docker/jenkins/stack.yaml`. For lokal testing kan skriptet
  `utils/create-dummy-secrets` benyttes.

Applikasjonen kan kjøres som et sett tjenester (en _stack_) på en Docker-sverm:
```
$ docker/run USERNAME PASSWORD STACK_NAME VERSION
```

På en utvikler-maskin kan applikasjonen kjøres opp slik:
```
$ docker/build verify
$ docker/run-local
```

## Jobb-definisjoner

Applikasjonen krever at Docker-svermen har en konfigurasjon som heter _pipeline-jobs_. Denne er på følgende format (yaml):
```
jobs:
  jenkins-docker:
    repository: git@github.com:difi/jenkins-docker
    sshKey: difi-ssh-key
  another-job-name:
    repository: git@mygithost.example.com:another-job
    sshKey: another-ssh-key
  [...]    
```

## Hvordan vedlikeholde bildet

### Oppgradere Jenkins-versjon

Dockerfile inneholder følgende linjer:

```
ARG JENKINS_VERSION=2.23
ARG JENKINS_SHA=6c47f8f6019b9a2be17662033444ce7eec03f4fa
```

På http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/[versjon]/jenkins-war-[versjon].war finner du siste versjon, og SHA1-sum for denne finner du i http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-war/[versjon]/jenkins-war-[versjon].war.sha1. Erstatt argumentene over med disse for å bygge bilder med denne versjonen.

### Oppgradere tillegg

TODO

### Bygge bildet

```
$ docker/build verify
```

### Publisere bildet

```
$ docker/build deliver VERSION REGISTRY_USERNAME REGISTRY_PASSWORD
```
