# Definition of Service Done:
- [ ] Confluence platforms has entry for the service? [Platforms](https://confluence.aws.telegraph.co.uk/display/PLAT/Platforms+Home)
- [ ] Swagger entry points
- [ ] Is there appropriate test coverage?
- [ ] Infrastructure created?
- [ ] Does it have a pipeline in jenkins? 
- [ ] Does it have a codacy project? Does it have the badges in the readme?
- [ ] Does it imply any kind of data migration? If so what are the steps for that?
- [ ] Is the Documentation been created, if needed?
- [ ] Does it has appropriate logs?
- [ ] Does it has appropriate alerts?

$name$
-------
[![Build Status](https://jenkins-prod.api-platforms.telegraph.co.uk/job/Pipeline/job/$name$/badge/icon)](https://jenkins-prod.api-platforms.telegraph.co.uk/job/Pipeline/job/$name$/)

$project_description$

# $name$ Definition

## Data Model

|Field|Mandatory|Description|
|:--------------:|:------------|:--------------:|
|Example|y|this is an example|

## API Endpoints

You can see the endpoints at:
- [Preprod Swagger](http://swagger-ui-preprod.api-platforms.telegraph.co.uk/?url=http://platforms-preprod.api-platforms.telegraph.co.uk/$name$/swagger.json)
- [Prod Swagger](http://swagger-ui-prod.api-platforms.telegraph.co.uk/?url=http://platforms-prod.api-platforms.telegraph.co.uk/$name$/swagger.json)
