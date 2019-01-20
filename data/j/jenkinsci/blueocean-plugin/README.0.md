# BlueOCean REST API implementation

Implementation of BlueOcean REST API from `blueocean-rest` module.

See README.md in `blueocean-rest` module.    
    


    

    
# BlueOcean JWT Plugin

This plugin provides JWT authenticated related APIs. JWT token is signed using RSA256 algorithm. This is asymmetric 
algorithm, this means the token is signed using the private key and Client must use corresponding public key to verify 
the claims. 

# APIs

## JWT Token API

JWT token is generated for the user in session. In Jenkins there is always a user in context, that is if there is no 
logged in user then the generated token will carry the claim for anonymous user.

Default expiry time of token is 30 minutes.

JWT token is return as X-BLUEOCEAN-JWT HTTP header. 


    GET /jwt-auth/token
    
    HTTP/1.1 200 OK
    X-BLUEOCEAN-JWT: eyJraWQiOiI2M2ZhMTY0ZWRhMDk0NjNjOGZlZTI2Njg4ZjgxOTZmZCIsImFsZyI6IlJTMjU2IiwidHlwIjoiSldUIn0.eyJqdGkiOiJiMGVmMjJiNDliNWM0N2JjODU4YTg2MDdkM2Y0NGQzMyIsImlzcyI6ImJsdWVvY2Vhbi1qd3Q6Iiwic3ViIjoiYWxpY2UiLCJuYW1lIjoiQWxpY2UgQ29vcGVyIiwiaWF0IjoxNDcwMzMxNjA1LCJleHAiOjE0NzAzMzM0MDUsIm5iZiI6MTQ3MDMzMTU3NSwiY29udGV4dCI6eyJ1c2VyIjp7ImlkIjoiYWxpY2UiLCJmdWxsTmFtZSI6IkFsaWNlIENvb3BlciIsImVtYWlsIjoiYWxpY2VAamVua2lucy1jaS5vcmcifX19.H1iZAR2ajMeWRhh1VDdbqOtD7Wo0e0FZx8JDDNzphLu2DaLlxVRzBbhZ5TllvPx787kbNeK2tymFu_2Y_59qkq7YxZkrJctZTeiHVlTlHIxf2woBBggkIgoSvzNSsCcX73vjH5A5e54T5e8rUjF56XP05d5-WDvvheLo_Sqn4j19_lXkogCC2-JhDfc7sb8Xnw5PwYNZs29JYSSLOuUWm8UnD3AnBeFBhPfY2bR8-BjPXxdRWAyrZ-bz1CITfOm1xHZ-8NCGsfsUUGlcB_ijPVBt5T_29JWWFnougM1qZ_CEO56xu1572LMUmBYi8ynl75frzoSL_PvZYMXF47zcdg

JSON presentation of this token:

Header:

    {"kid":"63fa164eda09463c8fee26688f8196fd","alg":"RS256","typ":"JWT"}
    
Claims:

    {
       "name" : "Alice Cooper",
       "iss" : "blueocean-jwt:",
       "sub" : "alice",
       "exp" : 1470333405,
       "nbf" : 1470331575,
       "context" : {
          "user" : {
             "id" : "alice",
             "fullName" : "Alice Cooper",
             "email" : "alice@jenkins-ci.org"
          }
       },
       "jti" : "b0ef22b49b5c47bc858a8607d3f44d33",
       "iat" : 1470331605
    }

### Change expiry time

JWT tokens expires after 30 minutes (Default). exp claim header gives the time at which token expires. It is unix time 
in seconds. Default 30 minutes can be changed by sending expiryTimeInMins query parameter. This parameter value must be 
less than maximum expiry time allowed (8 hours or 480 minutes).   

This parameter must be used carefully, it has security implications.

    GET /jwt-auth/token?expiryTimeInMins=15

## Change maximum allowed expiry time

Use query maxExpiryTimeInMins to change default 8 hours maximum allowed expiry time.

This parameter must be used carefully, it has security implications.

    GET /jwt-auth/token?maxExpiryTimeInMins=15

## Json web key (jwk) API 

Client can call this API to get public key using the key id received as part of JWT header field 'kid'. This public key 
must be used to verify the JWT token.

    GET /jwt-auth/jwks/bab71d7b184548a6b93480721d352ba1
     
    HTTP/1.1 200 OK
    Content-type: application/json
    {
       "alg" : "RS256",
       "e" : "AQAB",
       "kty" : "RSA",
       "n" : "AMmWNNrmWzJXik7K7gmDkPumxqPzxc/JnxWsZ3CrhJGSO8hIgfsN6M5UHWSwkAoBHyNIaaPXhubWpcWCRewiI0U2Aw4jO3vzxNndRB9YaDPrrWDjvKBaqMC08IePPxmxXCj3ZS0QoEpf6rczdm2f9Of6Fro0TufXf2EYjLndBH7ep6iDQ4/TG7FkD7o39/GXuHAin0sz7atrPun3tlkuxllu5XNV+yW6WusrNIz3txyvKKEyQX950eW/6mMD0hS6yT7TbAwfrxkTnq4SiagCTllV+ct4wfnONDrao3WYgZnNgohsX/nEnYMHYq592n2WZW/i2+PNaFZlL2+3QgWO4qc=",
       "use" : "sig",
       "key_ops" : [
          "verify"
       ],
       "kid" : "bab71d7b184548a6b93480721d352ba1"
    }

 
The Blue Ocean REST API is a "private API" designed for the Blue Ocean user interface. It may change without notice at any time.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Run Blue Ocean plugin](#run-blue-ocean-plugin)
- [Schema](#schema)
  - [Media Type](#media-type)
  - [Date Format](#date-format)
  - [Error Message](#error-message)
  - [Crumbs](#crumbs)
- [Security](#security)
  - [API access from browser with JWT enabled](#api-access-from-browser-with-jwt-enabled)
- [Navigability](#navigability)
  - [Links](#links)
- [Resource discovery](#resource-discovery)
  - [classes API](#classes-api)
    - [Get class details](#get-class-details)
    - [Get detailed map of all given classes](#get-detailed-map-of-all-given-classes)
- [User API](#user-api)
  - [Get a user](#get-a-user)
  - [Find users in an organization](#find-users-in-an-organization)
  - [Get authenticated user](#get-authenticated-user)
- [Organization API](#organization-api)
  - [Get organization details](#get-organization-details)
  - [Get all organizations](#get-all-organizations)
- [Pipeline API](#pipeline-api)
  - [Get a Pipeline](#get-a-pipeline)
  - [Get Pipelines for an organization](#get-pipelines-for-an-organization)
  - [Get Pipelines across organization](#get-pipelines-across-organization)
    - [Exclude flattening of certain job types](#exclude-flattening-of-certain-job-types)
    - [Get pipelines for specific organization](#get-pipelines-for-specific-organization)
  - [Parameterized Pipeline](#parameterized-pipeline)
  - [Get a Folder](#get-a-folder)
  - [Get Nested Pipeline Inside A Folder](#get-nested-pipeline-inside-a-folder)
  - [Get nested Folder and Pipeline](#get-nested-folder-and-pipeline)
  - [MultiBranch Pipeline API](#multibranch-pipeline-api)
    - [Get MultiBranch pipeline](#get-multibranch-pipeline)
    - [Get MultiBranch pipeline branches](#get-multibranch-pipeline-branches)
  - [Pipeline Permissions](#pipeline-permissions)
- [Queue API](#queue-api)
  - [Fetch queue for an pipeline](#fetch-queue-for-an-pipeline)
  - [GET queue for a MultiBranch pipeline](#get-queue-for-a-multibranch-pipeline)
  - [Remove a queued item](#remove-a-queued-item)
- [Run API](#run-api)
  - [Get all runs in a pipeline](#get-all-runs-in-a-pipeline)
  - [Get a run details](#get-a-run-details)
  - [Find latest run of a pipeline](#find-latest-run-of-a-pipeline)
  - [Find latest run on all pipelines](#find-latest-run-on-all-pipelines)
  - [Start a build](#start-a-build)
  - [Start a parameterized build](#start-a-parameterized-build)
  - [Stop a build](#stop-a-build)
    - [Stop a build as blocking call](#stop-a-build-as-blocking-call)
  - [Get MultiBranch job's branch run detail](#get-multibranch-jobs-branch-run-detail)
  - [Get all runs for all branches on a multibranch pipeline (ordered by date)](#get-all-runs-for-all-branches-on-a-multibranch-pipeline-ordered-by-date)
  - [Get latest activity of Multi-branch pipeline for all branches](#get-latest-activity-of-multi-branch-pipeline-for-all-branches)
  - [Get change set for a run](#get-change-set-for-a-run)
  - [Pipeline Node API](#pipeline-node-api)
    - [Get Pipeline run nodes](#get-pipeline-run-nodes)
    - [Get a Pipeline run node's detail](#get-a-pipeline-run-nodes-detail)
  - [Pipeline Steps API](#pipeline-steps-api)
    - [Get steps for a Pipeline node](#get-steps-for-a-pipeline-node)
    - [Get a Pipeline step details](#get-a-pipeline-step-details)
    - [Get Pipeline Steps](#get-pipeline-steps)
    - [Get Pipeline Steps with Input](#get-pipeline-steps-with-input)
    - [Submit step input to proceed](#submit-step-input-to-proceed)
    - [Submit step input to abort](#submit-step-input-to-abort)
  - [Replay a pipeline build](#replay-a-pipeline-build)
- [Favorite API](#favorite-api)
  - [Favorite a pipeline](#favorite-a-pipeline)
  - [Favorite a multi branch pipeline](#favorite-a-multi-branch-pipeline)
  - [Un-favorite a multi branch pipeline](#un-favorite-a-multi-branch-pipeline)
  - [Favorite a multi branch pipeline branch](#favorite-a-multi-branch-pipeline-branch)
  - [Un-favorite a multi branch pipeline branch](#un-favorite-a-multi-branch-pipeline-branch)
  - [Fetch user favorites](#fetch-user-favorites)
- [Log API](#log-api)
  - [Fetching logs](#fetching-logs)
  - [Download a log for a Pipeline run](#download-a-log-for-a-pipeline-run)
  - [Get log for a Pipeline run](#get-log-for-a-pipeline-run)
  - [Get log for a Pipeline step](#get-log-for-a-pipeline-step)
- [SCM API](#scm-api)
  - [Validate Github personal access token](#validate-github-personal-access-token)
  - [Check SCM for available credentialId to use:](#check-scm-for-available-credentialid-to-use)
  - [List organizations of SCM (e.g. github)](#list-organizations-of-scm-eg-github)
  - [Repositories API](#repositories-api)
    - [Get SCM repositories in an organization](#get-scm-repositories-in-an-organization)
      - [Pagination for GitHub repositories](#pagination-for-github-repositories)
    - [Get SCM repository in an organization](#get-scm-repository-in-an-organization)
    - [Get Github file content of a pipeline (Multibranch or OrganizationFolder)](#get-github-file-content-of-a-pipeline-multibranch-or-organizationfolder)
      - [Get github file content from MBP branch](#get-github-file-content-from-mbp-branch)
      - [Get github file content from MBP folder](#get-github-file-content-from-mbp-folder)
      - [Get github file content from org folder](#get-github-file-content-from-org-folder)
    - [Save file content to SCM repo](#save-file-content-to-scm-repo)
      - [Save file to an OrganizationFolder](#save-file-to-an-organizationfolder)
      - [Save file to a MultiBranchProject](#save-file-to-a-multibranchproject)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

This document defines REST API interface that front end UI or any HTTP client can use.

# Run Blue Ocean plugin

    cd blueocean-plugin
    mvn hpi:run

This will launch a development Jenkins instance with the Blue Ocean plugin and this plugin ready to go.

BlueOcean UI is available at:

    http://localhost:8080/jenkins/blue


BlueOcean rest API base URL is:

    http://localhost:8080/jenkins/blue/rest

# Schema

## Media Type

* All responses are _application/json_ content type
* All POST/PUT/PATCH methods must be _application/json_ content type

## Date Format

All date formats are in ISO 8601 format

    YYYY-MM-DDTHH:MM:SSZ

## Error Message

```
{
  "message" : "Failed to create Git pipeline: demo",
  "code" : 400,
  "errors" : [ {
    "message" : "demo already exists",
    "code" : "ALREADY_EXISTS",
    "field" : "name"
  } ]
}
```

_message_ - High level error message. E.g. 'Failed to create Git Pipeline'

_code_ - error code, should be HTTP error code

_errors_ - array of errors for request fields.

_errors.message_ - Field validation error message.

_errors.code_ - Field validation codes. Known codes, ALREADY_EXISTS, MISSING, NOT_FOUND, INVALID.

_errors.field_ - Name of the field in request. Top level field name are represented as it is. Request subgraph are represented as follows:

* If value is map its represented with . notation. For example for `{"scmConfig":{"uri":"abcd"}}`, the field name will be scmConfig.uri
* If value is array its represented with [index] notation. For example for `{"repos":[{"name":"abcd"}}]`, the field name will be repos[0].name

_Field Error codes_

| Field Error Code  | Description   |
| ------------------|:-------------:|
| ALREADY_EXISTS    | Field value already exists |
| MISSING| Required field|
| NOT_FOUND | Field value not found |
| INVALID | Invalid field value |

_Http Error codes_

| HTTP Error Code  | Description   |
| ------------------|:-------------:|
| 400    | Bad Request |
| 401| Unauthorized, invalid credentials|
| 403| Forbidden, not authorized|
| 404 | Not found |
| 500 | Unexpected error



## Crumbs

Jenkins usually requires a "crumb" with posted requests to prevent request forgery and other shenanigans.
To avoid needing a crumb to POST data, the header `Content-Type: application/json` *must* be used.

# Security

NOTE: JWT is disabled by default for now. to enable JWT authentication use BLUEOCEAN_FEATURE_JWT_AUTHENTICATION=true system property.

    mvn hpi:run -DBLUEOCEAN_FEATURE_JWT_AUTHENTICATION=true

With -DBLUEOCEAN_FEATURE_JWT_AUTHENTICATION=false (default)

* No JWT tokens are send from the frontend.
* Api does not look for a JWT token, and instead uses cookies for authentication.

With -DBLUEOCEAN_FEATURE_JWT_AUTHENTICATION=true

* JWT tokens are fetched and sent with api requests from the frontend.
* API requires a valid JWT token, and does not use cookies for authentication.


BlueOcean REST APIs requires JWT token for authentication. JWT APIs are provided by blueocean-jwt plugin. See
[JWT APIs](../blueocean-jwt/README.md) to get JWT token and to get public key needed to verify the claims.

JWT token must be sent as bearer token as value of HTTP 'Authorization' header:

    curl -H 'Authorization: Bearer eyJraWQ...' http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/

## API access from browser with JWT enabled

Sometimes testing API from browser is desirable. Here are steps to to do that using Postman Chrome app:

* Install Postman on Chrome (chrome://apps/) or install Postman app on Mac OS (https://www.getpostman.com).
* Launch postman
* Create a JWT token, see [JWT APIs](../blueocean-jwt/README.md). You can customize expiry time to reuse the fetched token. You may like to save the query in Postman as collection *blueocean*. Anytime later you want to generate token use *blueocean* collection and click send on previous GET.
* Click on + on tab and type the API URL, e.g. http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/, then add header with *Authorization* header with value *Bearer COPIED_JWT_TOKEN*. Use this tab to invoke any Blueocean REST API. You may like to either add to 'blueocean' collection if you like.



# Navigability

## Links
Each BlueOcean JSON response object includes *_links" as defined by [HAL](https://tools.ietf.org/html/draft-kelly-json-hal-08) spec.
*self* link references the reachable path to *this* resource. It may include other navigable resources as well. A resource can expose it's methods as navigable by using [@Navigable](https://github.com/jenkinsci/blueocean-plugin/blob/master/blueocean-rest/src/main/java/io/jenkins/blueocean/rest/Navigable.java) annotation.

    "_links" : {
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/f/"
        },
        "runs" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/f/runs/"
        },
        "queue" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/f/queue/"
        }

Above, *self* references path to pipeline 'f', *runs* and *queue* resource are navigable from this resource and their
href references path to them.


# Resource discovery

Each resource provides _class field, it’s a fully qualified name and is an  identifier of the producer of this
resource's capability.

    {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl",
      "_links" : {
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/p/"
        },
        "branches" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/"
        },
        "runs" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/p/runs/"
        },
        "queue" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/p/queue/"
        }
      },
      "displayName" : "p",
      ....
    }


Above a multi-branch pipeline resource object's class is exposed using _class element: *io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl*.

## classes API

### Get class details

To get list of what other classes or capabilities io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl class supports, use *classes* API:

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/classes/io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl
    {
      “classes”:[“io.jenkins.blueocean.rest.model.BlueMultiBranchPipeline”,"io.jenkins.blueocean.rest.model.BluePipeline","io.jenkins.blueocean.rest.model.Resource"]
    }

Above MultiBranchPipelineImpl supports capabilities: BlueMultiBranchPipeline, BluePipeline and Resource.

Frontend can use _class in resource and classes API to serve UI based on class or capability this resource supports.

### Get detailed map of all given classes

    curl -v -X POST  http://localhost:8080/jenkins/blue/rest/classes/ -d '{"q":["io.jenkins.blueocean.service.embedded.rest.PipelineImpl","io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl"]

    {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.ExtensionClassContainerImpl$1",
      "_links" : {
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/classes/?q=io.jenkins.blueocean.service.embedded.rest.PipelineImpl,io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl,io.jenkins.blueocean.service.embedded.PipelineApiTest$TestPipelineImpl/"
        }
      },
      "map" : {
        "io.jenkins.blueocean.service.embedded.rest.PipelineImpl" : {
          "_class" : "io.jenkins.blueocean.service.embedded.rest.ExtensionClassImpl",
          "_links" : {
            "self" : {
              "_class" : "io.jenkins.blueocean.rest.hal.Link",
              "href" : "/blue/rest/classes/io.jenkins.blueocean.service.embedded.rest.PipelineImpl/"
            }
          },
          "classes" : [ "io.jenkins.blueocean.rest.model.BluePipeline", "io.jenkins.blueocean.rest.model.Resource" ]
        },
        "io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl" : {
          "_class" : "io.jenkins.blueocean.service.embedded.rest.ExtensionClassImpl",
          "_links" : {
            "self" : {
              "_class" : "io.jenkins.blueocean.rest.hal.Link",
              "href" : "/blue/rest/classes/io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl/"
            }
          },
          "classes" : [ "io.jenkins.blueocean.rest.model.BlueMultiBranchPipeline", "io.jenkins.blueocean.rest.model.BluePipelineFolder", "io.jenkins.blueocean.rest.model.BluePipeline", "io.jenkins.blueocean.rest.model.Resource" ]
        }
      }
    }

# User API

## Get a user

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/users/alice

    {
      "id" : "alice",
      "fullName" : "Alice"
      "email" : "alice@example.com"
    }

## Find users in an organization

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/users/

    [
      {
        "id" : "alice",
        "name" : "Alice"
      }
    ]

## Get authenticated user

Gives authenticated user, gives HTTP 404 error if there is no authenticated user found.

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/user/

    {
      "id" : "alice",
      "fullName" : "Alice"
      "email" : "alice@example.com"
    }

# Organization API

## Get organization details

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/jenkins

    {
      "name" : "jenkins"
    }

## Get all organizations

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/

    [{
      "name" : "jenkins"
    }]


# Pipeline API

## Get a Pipeline

    curl -v -X GET  "http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1"

    {
      "organization" : "jenkins",
      "name" : "pipeline1",
      "displayName": "pipeline1",
      "fullName": "pipeline1",
      "weatherScore": 100,
      "estimatedDurationInMillis": 20264,
      "latestRun": {
          "changeSet": [],
          "artifacts": [
              {
                  "name": "fizz",
                  "size": 8,
                  "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
              }
          ],
          "durationInMillis": 20264,
          "estimatedDurationInMillis" : 567,
          "enQueueTime": "2016-04-11T17:44:28.342+1000",
          "endTime": "2016-04-11T17:44:48.608+1000",
          "id": "3",
          "organization": "jenkins",
          "pipeline": "mypipe1",
          "result": "SUCCESS",
          "runSummary": "stable",
          "startTime": "2016-04-11T17:44:28.344+1000",
          "state": "FINISHED",
          "type": "WorkflowRun",
          "commitId": null
        }
    }

## Get Pipelines for an organization

Pipelines are sorted by pipeline name alphabetically

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/

    [
      {
      "organization" : "jenkins",
      "name" : "pipeline1",
      "displayName": "pipeline1",
      "fullName" : "pipeline1",
      "weatherScore": 100,
      "estimatedDurationInMillis": 280,
      }
    ]

## Get Pipelines across organization

Pipelines are sorted by pipeline name alphabetically across organizations. It gives flattened list of pipelines including
folders and nested pipelines inside them.

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/search/?q=type:pipeline

    [
      {
      "organization" : "jenkins",
      "name" : "pipeline1",
      "displayName": "pipeline1",
      "fullName" : "pipeline1",
      "weatherScore": 100,
      "estimatedDurationInMillis": 280,
      }
    ]

### Exclude flattening of certain job types

__excludedFromFlattening__ query parameter takes comma separated class names of Jenkins item that should not be flattened.

To exclude flattening multi branch project:

    GET http://localhost:8080/jenkins/blue/rest/search/?q=type:pipeline;organization:jenkins;excludedFromFlattening=jenkins.branch.MultiBranchProject

To exclude flattening a folder:

    GET http://localhost:8080/jenkins/blue/rest/search/?q=type:pipeline;organization:jenkins;excludedFromFlattening=com.cloudbees.hudson.plugins.folder.AbstractFolder

To exclude flattening both a folder and multi-branch projects:

    GET http://localhost:8080/jenkins/blue/rest/search/?q=type:pipeline;organization:jenkins;excludedFromFlattening=jenkins.branch.MultiBranchProject,com.cloudbees.hudson.plugins.folder.AbstractFolder


### Get pipelines for specific organization

Use __organization__ query parameter to get flattened pipelines in that organization. If given organization is not found a 400 BadRequest error is returned.

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/search/?q=type:pipeline;organization:jenkins

      [
         {
            "numberOfFailingBranches" : 0,
            "numberOfSuccessfulBranches" : 0,
            "_links" : {
               "queue" : {
                  "href" : "/blue/rest/organizations/jenkins/pipelines/bo1/queue/",
                  "_class" : "io.jenkins.blueocean.rest.hal.Link"
               },
               "actions" : {
                  "href" : "/blue/rest/organizations/jenkins/pipelines/bo1/actions/",
                  "_class" : "io.jenkins.blueocean.rest.hal.Link"
               },
               "runs" : {
                  "_class" : "io.jenkins.blueocean.rest.hal.Link",
                  "href" : "/blue/rest/organizations/jenkins/pipelines/bo1/runs/"
               },
               "self" : {
                  "_class" : "io.jenkins.blueocean.rest.hal.Link",
                  "href" : "/blue/rest/organizations/jenkins/pipelines/bo1/"
               },
               "branches" : {
                  "href" : "/blue/rest/organizations/jenkins/pipelines/bo1/branches/",
                  "_class" : "io.jenkins.blueocean.rest.hal.Link"
               }
            },
            "organization" : "jenkins",
            "estimatedDurationInMillis" : 1,
            "numberOfFailingPullRequests" : 0,
            "weatherScore" : 0,
            "fullName" : "bo1",
            "_class" : "io.jenkins.blueocean.service.embedded.rest.MultiBranchPipelineImpl",
            "totalNumberOfPullRequests" : 0,
            "runs" : [],
            "displayName" : "bo1",
            "totalNumberOfBranches" : 0,
            "numberOfPipelines" : 0,
            "name" : "bo1",
            "numberOfFolders" : 0,
            "numberOfSuccessfulPullRequests" : 0,
            "actions" : [],
            "branchNames" : []
         }
      ]


## Parameterized Pipeline

A pipeline can define list of parameters pipeline job expects. For example:

      properties([parameters([string(defaultValue: 'xyz', description: 'string param', name: 'param1')]), pipelineTriggers([])])

      node(){
          stage('build'){
              echo "building"
          }
      }

Once this pipeline script is executed, subsequent REST call to get pipeline details (on a branch in multi-branch pipeline or just a pipeline job) will have 'parameters' element with all parameter definitions.

    curl -X GET http://localhost:59702/jenkins/blue/rest/organizations/jenkins/pipelines/p/branches/master/

    {
      "_class" : "io.jenkins.blueocean.rest.impl.pipeline.BranchImpl",
      "_links" : {...},
      "actions" : [...],
      "displayName" : "feature/ux-1",
      "estimatedDurationInMillis" : 1689,
      "fullDisplayName" : "p/master",
      "fullName" : "p/master",
      "latestRun" : {...},
      "name" : "feature%2Fux-1",
      "organization" : "jenkins",
      "parameters" : [ {
        "_class" : "hudson.model.StringParameterDefinition",
        "defaultParameterValue" : {
          "_class" : "hudson.model.StringParameterValue",
          "name" : "param1",
          "value" : "xyz"
        },
        "description" : "string param",
        "name" : "param1",
        "type" : "StringParameterDefinition"
      } ],
      "permissions" : {
        "create" : true,
        "read" : true,
        "start" : true,
        "stop" : true
      },
      "weatherScore" : 100,
      "pullRequest" : null
    }

## Get a Folder

    curl -v -X GET  http://localhost:63934/jenkins/blue/rest/organizations/jenkins/pipelines/folder1/
    {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.PipelineFolderImpl",
      "displayName" : "folder1",
      "fullName" : "folder1",
      "name" : "folder1",
      "organization" : "jenkins",
      "numberOfFolders" : 1,
      "numberOfPipelines" : 1
    }


## Get Nested Pipeline Inside A Folder

    curl -v -X GET   http://localhost:62054/jenkins/blue/rest/organizations/jenkins/pipelines/folder1/pipelines/folder2/pipelines/test2/

    {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.PipelineImpl",
      "displayName" : "test2",
      "estimatedDurationInMillis" : -1,
      "fullName" : "folder1/folder2/test2",
      "latestRun" : null,
      "name" : "test2",
      "fullName" : "test2",
      "organization" : "jenkins",
      "weatherScore" : 100
    }

## Get nested Folder and Pipeline

Pipelines can be nested inside folder.

    curl -v -X GET   http://localhost:62054/jenkins/blue/rest/organizations/jenkins/pipelines/folder1/pipelines/

    [ {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.PipelineFolderImpl",
      "displayName" : "folder2",
      "fullName" : "folder1/folder2",
      "name" : "folder2",
      "organization" : "jenkins",
      "numberOfFolders" : 0,
      "numberOfPipelines" : 1
    }, {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.PipelineImpl",
      "displayName" : "test1",
      "estimatedDurationInMillis" : -1,
      "fullName" : "folder1/test1",
      "latestRun" : null,
      "name" : "test1",
      "organization" : "jenkins",
      "weatherScore" : 100
    } ]

## MultiBranch Pipeline API

Create MultiBranch build and set it up with your git repo. Your git repo must have Jenkinsfile with build script.
Each branch in the repo with Jenkins file will appear as a branch in this pipeline.

### Get MultiBranch pipeline

    curl -v http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/p/

    {
        "displayName": "p",
        "estimatedDurationInMillis": 280,
        "latestRun": null,
        "name": "p",
        "organization": "jenkins",
        "weatherScore": 100,
        "branchNames": [
            "feature2",
            "master",
            "feature1"
        ],
        "numberOfFailingBranches": 0,
        "numberOfFailingPullRequests": 0,
        "numberOfSuccessfulBranches": 0,
        "numberOfSuccessfulPullRequests": 0,
        "totalNumberOfBranches": 3,
        "totalNumberOfPullRequests": 0
    }


### Get MultiBranch pipeline branches

The list of branches will be ordered by favorited branches first, and then branches that have the most recent
activity.

    curl -v http://localhost:56720/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/branches

    [
        {
            "displayName": "feature2",
            "estimatedDurationInMillis": 1391,
            "name": "master",
            "weatherScore":100,
            "latestRun": {
                "changeSet": [

                ],
                "durationInMillis": 1391,
                "estimatedDurationInMillis" : 567,
                "enQueueTime": "2016-04-15T19:59:28.717-0700",
                "endTime": "2016-04-15T19:59:30.114-0700",
                "id": "1",
                "organization": "jenkins",
                "pipeline": "feature2",
                "result": "SUCCESS",
                "runSummary": "stable",
                "startTime": "2016-04-15T19:59:28.723-0700",
                "state": "FINISHED",
                "type": "WorkflowRun",
                "commitId": "662766a80af35404c430240e6996598d5397471e"
            },
            "name": "feature2",
            "organization": "jenkins",
            "weatherScore": 100,
            "pullRequest": {
                "_links": {
                    "self":null
                },
                "author":"<githubuser>",
                "id":"543",
                "title":"Fixes for stuff",
                "url":"https://github.com/jenkinsci/some-plugin/pull/543"
            },
            "totalNumberOfPullRequests": 0
        },
        {
            "displayName": "master",
            "estimatedDurationInMillis": 1468,
            "name": "feature1",
            "weatherScore":100,
            "latestRun": {
                "changeSet": [

                ],
                "artifacts": [
                  {
                      "name": "fizz",
                      "size": 8,
                      "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
                  }
                ],
                "durationInMillis": 1468,
                "estimatedDurationInMillis" : 567,
                "enQueueTime": "2016-04-15T19:59:28.730-0700",
                "endTime": "2016-04-15T19:59:30.199-0700",
                "id": "1",
                "organization": "jenkins",
                "pipeline": "master",
                "result": "SUCCESS",
                "runSummary": "stable",
                "startTime": "2016-04-15T19:59:28.731-0700",
                "state": "FINISHED",
                "type": "WorkflowRun",
                "commitId": "96e0a0f29d9e5b1381ebb1b7503b0be04ed19a5b"
            },
            "name": "master",
            "organization": "jenkins",
            "weatherScore": 100,
            "pullRequest": null,
            "totalNumberOfPullRequests": 0
        },
        {
            "displayName": "feature1",
            "estimatedDurationInMillis": 1443,
            "name": "feature2",
            "weatherScore":100,
            "latestRun": {
                "changeSet": [

                ],
                "durationInMillis": 1443,
                "estimatedDurationInMillis" : 567,
                "enQueueTime": "2016-04-15T19:59:28.723-0700",
                "endTime": "2016-04-15T19:59:30.167-0700",
                "id": "1",
                "organization": "jenkins",
                "pipeline": "feature1",
                "result": "SUCCESS",
                "runSummary": "stable",
                "startTime": "2016-04-15T19:59:28.724-0700",
                "state": "FINISHED",
                "type": "WorkflowRun",
                "commitId": "f436952a7de493603f4937ecb9dac3f79fd13c79"
            },
            "name": "feature1",
            "organization": "jenkins",
            "weatherScore": 100,
            "pullRequest": null,
            "totalNumberOfPullRequests": 0
        }
    ]


## Pipeline Permissions

Pipeline API response gives permission object in response:

Following permissions are returned as key to the permission map: create, start, stop, read for a pipeline job:

* create: User can create a pipeline
* start: User can start a run of this pipeline. If not applicable to certain pipeline then can be false or null.
* stop: User can stop a run of this pipeline. If not applicable to certain pipeline then can be false or null.
* read: User has permission to view this pipeline

For example for anonymous user with security enabled and only read permission, the permission map for a pipeline job is:

    "permissions" : {
        "create" : false,
        "read" : true,
        "start" : false,
        "stop" : false
    }

> Implementation of BluePipeline can provide their own set of permissions in addition to the ones defined here.

# Queue API

## Fetch queue for an pipeline

     curl http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/queue
     [ {
       "_class" : "io.jenkins.blueocean.service.embedded.rest.QueueItemImpl",
       "expectedBuildNumber" : 4,
       "id" : "4",
       "pipeline" : "pipeline1",
       "queuedTime" : 1465433910205
     }, {
       "_class" : "io.jenkins.blueocean.service.embedded.rest.QueueItemImpl",
       "expectedBuildNumber" : 3,
       "id" : "3",
       "pipeline" : "pipeline1",
       "queuedTime" : 1465433910203
     } ]

## GET queue for a MultiBranch pipeline

    curl http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/bo2/queue/

    [
       {
          "_class" : "io.jenkins.blueocean.service.embedded.rest.QueueItemImpl",
          "id" : "64",
          "expectedBuildNumber" : 10,
          "pipeline" : "bug%2FUX-334",
          "_links" : {
             "self" : {
                "_class" : "io.jenkins.blueocean.rest.hal.Link",
                "href" : "/blue/rest/organizations/jenkins/pipelines/bo2/queue/64/"
             }
          },
          "queuedTime" : "2016-06-29T14:11:52.191-0700"
       },
       {
          "id" : "63",
          "_class" : "io.jenkins.blueocean.service.embedded.rest.QueueItemImpl",
          "queuedTime" : "2016-06-29T14:11:51.290-0700",
          "pipeline" : "bug%2FUX-334",
          "_links" : {
             "self" : {
                "_class" : "io.jenkins.blueocean.rest.hal.Link",
                "href" : "/blue/rest/organizations/jenkins/pipelines/bo2/queue/63/"
             }
          },
          "expectedBuildNumber" : 11
       }
    ]

## Remove a queued item

    curl -X DELETE http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/bo2/queue/64/

# Run API

## Get all runs in a pipeline

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs

    [
        {
            "changeSet": [],
            "artifacts": [
              {
                  "name": "fizz",
                  "size": 8,
                  "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
              }
            ],
            "durationInMillis": 841,
            "estimatedDurationInMillis" : 567,
            "enQueueTime": "2016-03-16T09:02:26.492-0700",
            "endTime": "2016-03-16T09:02:27.339-0700",
            "id": "1",
            "organization": "jenkins",
            "pipeline": "pipeline1",
            "result": "SUCCESS",
            "runSummary": "stable",
            "startTime": "2016-03-16T09:02:26.498-0700",
            "state": "FINISHED",
            "type": "WorkflowRun",
            "commitId": null
        }
    ]


## Get a run details

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1

    {
        "changeSet": [],
        "artifacts": [
          {
              "name": "fizz",
              "size": 8,
              "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
          }
        ],
        "durationInMillis": 841,
        "estimatedDurationInMillis" : 567,
        "enQueueTime": "2016-03-16T09:02:26.492-0700",
        "endTime": "2016-03-16T09:02:27.339-0700",
        "id": "1",
        "organization": "jenkins",
        "pipeline": "pipeline1",
        "result": "SUCCESS",
        "runSummary": "stable",
        "startTime": "2016-03-16T09:02:26.498-0700",
        "state": "FINISHED",
        "type": "WorkflowRun",
        "commitId": null
    }

## Find latest run of a pipeline

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/?q=type:run;organization:jenkins;pipeline:pipeline1;latestOnly:true

    [
      {
          "changeSet": [],
          "artifacts": [
            {
                "name": "fizz",
                "size": 8,
                "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
            }
          ],
          "durationInMillis": 841,
          "estimatedDurationInMillis" : 567,
          "enQueueTime": "2016-03-16T09:02:26.492-0700",
          "endTime": "2016-03-16T09:02:27.339-0700",
          "id": "1",
          "organization": "jenkins",
          "pipeline": "pipeline1",
          "result": "SUCCESS",
          "runSummary": "stable",
          "startTime": "2016-03-16T09:02:26.498-0700",
          "state": "FINISHED",
          "type": "WorkflowRun",
          "commitId": null
      }
    ]

## Find latest run on all pipelines

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/?q=type:run;organization:jenkins;latestOnly:true

    [
      {
          "changeSet": [],
          "artifacts": [
            {
                "name": "fizz",
                "size": 8,
                "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
            }
          ],
          "durationInMillis": 841,
          "estimatedDurationInMillis" : 567,
          "enQueueTime": "2016-03-16T09:02:26.492-0700",
          "endTime": "2016-03-16T09:02:27.339-0700",
          "id": "1",
          "organization": "jenkins",
          "pipeline": "pipeline1",
          "result": "SUCCESS",
          "runSummary": "stable",
          "startTime": "2016-03-16T09:02:26.498-0700",
          "state": "FINISHED",
          "type": "WorkflowRun",
          "commitId": null
      }
    ]

## Start a build

    curl -XPOST http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline3/runs/
    {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.QueueItemImpl",
      "_links" : {
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline3/queue/3/"
        }
      },
      "expectedBuildNumber" : 1,
      "id" : "3",
      "pipeline" : "pipeline3",
      "qeueudTime" : "2016-06-22T11:05:41.309+1200"
    }

## Start a parameterized build

Parameterized build can be triggered on a free-style, pipeline and a branch of multi-branch pipeline jobs.

    curl -XPOST -H 'Content-Type: application/json' http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/
    {
      "parameters" : [{
        "name" : "param1",
        "value" : "def"
      }]
    }

Response:

    {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.QueueItemImpl",
      "_links" : {
        "parent" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/"
        },
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/queue/3/"
        }
      },
      "expectedBuildNumber" : 2,
      "id" : "3",
      "organization" : "jenkins",
      "pipeline" : "pipeline1",
      "queuedTime" : "2016-12-22T15:43:52.866+0530"
    }


## Stop a build

> Note: it takes a while to stop, so you may get a state of RUNNING or QUEUED.

    curl -X PUT http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/stop
    {
           "changeSet": [],
           "artifacts": [
             {
                 "name": "fizz",
                 "size": 8,
                 "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
             }
           ],
           "durationInMillis": 841,
           "estimatedDurationInMillis" : 567,
           "enQueueTime": "2016-03-16T09:02:26.492-0700",
           "endTime": "2016-03-16T09:02:27.339-0700",
           "id": "1",
           "organization": "jenkins",
           "pipeline": "pipeline1",
           "result": "ABORTED",
           "runSummary": "stable",
           "startTime": "2016-03-16T09:02:26.498-0700",
           "state": "FINISHED",
           "type": "WorkflowRun",
           "commitId": null
       }

### Stop a build as blocking call

You can pass blocking=true (default false) with optional timeOutInSecs parameter (Default 10 sec). This API tries to
stop running job and between each retries does a sleep for 10% of timeOutInSecs value.

Client should check the state and if its not FINISHED they may issue another stop API call to ensure the build is stopped.

> Note: There is no guarantee, after timeout build build might still be running.

    curl -X PUT http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/stop/?blocking=true&timeOutInSecs=5

    {
           "changeSet": [],
           "artifacts": [
             {
                 "name": "fizz",
                 "size": 8,
                 "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
             }
           ],
           "durationInMillis": 841,
           "estimatedDurationInMillis" : 567,
           "enQueueTime": "2016-03-16T09:02:26.492-0700",
           "endTime": "2016-03-16T09:02:27.339-0700",
           "id": "1",
           "organization": "jenkins",
           "pipeline": "pipeline1",
           "result": "ABORTED",
           "runSummary": "stable",
           "startTime": "2016-03-16T09:02:26.498-0700",
           "state": "FINISHED",
           "type": "WorkflowRun",
           "commitId": null
       }


## Get MultiBranch job's branch run detail

    curl -v http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/branches/feature1/runs/1

    {
        "durationInMillis": 1330,
        "estimatedDurationInMillis" : 567,
        "enQueueTime": "2016-03-16T09:08:15.607-0700",
        "endTime": "2016-03-16T09:08:16.942-0700",
        "id": "1",
        "organization": "jenkins",
        "pipeline": "feature1",
        "result": "SUCCESS",
        "runSummary": "stable",
        "startTime": "2016-03-16T09:08:15.612-0700",
        "state": "FINISHED",
        "type": "WorkflowRun",
        "commitId": "aad1c51fb29e053d1ccb20dbcdb1fe28fddcfba5",
        "changeSet": []
    }

## Get all runs for all branches on a multibranch pipeline (ordered by date)

     curl -v http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs

    [
        {
            "changeSet": [

            ],
            "artifacts": [
              {
                  "name": "fizz",
                  "size": 8,
                  "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
              }
            ],
            "durationInMillis": 1875,
            "estimatedDurationInMillis" : 567,
            "enQueueTime": "2016-03-10T15:27:13.687+1300",
            "endTime": "2016-03-10T15:27:15.567+1300",
            "id": "1",
            "organization": "jenkins",
            "pipeline": "feature1",
            "result": "SUCCESS",
            "runSummary": "stable",
            "startTime": "2016-03-10T15:27:13.692+1300",
            "state": "FINISHED",
            "type": "WorkflowRun",
            "commitId": "52615df5828f1dddf672b86d64196294e3fbee88"
        },
        {
            "changeSet": [

            ],
            "durationInMillis": 1716,
            "estimatedDurationInMillis" : 567,
            "enQueueTime": "2016-03-10T15:27:13.692+1300",
            "endTime": "2016-03-10T15:27:15.409+1300",
            "id": "1",
            "organization": "jenkins",
            "pipeline": "master",
            "result": "SUCCESS",
            "runSummary": "stable",
            "startTime": "2016-03-10T15:27:13.693+1300",
            "state": "FINISHED",
            "type": "WorkflowRun",
            "commitId": "bfd1f72dc63ca63a8c1b152dc9263c7c81862afa"
        },
        {
            "changeSet": [

            ],
            "durationInMillis": 1714,
            "estimatedDurationInMillis" : 567,
            "enQueueTime": "2016-03-10T15:27:13.700+1300",
            "endTime": "2016-03-10T15:27:15.415+1300",
            "id": "1",
            "organization": "jenkins",
            "pipeline": "feature2",
            "result": "SUCCESS",
            "runSummary": "stable",
            "startTime": "2016-03-10T15:27:13.701+1300",
            "state": "FINISHED",
            "type": "WorkflowRun",
            "commitId": "84cb56b50589e720385ef2491a1ebab9d227da6e"
        }
    ]

## Get latest activity of Multi-branch pipeline for all branches

     curl -v http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/activities/

        [
            {
                "changeSet": [

                ],
                "artifacts": [
                  {
                      "name": "fizz",
                      "size": 8,
                      "url": "/jenkins/job/pipeline1/1/artifact/dir/fizz"
                  }
                ],
                "durationInMillis": 1875,
                "estimatedDurationInMillis" : 567,
                "enQueueTime": "2016-03-10T15:27:13.687+1300",
                "endTime": "2016-03-10T15:27:15.567+1300",
                "id": "1",
                "organization": "jenkins",
                "pipeline": "feature1",
                "result": "SUCCESS",
                "runSummary": "stable",
                "startTime": "2016-03-10T15:27:13.692+1300",
                "state": "FINISHED",
                "type": "WorkflowRun",
                "commitId": "52615df5828f1dddf672b86d64196294e3fbee88"
            },
            {
                "changeSet": [

                ],
                "durationInMillis": 1716,
                "estimatedDurationInMillis" : 567,
                "enQueueTime": "2016-03-10T15:27:13.692+1300",
                "endTime": "2016-03-10T15:27:15.409+1300",
                "id": "1",
                "organization": "jenkins",
                "pipeline": "master",
                "result": "SUCCESS",
                "runSummary": "stable",
                "startTime": "2016-03-10T15:27:13.693+1300",
                "state": "FINISHED",
                "type": "WorkflowRun",
                "commitId": "bfd1f72dc63ca63a8c1b152dc9263c7c81862afa"
            },
            {
                "changeSet": [

                ],
                "durationInMillis": 1714,
                "estimatedDurationInMillis" : 567,
                "enQueueTime": "2016-03-10T15:27:13.700+1300",
                "endTime": "2016-03-10T15:27:15.415+1300",
                "id": "1",
                "organization": "jenkins",
                "pipeline": "feature2",
                "result": "SUCCESS",
                "runSummary": "stable",
                "startTime": "2016-03-10T15:27:13.701+1300",
                "state": "FINISHED",
                "type": "WorkflowRun",
                "commitId": "84cb56b50589e720385ef2491a1ebab9d227da6e"
            }
        ]


> This API collects runs (in descending order) for each branch in a multi-branch project( branches sorted in descending order of branch with latest activity). It fetches max up to 250 runs for each branch by default, it can be changed using JVM property MAX_MBP_RUNS_ROWS.


## Get change set for a run

    curl -v http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/branches/master/runs/2/

    {
        "changeSet": [
            {
                "author": {
                    "email": "vivek.pandey@gmail.com",
                    "fullName": "vivek.pandey",
                    "id": "vivek.pandey"
                },
                "affectedPaths": [
                    "file"
                ],
                "commitId": "e2d1d695a2009ac44d97e6e7a542ba3786153c41",
                "comment": "tweaked11\n",
                "date": "2016-03-02 16:49:26 -0800",
                "id": "e2d1d695a2009ac44d97e6e7a542ba3786153c41",
                "msg": "tweaked11",
                "paths": [
                    {
                        "editType": "edit",
                        "file": "file"
                    }
                ],
                "timestamp": "2016-03-02T16:49:26.000-0800"
            }
        ],
        "durationInMillis": 348,
        "estimatedDurationInMillis" : 567,
        "enQueueTime": "2016-03-02T16:49:26.548-0800",
        "endTime": "2016-03-02T16:49:26.898-0800",
        "id": "2",
        "organization": "jenkins",
        "pipeline": "master",
        "runSummary": "stable",
        "startTime": "2016-03-02T16:49:26.550-0800",
        "status": "SUCCESS",
        "type": "WorkflowRun"
    }
## Pipeline Node API

### Get Pipeline run nodes
    curl -v  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/nodes/

    [ {
      "displayName" : "build",
      "durationInMillis" : 219,
      "edges" : [ {
        "id" : "9"
      } ],
      "id" : "3",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:15:08.719-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "test",
      "durationInMillis" : 158,
      "edges" : [ {
        "id" : "13"
      }, {
        "id" : "14"
      }, {
        "id" : "15"
      } ],
      "id" : "9",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:15:08.938-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "unit",
      "durationInMillis" : 127,
      "edges" : [ {
        "id" : "35"
      } ],
      "id" : "13",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:15:08.942-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "integration",
      "durationInMillis" : 126,
      "edges" : [ {
        "id" : "35"
      } ],
      "id" : "14",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:15:08.944-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "ui",
      "durationInMillis" : 137,
      "edges" : [ {
        "id" : "35"
      } ],
      "id" : "15",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:15:08.945-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "deploy",
      "durationInMillis" : 47,
      "edges" : [ ],
      "id" : "35",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:15:09.096-0700",
      "state" : "FINISHED"
    } ]

> In case pipeline run fails in one of the parallel branch, enclosing stage node will appear failed as well.

> In case if the pipeline is in progress or failed in the middle, the response may include future nodes if there was
  last successful pipeline build. The returned future nodes will have startTime, result and state as null.
  Also the last node's edges will be patched to point to the future node.

From the above example, if build failed at parallel node *unit* then the response will be:

    [ {
      "displayName" : "build",
      "durationInMillis" : 51,
      "edges" : [ {
        "id" : "9"
      } ],
      "id" : "3",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:39:18.569-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "test",
      "durationInMillis" : 344,
      "edges" : [ {
        "id" : "13"
      }, {
        "id" : "14"
      }, {
        "id" : "15"
      } ],
      "id" : "9",
      "result" : "FAILURE",
      "startTime" : "2016-05-06T15:39:18.620-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "unit",
      "durationInMillis" : 329,
      "edges" : [ {
        "id" : "35"
      } ],
      "id" : "13",
      "result" : "FAILURE",
      "startTime" : "2016-05-06T15:39:18.622-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "integration",
      "durationInMillis" : 97,
      "edges" : [ {
        "id" : "35"
      } ],
      "id" : "14",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:39:18.623-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "ui",
      "durationInMillis" : 107,
      "edges" : [ {
        "id" : "35"
      } ],
      "id" : "15",
      "result" : "SUCCESS",
      "startTime" : "2016-05-06T15:39:18.623-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "deploy",
      "durationInMillis" : null,
      "edges" : [ {
        "id" : "41"
      } ],
      "id" : "35",
      "result" : null,
      "startTime" : null,
      "state" : null
    }, {
      "displayName" : "deployToProd",
      "durationInMillis" : null,
      "edges" : [ ],
      "id" : "41",
      "result" : null,
      "startTime" : null,
      "state" : null
    } ]

### Get a Pipeline run node's detail

    curl -v  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/nodes/3

    {
        "displayName": "build",
        "edges": [
            {
                "id": "9"
            }
        ],
        "id": "3",
        "startTime": "2016-03-11T00:32:52.273-0800",
        "status": "SUCCESS",
        "state": "FINISHED"
    }

## Pipeline Steps API

This API gives steps inside a pipeline node. For a Stage, the steps will include all the steps defined inside Parallels as well as the stage.


### Get steps for a Pipeline node

Given this pipeline script:

    stage 'build'
    node{
      echo "Building..."
    }

    stage 'test'
    parallel 'unit':{
      node{
        echo "Unit testing..."
      }
    },'integration':{
      node{
        echo "Integration testing..."
      }
    }, 'ui':{
      node{
        echo "UI testing..."
      }
    }

    stage 'deploy'
    node{
      echo "Deploying"
    }

    stage 'deployToProd'
    node{
      echo "Deploying to production"
    }


Get steps of 'test' stage node:

    GET http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/nodes/9/steps/

    [ {
      "displayName" : "Print Message",
      "durationInMillis" : 1,
      "id" : "21",
      "result" : "SUCCESS",
      "startTime" : "2016-05-13T09:37:01.230-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "Shell Script",
      "durationInMillis" : 2,
      "id" : "22",
      "result" : "SUCCESS",
      "startTime" : "2016-05-13T09:37:01.231-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "Print Message",
      "durationInMillis" : 1,
      "id" : "23",
      "result" : "SUCCESS",
      "startTime" : "2016-05-13T09:37:01.233-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "Print Message",
      "durationInMillis" : 1,
      "id" : "28",
      "result" : "SUCCESS",
      "startTime" : "2016-05-13T09:37:01.266-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "Shell Script",
      "durationInMillis" : 272,
      "id" : "32",
      "result" : "SUCCESS",
      "startTime" : "2016-05-13T09:37:01.474-0700",
      "state" : "FINISHED"
    }, {
      "displayName" : "Print Message",
      "durationInMillis" : 2,
      "id" : "39",
      "result" : "SUCCESS",
      "startTime" : "2016-05-13T09:37:01.784-0700",
      "state" : "FINISHED"
    } ]

### Get a Pipeline step details

    GET http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/nodes/13/steps/21/
    {
      "displayName" : "Print Message",
      "durationInMillis" : 1,
      "id" : "21",
      "result" : "SUCCESS",
      "startTime" : "2016-05-13T09:37:01.230-0700",
      "state" : "FINISHED"
    }

### Get Pipeline Steps

    Gives all steps in a pipeline. Excludes stages and parallels/blocks.

    curl http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/steps/

    [ {
      "_class" : "io.jenkins.blueocean.rest.model.GenericResource",
      "displayName" : "Shell Script",
      "durationInMillis" : 70,
      "id" : "5",
      "result" : "SUCCESS",
      "startTime" : "2016-06-18T13:28:29.443+0900"
    }, {
      "_class" : "io.jenkins.blueocean.rest.model.GenericResource",
      "displayName" : "Print Message",
      "durationInMillis" : 1,
      "id" : "10",
      "result" : "SUCCESS",
      "startTime" : "2016-06-18T13:28:29.545+0900"
    }, {
      "_class" : "io.jenkins.blueocean.rest.model.GenericResource",
      "displayName" : "Shell Script",
      "durationInMillis" : 265,
      "id" : "11",
      "result" : "SUCCESS",
      "startTime" : "2016-06-18T13:28:29.546+0900"
    }, {
      "_class" : "io.jenkins.blueocean.rest.model.GenericResource",
      "displayName" : "Shell Script",
      "durationInMillis" : 279,
      "id" : "12",
      "result" : "SUCCESS",
      "startTime" : "2016-06-18T13:28:29.811+0900"
    } ]


### Get Pipeline Steps with Input

    curl -v -X GET http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/p31/runs/22/nodes/9/steps/

    [ {
      "_class" : "io.jenkins.blueocean.rest.impl.pipeline.PipelineStepImpl",
      "_links" : {
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/steps/12/"
        },
        "actions" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/steps/12/actions/"
        }
      },
      "actions" : [...],
      "displayName" : "Wait for interactive input",
      "durationInMillis" : 81,
      "id" : "12",
      "input" : {
        "_class" : "io.jenkins.blueocean.rest.impl.pipeline.InputStepImpl",
        "_links" : {
          "self" : {
            "_class" : "io.jenkins.blueocean.rest.hal.Link",
            "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/steps/12/input/"
          }
        },
        "id" : "C51b52435b43a326d5d4f92c290a64d5",
        "message" : "Please input branch to test against",
        "ok" : "Proceed",
        "parameters" : [ {
          "_class" : "hudson.model.StringParameterDefinition",
          "defaultParameterValue" : {
            "_class" : "hudson.model.StringParameterValue",
            "name" : "branch",
            "value" : "master"
          },
          "description" : "",
          "name" : "branch",
          "type" : "StringParameterDefinition"
        } ],
        "submitter" : null
      },
      "result" : "UNKNOWN",
      "startTime" : "2016-12-21T17:41:58.488+0530",
      "state" : "PAUSED"
    } ]

### Submit step input to proceed

    curl -v -u 'xxx:yyy'  -H 'Content-Type: application/json' -X POST http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/p31/runs/22/nodes/9/steps/12/ -d
    '{
       "id" : "C51b52435b43a326d5d4f92c290a64d5",
       "parameters" : [{
         "name" : "branch",
         "value" : "master"
       }]
     }'

Above, "id" is the input.id received in GET /steps/ call:

     curl -v -X GET http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/p31/runs/22/nodes/9/steps/
     [ {
           "_class" : "io.jenkins.blueocean.rest.impl.pipeline.PipelineStepImpl",
           "_links" : {
             "self" : {
               "_class" : "io.jenkins.blueocean.rest.hal.Link",
               "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/steps/12/"
             },
             "actions" : {
               "_class" : "io.jenkins.blueocean.rest.hal.Link",
               "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/steps/12/actions/"
             }
           },
           "actions" : [...],
           "displayName" : "Wait for interactive input",
           "durationInMillis" : 81,
           "id" : "12",
           "input" : {
             "_class" : "io.jenkins.blueocean.rest.impl.pipeline.InputStepImpl",
             "_links" : {
               "self" : {
                 "_class" : "io.jenkins.blueocean.rest.hal.Link",
                 "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/steps/12/input/"
               }
             },
             "id" : "C51b52435b43a326d5d4f92c290a64d5",
             "message" : "Please input branch to test against",
             "ok" : "Proceed",
             "parameters" : [ {
               "_class" : "hudson.model.StringParameterDefinition",
               "defaultParameterValue" : {
                 "_class" : "hudson.model.StringParameterValue",
                 "name" : "branch",
                 "value" : "master"
               },
               "description" : "",
               "name" : "branch",
               "type" : "StringParameterDefinition"
             } ],
             "submitter" : null
           },
           "result" : "UNKNOWN",
           "startTime" : "2016-12-21T17:41:58.488+0530",
           "state" : "PAUSED"
         } ]

Here input.id is 'C51b52435b43a326d5d4f92c290a64d5' and this must be sent as 'id' element in POST call to submit input action.

### Submit step input to abort

    curl -v -u 'xxx:yyy'  -H 'Content-Type: application/json' -X POST http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/p31/runs/22/nodes/9/steps/12/ -d
    '{
       "id" : "C51b52435b43a326d5d4f92c290a64d5",
       "abort" : true
     }'

## Replay a pipeline build

This will queue up a replay of the pipeline run with the same commit id as the run used

    curl -XPOST http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline3/runs/1/replay
    {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.QueueItemImpl",
      "id" : "64",
      "expectedBuildNumber" : 10,
      "pipeline" : "bug%2FUX-334",
      "_links" : {
         "self" : {
            "_class" : "io.jenkins.blueocean.rest.hal.Link",
            "href" : "/blue/rest/organizations/jenkins/pipelines/bo2/queue/64/"
         }
      },
      "queuedTime" : "2016-06-29T14:11:52.191-0700"
   }

# Favorite API

Favorite API can be used to favorite a pipeline (Multi-branch, branch, pipeline or even folder) for a logged in user.
If favorite request is successful then the response is favorited item.

    curl -u alice:xxx -H"Content-Type:application/json" -XPUT -d '{"favorite":true} ttp://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/favorite

    {
        "_class" : "io.jenkins.blueocean.service.embedded.rest.FavoriteImpl",
        "_links" : {
                  "self" : {
                     "_class" : "io.jenkins.blueocean.rest.hal.Link",
                     "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/favorite/"
                  }
               },
       "item" : {
          "displayName" : "pipeline1",
          "_links" : {
             "runs" : {
                "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/",
                "_class" : "io.jenkins.blueocean.rest.hal.Link"
             },
             "self" : {
                "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/",
                "_class" : "io.jenkins.blueocean.rest.hal.Link"
             },
             "queue" : {
                "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/queue/",
                "_class" : "io.jenkins.blueocean.rest.hal.Link"
             },
             "actions" : {
                "_class" : "io.jenkins.blueocean.rest.hal.Link",
                "href" : "/blue/rest/organizations/jenkins/pipelines/pipeline1/actions/"
             }
          },
          "organization" : "jenkins",
          "latestRun" : null,
          "name" : "pipeline1",
          "actions" : [],
          "weatherScore" : 100,
          "_class" : "io.jenkins.blueocean.service.embedded.rest.PipelineImpl",
          "fullName" : "pipeline1",
          "estimatedDurationInMillis" : -1
       }
    }



## Favorite a pipeline
Returns 200 on success. Must be authenticated.

    curl -u bob:bob -H"Content-Type:application/json" -XPUT -d '{"favorite":true} ttp://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/favorite/

## Favorite a multi branch pipeline
Must be authenticated.

Favorited multi-branch pipeline returns master branch as favorited item. Returns 200 on success. 400 if master does not exist

    curl -u bob:bob  -H"Content-Type:application/json" -XPUT -d '{"favorite":true} http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/favorite/

## Un-favorite a multi branch pipeline
Must be authenticated.

This un-favorites the master branch. Returns 200 on success. 400 if master does not exist

    curl -u bob:bob  -H"Content-Type:application/json" -XPUT -d '{"favorite":false} http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/favorite/


## Favorite a multi branch pipeline branch
Returns 200 on success. Must be authenticated.

    curl -H"Content-Type:application/json" -XPUT -d '{"favorite":true} http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/branches/master/favorite/

## Un-favorite a multi branch pipeline branch
Returns 200 on success. Must be authenticated.

    curl -H"Content-Type:application/json" -XPUT -d '{"favorite":false} http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/branches/master/favorite/


## Fetch user favorites
Must be authenticated.

    curl -u bob:bob  http://localhost:8080/jenkins/blue/rest/users/bob/favorites/

    [ {
      "_class" : "io.jenkins.blueocean.service.embedded.rest.FavoriteImpl",
      "_links" : {
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/blue/rest/users/alice/favorites/p%2Fmaster/"
        }
      },
      "item" : {
        "_class" : "io.jenkins.blueocean.service.embedded.rest.BranchImpl",
        "_links" : {
          "self" : {
            "_class" : "io.jenkins.blueocean.rest.hal.Link",
            "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/"
          },
          "actions" : {
            "_class" : "io.jenkins.blueocean.rest.hal.Link",
            "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/actions/"
          },
          "runs" : {
            "_class" : "io.jenkins.blueocean.rest.hal.Link",
            "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/runs/"
          },
          "queue" : {
            "_class" : "io.jenkins.blueocean.rest.hal.Link",
            "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/queue/"
          }
        },
        "actions" : [ ],
        "displayName" : "master",
        "estimatedDurationInMillis" : 953,
        "fullName" : "p/master",
        "latestRun" : {
          "_class" : "io.jenkins.blueocean.service.embedded.rest.PipelineRunImpl",
          "_links" : {
            "nodes" : {
              "_class" : "io.jenkins.blueocean.rest.hal.Link",
              "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/runs/1/nodes/"
            },
            "log" : {
              "_class" : "io.jenkins.blueocean.rest.hal.Link",
              "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/runs/1/log/"
            },
            "self" : {
              "_class" : "io.jenkins.blueocean.rest.hal.Link",
              "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/runs/1/"
            },
            "actions" : {
              "_class" : "io.jenkins.blueocean.rest.hal.Link",
              "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/runs/1/actions/"
            },
            "steps" : {
              "_class" : "io.jenkins.blueocean.rest.hal.Link",
              "href" : "/blue/rest/organizations/jenkins/pipelines/p/branches/master/runs/1/steps/"
            }
          },
          "actions" : [ ],
          "artifacts" : [ ],
          "changeSet" : [ ],
          "durationInMillis" : 953,
          "enQueueTime" : "2016-07-08T13:27:15.250-0700",
          "endTime" : "2016-07-08T13:27:16.204-0700",
          "estimatedDurationInMillis" : 953,
          "id" : "1",
          "organization" : "jenkins",
          "pipeline" : "master",
          "result" : "SUCCESS",
          "runSummary" : "stable",
          "startTime" : "2016-07-08T13:27:15.251-0700",
          "state" : "FINISHED",
          "type" : "WorkflowRun",
          "commitId" : "0cd84cc9a1a62fbe636e5d1197ef7a5cc4c56b63"
        },
        "name" : "master",
        "organization" : "jenkins",
        "weatherScore" : 100,
        "pullRequest" : null
      }
    } ]


# Log API

## Fetching logs

Clients should look for HTTP header *X-TEXT-SIZE* and *X-More-Data* in the response.

 By default only last 150 KB log data is returned in the response. You can fetch full log by sending start=0 query
 parameter. You can override default log size from 150KB to other values using thresholdInKB query parameter.

* X-More-Data Header

If *X-More-Data* is true, then client should repeat the request after some delay. In the repeated request it should use
*X-TEXT-SIZE* header value with *start* query parameter.

* X-TEXT-SIZE Header

X-TEXT-SIZE is the byte offset of the raw log file client should use in the next request as value of start query parameter.

* start Query Parameter

start query parameter tells API to send log starting from this offset in the log file.

* thresholdInKB Query Parameter

Size of log to return in the response. Default value is 150 KB of log data.


## Download a log for a Pipeline run

This will show up as a download in the browser.

    curl -v http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/log?start=0&download=true


## Get log for a Pipeline run

    curl -v http://localhost:56748/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/log?start=0

    Content-Type: text/plain; charset=utf-8
    X-Text-Size: 1835
    X-More-Data: false

    Started
    [Pipeline] Allocate node : Start
    Running on master in /var/folders/5q/51y3qf0x5t39d4c4c_c2l1s40000gn/T/hudson6188345779815397724test/workspace/pipeline1
    [Pipeline] node {
    [Pipeline] stage (Build1)
    Entering stage Build1
    Proceeding
    [Pipeline] echo
    Building
    [Pipeline] stage (Test1)
    Entering stage Test1
    Proceeding
    [Pipeline] echo
    Testing
    [Pipeline] } //node
    [Pipeline] Allocate node : End
    [Pipeline] End of Pipeline
    Finished: SUCCESS

> Note: Fetching log on a Multi-Branch project will give 404 as a Multi-Branch project doesn't have run of it's own, it's essentially a folder hence no logs.

## Get log for a Pipeline step

    GET http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/pipeline1/runs/1/nodes/13/steps/21/log/

    Unit testing...

# SCM API

## Validate Github personal access token

This API does the following:

- Calls SCM provider API, for example GitHub API, to validate the token as well as look for appropriate scopes (in case of GitHub its repo and user:email). It picks up SCM provider from URL path (../scm/:id/validate)
- If the token is valid
  - Look for domain 'github-domain' with github api url specifications in authenticated user's  credential store. If its not found then a new one is created.
  - If the token is valid and there is no Jenkins credentials found with id 'github' in authenticated user scoped domain 'github-domain' then this new credential is created.
  - If there exists a Jenkins credentials with authenticated user scope, in user scope domain named 'github-domain' and credentialId == scm id 'github', then this credential is updated with the given token. SCM id is picked from URL path (../scm/:id/validate).
  - HTTP response with credentialId and status 200 is returned
- If the token is not valid for any reason then 403 error is returned with cause of validation failure.

eg:

```
curl -v -u admin:admin -d '{"accessToken": boo"}' -H "Content-Type:application/json" -XPUT http://localhost:8080/jenkins/blue/rest/organizations/jenkins/scm/github/validate
```

Response:

````
{
  "credentialId" : "github"
}
````
If invalid/forbidden/unauthorized 403 error is returned. For bad request 400.

## Check SCM for available credentialId to use:

````
curl -v -u xxx:yyy http://localhost:8080/jenkins/blue/rest/organizations/jenkins/scm/github/

{
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubScm",
  "_links" : {
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/"
    }
  },
  "credentialId" : ".....",
  "id" : "github",
  "uri" : "https://api.github.com"
}
````

## List organizations of SCM (e.g. github)

> As prerequisite GitHub personal access token must be set as Credential with id 'github' in 'github-domain' domain of authenticated user's credential store. Calling validate access token API above automatically sets it up for you. You can also do it manually.

> Credential id corresponding to github personal access token must be sent either as query parameter 'credentialId' or as HTTP header X-CREDENTIAL-ID. If both are provided query parameter takes precedence.

````
curl -XGET -u xxx:yyy http://localhost:8080/jenkins/blue/rest/organizations/jenkins/scm/github/organizations/?credentialId=github

[ {
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubOrganization",
  "_links" : {
    "repositories" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/jenkinsci/repositories/"
    },
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/jenkinsci/"
    }
  },
  "jenkinsOrganizationPipeline" : false,
  "name" : "jenkinsci"
}, {
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubOrganization",
  "_links" : {
    "repositories" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/CloudBees-community/repositories/"
    },
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/CloudBees-community/"
    }
  },
  "jenkinsOrganizationPipeline" : false,
  "name" : "CloudBees-community"
}, {
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubOrganization",
  "_links" : {
    "repositories" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/cloudbees/repositories/"
    },
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/cloudbees/"
    }
  },
  "jenkinsOrganizationPipeline" : false,
  "name" : "cloudbees"
}, {
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubUserOrganization",
  "_links" : {
    "repositories" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/vivek/repositories/"
    },
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/vivek/"
    }
  },
  "jenkinsOrganizationPipeline" : false,
  "name" : "vivek"
}, {
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubOrganization",
  "_links" : {
    "repositories" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/stapler/repositories/"
    },
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/stapler/"
    }
  },
  "jenkinsOrganizationPipeline" : false,
  "name" : "stapler"
}, {
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubOrganization",
  "_links" : {
    "repositories" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/jruby/repositories/"
    },
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/jruby/"
    }
  },
  "jenkinsOrganizationPipeline" : false,
  "name" : "jruby"
} ]
````

## Repositories API

> Credential id corresponding to github personal access token must be sent either as query parameter 'credentialId' or as HTTP header X-CREDENTIAL-ID. If both are provided query parameter takes precedence.

### Get SCM repositories in an organization

````
curl -v -u xxx:yyy http://localhost:8080/jenkins/blue/rest/organizations/jenkins/scm/github/organizations/CloudBees-community/repositories/?credentialId=github&pageSize=10&pageNumber=3

{
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubRepositoryContainer",
  "_links" : {
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/CloudBees-community/repositories/"
    }
  },
  "repositories" : {
    "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubRepositories",
    "_links" : {
      "self" : {
        "_class" : "io.jenkins.blueocean.rest.hal.Link",
        "href" : "/organizations/jenkins/scm/github/organizations/CloudBees-community/repositories/"
      }
    },
    "items" : [ {
      "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubRepository",
      "_links" : {
        "self" : {
          "_class" : "io.jenkins.blueocean.rest.hal.Link",
          "href" : "/organizations/jenkins/scm/github/organizations/CloudBees-community/repositories/bees-cli-router-plugin/"
        }
      },
      "defaultBranch" : "master",
      "description" : "CloudBees SDK \"router:*\" plugin",
      "name" : "bees-cli-router-plugin",
      "permissions" : {
        "admin" : false,
        "push" : false,
        "pull" : true
      },
      ...],
    "lastPage" : 5,
    "nextPage" : 4,
    "pageSize" : 10
  }
}
````

#### Pagination for GitHub repositories

Repositories response includes nextPage, lastPage and pageSize. nextPage or lastPage might be null if there is no more pages available.

> use pageSize and pageNumber query parameter to get number of items in a page and which page number is needed. Default value of pageNumber is 1 and default and max size is 100.


### Get SCM repository in an organization

````
curl -v -u xxx:yyy http://localhost:8080/jenkins/blue/rest/organizations/jenkins/scm/github/organizations/CloudBees-community/repositories/game-of-life/?credentialId=github

{
  "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubRepository",
  "_links" : {
    "self" : {
      "_class" : "io.jenkins.blueocean.rest.hal.Link",
      "href" : "/organizations/jenkins/scm/github/organizations/CloudBees-community/repositories/game-of-life/?credentialId=github"
    }
  },
  "defaultBranch" : "master",
  "description" : "Demo application for the 'Jenkins: The Definitive Guide' book",
  "name" : "game-of-life",
  "permissions" : {
    "admin" : false,
    "push" : false,
    "pull" : true
  },
  "private" : false,
  "fullName" : "CloudBees-community/game-of-life"
}
````

### Get Github file content of a pipeline (Multibranch or OrganizationFolder)

Parameters:

- **path**

Required. path to file from repo root. e.g. Jenkinsfile

- **repo**

Optional if request is in context of MBP pipeline, required if made in context of organization folder

- **branch**

Optional in case request is made in context of MBP pipeline branch. If missing default branch is assumed if scm
supports default branch. Required in all other cases.

- **type**

Optional. Defaults to file.

#### Get github file content from MBP branch

```
curl -v -u xxx:yyy "http://127.0.0.1:8080/jenkins/blue/rest/organizations/jenkins/pipelines/vivek1/pipelines/test-no-jenkins-file/branches/master/scm/content/?path=Jenkinsfile"
```

#### Get github file content from MBP folder

```
curl -v -u xxx:yyy "http://127.0.0.1:8080/jenkins/blue/rest/organizations/jenkins/pipelines/vivek1/pipelines/test-no-jenkins-file/scm/content/?path=Jenkinsfile&branch=test1"
```

#### Get github file content from org folder

```
curl -v -u xxx:yyy "http://127.0.0.1:8080/jenkins/blue/rest/organizations/jenkins/pipelines/vivek1/scm/content/?path=Jenkinsfile&repo=test-no-jenkins-file&branch=test1"
```

Response:

```
{
   "content" : {
      "name" : "Jenkinsfile",
      "sha" : "f13b26341cf403aa7d697bc252908de092ee279d",
      "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubContent",
      "repo" : "test-no-jenkins-file",
      "size" : 7,
      "owner" : "vivek",
      "path" : "Jenkinsfile",
      "base64Data": "VGVzdDEyMw=="
   },
   "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubFile"
}
```

### Save file content to SCM repo

#### Save file to an OrganizationFolder

SCM owner and credentials are computed from the OrganizationFolder. Request must include **repo** element.

```
curl -H 'Content-Type: application/json' -u user:password -XPUT http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/vivek/scm/content/ -d

'{
  "content" : {
    "message" : "first commit",
    "path" : "Jenkinsfile",
    "branch" : "test1",
    "repo" : "test-no-jenkins-file",
    "sha" : "9e82c4011cd70446a2f44881a6c288c59b4abac0",
    "base64Data" : "VGVzdDEyMw=="
  }
}'
```

#### Save file to a MultiBranchProject

SCM owner, repo and credentials are computed from the MultiBranchProject.

```
curl -H 'Content-Type: application/json' -u user:password -XPUT http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/vivek/pipelines/test-no-jenkins-file/scm/content/ -d

'{
  "content" : {
    "message" : "first commit",
    "path" : "Jenkinsfile",
    "branch" : "test1",
    "sha" : "9e82c4011cd70446a2f44881a6c288c59b4abac0",
    "base64Data" : "VGVzdDEyMw=="
  }
}'
```

- If file **path** doesn't exist in SCM then a new file will be created
- If **sha** is provided and file **path** exists then it must match with the sha of existing file, else 400 (Bad Request) error will be returned.
- If **sha** matches then the file will be updated with the content provided in the request
- If **branch** element is not provided file will be saved on default branch (typically maser)
- If **branch** element is present and this branch doesn't exist then a new branch will be created off default branch HEAD

Response

```
{
   "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubFile",
   "content" : {
      "_class" : "io.jenkins.blueocean.blueocean_github_pipeline.GithubContent",
      "sha" : "f13b26341cf403aa7d697bc252908de092ee279d",
      "path" : "Jenkinsfile4",
      "owner" : "vivek",
      "repo" : "test-no-jenkins-file",
      "name" : "Jenkinsfile4"
   }
}
```
# Jenkins JavaScript Extensions

Jenkins JavaScript Extensions are extensions which contribute to the UI in Jenkins BlueOcean.
This module is used to define extension points - locations where the application accepts plugin-provided implementations.
This module is also used to process the plugin extension point implementations to provide to BlueOcean.

This module is published via npm as `@jenkins-cd/js-extensions` so that other plugins, external to the blueocean project, can make use of it.
Plugins can themselves make use of extension points.

Jenkins JavaScript Extensions are based on the extensibility model already established by Jenkins, based on data and views, with the ability to inherit views based on parent data types.

Jenkins JavaScript Extensions: `@jenkins-cd/js-extensions` module exports:
- `Renderer` - a React component to conveniently render extensions
- `store` - the `ExtensionStore` instance (which must be initialized before it can be used)
- `classMetadataStore` - class/capability metadata store
- `dataType()` - function for filtering extensions based on the data type
- `componentType()` - function for filtering extensions based on the required component type (e.g. React class)

### ExtensionStore API

The `ExtensionStore` API is very simple, all public methods are asynchronous:

- `getExtensions(extensionPointName, [filter,] onload)`
    This method will async load data, filter the extensions based on the provided `filter`s, and call the onload handler with a list of extension exports, e.g. the React classes or otherwise exported references.
    `filter` - a filter function currently the module exports the following functions - see the exported functions for the commonly used filters

### ClassMetadataStore API

- `getClassMetadata(dataType, onload)`
    This will return a list of type information, from the [classes API](../blueocean-rest/README.md#classes_API), this method also handles caching results locally.

### Rendering extension points

The most common usage pattern is to use the exported `Renderer`, specifying the extension point name, any necessary contextual data, and optionally specifying a data type.

    import Extensions from '@jenkins-cd/js-extensions';
    ...
    <Extensions.Renderer extensionPoint="jenkins.navigation.top.menu" />

For example, rendering the test results for a build may be scoped to the specific type of test results in this manner:

    <Extensions.Renderer extensionPoint="test-results-view" filter={dataType(data)} testResults={data} />

The `ExtensionRenderer` component optionally uses the [classes API](../blueocean-rest/README.md#classes_API) to look up an appropriate, specific set of views for the data being displayed.
This should works seamlessly with other [capabilities](../blueocean-rest/README.md#capabilities).


### Defining extension point implementations

Extensions are defined in a `jenkins-js-extensions.yaml` file in the javascript source directory of a plugin by defining a list of extensions similar to this:

    # Extensions in this plugin
    extensions:
      - component: AboutNavLink
        extensionPoint: jenkins.topNavigation.menu
      - component: components/tests/AbstractTestResult
        extensionPoint: jenkins.test.result
        dataType: hudson.tasks.test.AbstractTestResultAction

Properties are:
- `component`: a module from which the default export will be used
- `extensionPoint`: the extension point name
- `dataType`: an optional Java data type this extension handles

For example, the `AboutNavLink` might be defined as a default export:

    export default class NavLink extends React.Component {
        ...
    }

#### Enforcing specific component types

In order to ensure a specific component is returned, an extension point may also use the `componentType` filter - it accepts an object prototype (e.g. an ES6 class), e.g.:

    import TestResults from './base-components/TestResults';
    ...
    <Extensions.Renderer extensionPoint="test-view" filter={componentType(TestResults)} ... />

Extensions are not limited to React components.
The `componentType` filter will attempt to match returned components by a series of prototype and typeof checks to appropriately filter returned types including ES6 classes.

### i18n resource pre-loading

By default, all `@jenkins-cd/js-extensions` generated JavaScript bundles will automatically preload the i18n resource bundles it finds in the
  `src/main/resources/jenkins/plugins/[pluginId]`, where `pluginId` is the Jenkins HPI plugin ID with all hyphen characters replaced by a path separator
   e.g. for `blueocean-dashboard`, the path that is searched is `src/main/resources/jenkins/plugins/blueocean/dashboard`.
   
> See `findI18nBundles()` in [@jenkins-cd/subs/extensions-bundle.js](@jenkins-cd/subs/extensions-bundle.js)

In some situations, a `@jenkins-cd/js-extensions` generated bundle may depend on i18n resources that are not in the default location or not in the host plugin (e.g. they may be defined in a "common" style utility plugin). In this situation,
  your plugin needs to know about these i18n resources in order to generate the right pre-loading code into the generated bundle. To tell `@jenkins-cd/js-extensions` about the resources in the other plugin, you need to manually define a `i18nBundles`
  list in the `jenkins-js-extensions.yaml` e.g.
    
```yaml
extensions:
  # etc ....

i18nBundles:
  - jenkins.plugins.aaa.Messages
  - hpiPluginId: acme-commons
    resource: jenkins.plugins.acme.commons.Messages
```

> Note how `i18nBundles` entries can define a string or an object, allowing the loading of bundles from plugins other than the default (i.e. the same plugin as the `@jenkins-cd/js-extensions` generated JavaScript bundle). 

# Blue Ocean commons

Common utilities used across modules. Lets try to keep this not a dumping ground ;)
# Blue Ocean Pipeline Editor

This repository houses the [Jenkins](https://jenkins.io/) plugin for creating and editing Pipeline jobs within the [Blue Ocean](https://jenkins.io/projects/blueocean/) user interface.

![Pipeline Editor Screenshot](doc/editor-ss.png)

:exclamation: **Important!** This software is a work-in-progress and is not complete.

## Running Locally

To start a new jenkins and run this plugin for development purposes:

```
# Start a local Jenkins
mvn hpi:run
```

And in another term,
```
# Watch and build the JS
npm run bundle:watch
```


## Running in another development Jenkins Instance

```
# Link this as a plugin into your Blue Ocean Jenkins' hpi:run server
mvn hpi:hpl -DjenkinsHome=<path-to-blueocean-home/blueocean/work>
```
> BlueOcean Config plugin

# BlueOcean configuration

BlueOcean configuration is injected as $blueOceanConfig JS object. It's in the following JSON format:

    {
       "version" : "1.0-alpha-7-SNAPSHOT (private-33ee8e40-vivek)",
       "jenkinsConfig" : {
          "version" : "2.2",
          "security" : {
             "authorizationStrategy" : {
                "allowAnonymousRead" : true
             },
             "enabled" : true
          }
       }
    }


# RollBar

* Enable RollBar

RollBar is disabled by default. Use BLUEOCEAN_ROLLBAR_ENABLED JVM property to enable.

```` 
mvn hpi:run -DBLUEOCEAN_ROLLBAR_ENABLED=true
```` 


## Usage ...

    try {
        foo();
        $blueocean_Rollbar.debug('foo() called');
    } catch (e) {
        $blueocean_Rollbar.error('Problem calling foo()', e);
    }
# Blue Ocean events
This plugin handles the publishing of events which are pushed to the browser 
via SSE. This allows the app to be nice and responsive to changes on the server side. 
# Acceptance tests for Blue Ocean

## System Requirements

### Operating Systems

Linux and macOS are currently the only supported OS. Windows support is not available at this time.

### Dependencies

`libxml2-utils` and `libssl-dev` are needed by the node packages.

Maven 3.3+ and JDK8 are required to run the tests.

## Acceptance Tests

Please make sure that BlueOcean plugins are built correctly. If _funky_ things seem to be happening in ATH, try running the following command from the top level blueocean directory

```bash
mvn clean install -DskipTests -DcleanNode
```

### Areas covered

* Karaoke parallel: ParallelNavigationTest. This checks that users can navigate between concurrently executing parallel branches, including steps waiting for input.
* Commit Messages: CommitMessagesTest checks to see that commit messages of git commits are shown on a run
* Folder Names: FoldersTest checks that folders with special characters work correctly in Blue Ocean
* Github integration: GithubCreationTests cover github integration testing of both the creation flow and also simple editor round tripping.

### Run all tests (in one command)
 ```bash
./run.sh
```

This is mainly for CI servers. It starts the selenium docker container and runs all
nightwatch and java ATH tests in one shot.

### Run tests against a local instance

ATH looks for a properties file at `~/.blueocean-ath-config` (or any combination of similar command line options).
These options will allow you to run a local [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/),
 for example, and execute the ATH against a local development instance
that you can debug/etc.. Currently these properties are supported and/or necessary:
```webDriverType=chrome
webDriverUrl=http://localhost:9515
webDriverBrowserSize=1024x768
jenkinsUrl=http://localhost:8080/jenkins
adminUsername=admin
adminPassword=admin
```

### Run tests in DEV mode

DEV mode starts Jenkins and the selenium docker container running in a standalone mode.
This allows for individual tests to be run against the server multiple times, which makes
writing ATH tests much easier.

First, start the server:
```bash
./run.sh --dev
```

Next run the desired tests

#### Java Webdriver Tests via Maven

Maven has 5 profiles set up for running tests. The default profile runs the offline tests.
The `live` profile runs tests that need services like GitHub, and the `all` profile will run all of them. Finally there
are the `nightwatch` and `offlineAll` profiles which run the nightwatch tests and run the nightwatch  + offline tests respectively.

Specific tests can be specified with `-Dtest=`.
```bash
mvn clean test
mvn clean test -Dprofile=live
mvn clean test -Dprofile=offlineAll
mvn clean test -Dprofile=all
mvn clean test -Dprofile=all -Dtest=FavoritesTest
```

Note: to run the live tests, there needs to be a `live.properties` file in the acceptance-tests directory.

```properties
github.repo=<name of repository to be created
github.org=<org or user name to create repo in.>
github.token=<personal access token (roles: repo, user:email, and optionally delete_repo)>
github.deleteRepo=<true/false should the code delete repo once test is done>
github.randomSuffix=<true/false - add a random suffix to repo name (ie must have for CI>
```

#### Java Webdriver Tests via IntelliJ (and probably other IDEs)

Running tests via the IDE works as expected as long as the standalone part of the ATH is running.

To start a test in IntelliJ the easiest way is to right click on the test class or method and click Run test.

NOTE: if you have a `~/.blueocean-ath-config` it will be used when running tests this way.

#### JavaScript [nightwatch] tests.

Nightwatch tests can be run via the nightwatch npm package (`npm install -g nightwatch`). It is
possible to specify specific test files, or whole directories which it will recursively find tests in.

```bash
nightwatch src/test/js/
nightwatch src/test/js/edgeCases/
nightwatch src/test/js/edgeCases/folder.js
```

When running in `--dev` mode, it can be useful to turn on client code log output. To do this, simply set
the `LOG_CONFIG` env variable e.g. to turn on SSE logging:

```bash
export LOG_CONFIG=sse
nightwatch src/test/js/
```

## Writing Tests

### Java Webdriver tests

#### IntelliJ

Make sure you add the acceptance-tests to your intellij blueocean project by right-clicking on `acceptance-tests/pom.xml`
and adding it to the project.

### WebDriverMixin

There is a `WebDriverMixin` that can help simplify writing tests significantly. It offers a number of
utility methods for the most common operations, all which have logic added to deal with common problems
in Blue Ocean such as animation.

It is recommended you use this when writing tests.

A simple example:

```java
import io.blueocean.ath.WebDriverMixin;

public class LoginTest implements WebDriverMixin {
    @Test
    public void login() {
        // go: goes to a relative jenkins path or absolute if starts with http(s)://
        go("/login");
        // find: waits for elements to be preset, if starts with / uses xpath, otherwise CSS selectors
        find("#j_username") // find by ID when starts with #, this is just a CSS selector
            // setText: clears, sets text on an input
            .setText("admin");
        find("input[name=j_password]") // just a CSS selector
            .setText("admin");
        // click: handles animation, failures will retry up to 2 times
        click("//form[@name='login']//button"); // XPath selector
        // other utilities, see io.blueocean.ath.WebDriverMixin
        assert find("//a[contains(@href, 'logout')]").isDisplayed() : "Not logged in";
    }
}
```

#### JUnit4 Tests

All test code uses Guice to do dependency injection.

```java
//Makes the browser login at the start of every test in this class.
@Login
// Sets up the Guice DI and creates the WebDriver istan
@RunWith(ATHJUnitRunner.class)
@UseModules(AthModule.class)
public class MyFirstATHTest{

    // Base url for the browser to navigate to. e.g driver.get(baseUrl + "/blue/")
    @Inject @BaseUrl
    String baseUrl;

    // Helper functions for webdriver
    @Inject
    WaitUtil wait;

    // Incase direct access to the driver instance is needed
    @Inject
    Webdriver driver;

    // Page objects are injectable too
    @Inject
    DashboardPage dashboardPage;

    // Creates a temporary git repository to use in this test
    @Rule
    @Inject
    GitRepositoryRule repository;

    @Test
    public void myFirstTest() {
        dashboardPage.open();

        // Waits for 10s for the url to contain the string pipelines.
        wait.until(ExpectedConditions.urlContains("pipelines"));

        wait.until(By.cssSelector("button.some.clazz"));
            .click();
    }
}
```
#### Server Side Events

`SSEClient` is a JUnit `ExternalResource`. Once it is injected and marked as a rule on the test
it connects to the Jenkins server want waits for job events. Events are saved into a list as they happen.

Once a test is ready to check for events, `untilEvent()` can be used. `clear()` can be invoked at any time to clear out any
messages received until that point in time.

```java
@Login
@RunWith(ATHJUnitRunner.class)
@UseModules(AthModule.class)
public class MySecondATHTest{

    @Rule
    @Inject
    SSEClientRule sseClient;

    @Test
    public void mySecondTest() {
       // ... do something that makes a build run.

       // This waits for any builds that have been queued to finish.
       sseClient.untilEvents(SSEEvents.activityComplete(pipelineName));
       // Clear all events so far so that when wait is called again it doesnt see the old events.
       sseClient.clear();

       // ... some more run stuff
       sseClient.untilEvents(SSEEvents.activityComplete(pipelineName));

       // .. finish off test
    }
}
```
#### Page Objects

Page Objects allow for selectors and actions to be grouped into reusable classes.

```java
@Singleton
public class MyAwesomePage {

    @Inject
    WaitUtil wait;
    // PageFactory.initElements drivers the @Findby annotations. TBD if we want to use these TBH
    @Inject
    public MyAwesomePage(WebDriver driver) {
        PageFactory.initElements(driver, this);
    }

    // Use annotation to find the WebElement instead of driver.findElement
    @FindBy(xpath = "//span[text()='Awesome']")
    public WebElement myAwesomeButton;

    public void clickAwesomeButton() {
        // Make sure the button is visible
        wait.until(ExpectedConditions.visibilityOf(myAwesomeButton));
        myAwesomeButton.click()

        // Check to see if another element is selected using the By selector.
        WebElement somethingElse = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("somethingElse")));
        somethingElse.isSelected();
    }
}
```

Any new Page Object classes need to be bound in `ATHModule#configure` to be able to be injected via Guice.

#### Pipeline Helper

These are a series of helpers to deal with pipelines. They started life to deal with pipelines being in folders. It offers a way
to give PageObjects more contextual information about what they are operating on without having to be explicit about it in every method call.

```java

@Login
@RunWith(ATHJUnitRunner.class)
@UseModules(AthModule.class)
public class MySecondATHTest{

    @Inject
    MultiBranchPipelineFactory mbpFactory;

    @Rule
    @Inject
    public GitRepositoryRule git;


    @Rule
    @Inject
    public SSEClientRule sseClient;

    @Test
    public void mySecondTest() {
        // Sets up the pipeline model with folders and a job name
        MultiBranchPipeline pipeline = mbpFactory.pipeline(Folder.folders("afolder", "bFolder"), "pipelineName");

        // Creates the pipeline in jenkins using the git repository rule.
        pipeline.createPipeline(git);

        // Wait for all runs to finish on the pipeline. Including all branches.
        sseClient.untilEvents(pipeline.buildsFinished);

        // Builds a bunch
        pipeline.buildBranch("master");

        // Opens the activity page for this pipeline and verifies its not 404.
        pipeline.getActivityPage().open();
        // Stops any runsa that are currently running on any branch job.
        pipeline.stopAllBuilds();

    }
}
```

###
[nightwatch]: http://nightwatchjs.org/
# BlueOcean Aggregator

Aggregates all BlueOcean modules. 

## To start it all up

To use this in development or to tyre kick: 

`mvn hpi:run`

(make sure you have run `mvn clean install` from the parent first)

Blue Ocean UI: 

    http://localhost:8080/jenkins/blue
    
Embedded Jenkins UI (so you can create some pipelines for fun):

    http://localhost:8080/jenkins
    
    
This links source from the other modules. So if you make a source change to rest, web or other modules,
it will be applied here. If its a UI module, you will need to have gulp installed (http://gulpjs.com/) and run `gulp bundle:watch` in the modules directory that has the JS you want to watch for changes and to have the reloaded live. 

# Running Blue Ocean in development

If you want to add to some extension points or mess with the GUI as it is right now, take a look at the `blueocean-dashboard` module (actually a plugin). Also take a look at: https://github.com/cloudbees/blueocean-sample-pipeline-result-ext-plugin for an example of an plugin that augments Blue Ocean.

Run in this directory: 

`mvn hpi:run`

    
## Verify it's working

    curl -v -X GET  http://localhost:8080/jenkins/blue/rest/organizations/jenkins/

Should print:

    {"name":"jenkins"}          
    
Why not also try: `curl http://localhost:8080/jenkins/blue/rest/organizations/jenkins/pipelines/`    

Load it in browser to see your ui code:

    http://localhost:8080/jenkins/blue
    
Load it in the browser to see the embedded Jenkins: 

    http://localhost:8080/jenkins
    
Look in blueocean-dashboard plugin for instructions on how to make changes to GUI code.    
    
    


    

    
# Dashboard plugin

This plugin provides the main Dashboard user interface for Blue Ocean.
It has a bunch of GUI components and extension points for other plugins to extend. 
This is where the fun happens. 

## Running and modifying this plugin

### With mvn

1. Go into `blueocean` and run `mvn hpi:run` in a terminal. (mvn clean install from the root of the project is always a good idea regularly!)
2. From this directory, run `npm run bundle:watch` to watch for JS changes and reload them.
3. Open browser to http://localhost:8080/jenkins/blue/ to see this
4. hack away. Refreshing the browser will pick up changes. If you add a new extension point or export a new extension you may need to restart the `mvn hpi:run` process. 

### With npm/storybook

We are supporting React Storybook https://voice.kadira.io/introducing-react-storybook-ec27f28de1e2#.8zsjledjp 

```javascript
npm run storybook
```

Then it’ll start a webserver on port 9001. Further on any change it will
refresh the page for you on the browser. The design is not the same as 
in blueocean yet but you can fully develop the components without a 
running jenkins,

#### Writing Stories

Basically, a story is a single view of a component. It's like a test case, but you can preview it (live) from the Storybook UI.

You can write your stories anywhere you want. But keeping them close to your components is a pretty good idea.

Let's write some stories:

```javascript
// src/main/js/components/stories/button.js

import React from 'react';
import { storiesOf, action } from '@kadira/storybook';

storiesOf('Button', module)
  .add('with a text', () => (
    <button onClick={action('clicked')}>My First Button</button>
  ))
  .add('with no text', () => (
    <button></button>
  ));
```

Here, we simply have two stories for the built-in `button` component. But, you can import any of your components and write stories for them instead.

#### Configurations for storybook

Now you need to tell Storybook where it should load the stories from. For that, you need to add the new story to the configuration file `.storybook/config.js`:


```javascript
// .storybook/config.js
import { configure } from '@kadira/storybook';

function loadStories() {
  require('../src/main/js/components/stories/index');
  require('../components/stories/button'); // add this line
}

configure(loadStories, module);
```

or to the `src/main/js/components/stories/index.js` (this is the preferred way):

```javascript
// src/main/js/components/stories/index.js
require('./pipelines');
require('./status');
require('./button'); // add this line
```

That's it. Now simply run “npm run storybook” and start developing your components.

# Running Tests

Tests are run via jest using the gulp-jest plugin. Three modes of execution are supported:

## `npm run test`

Runs jest and outputs JUnit test reports and code coverage metrics, in the 'reports' and 'coverage' dirs.
This is the "full" execution that is run in CI.

## `npm run test-fast`

Runs jest without test reports or coverage. Fastest run, useful for local development.

## `npm run test-debug`

Runs jest in debug mode listening on localhost:5858. You must attach a debugger for execution to proceed.
Test reports and coverage are skipped. 

## Running select test(s)

All of the above profiles support executing one or more tests via jest's `testPathPattern` parameter:

`npm run test:fast -- --test test/js/UrlUtils-spec.js # one test `

`npm run test:fast -- --test /capability/ # any tests in a 'capability' dir`

`npm run test:fast -- --test Url # any test with 'Url' in the name`


### Linting with npm

ESLint with React linting options have been enabled.

```
npm run lint
```

#### lint:fix

You can use the command lint:fix and it will try to fix all
offenses, however there maybe some more that you need to fix manually.

```
npm run lint:fix
```

#### lint:watch

You can use the command lint:watch and it will give rapid feedback 
(as soon you save, lint will run) while you try to fix all offenses.

```
gulp lint:watch --continueOnLint
```
# Blue Ocean Core JS

This is an npm module that contains common javascript libraries/utilities that are used across modules and plugins in Blue Ocean.
 
# For Developers

The blueocean-core-js is **not** automatically incorporated into full builds of the blueocean-plugin project.
It is published as its own npm module which is then referenced in other Blue Ocean plugins, notably:
- blueocean-web (note that since "web" is responsible for "bootstrapping" the Blue Ocean UI, the version specified in blueocean-web/package.json is the version provided to all other modules)
- blueocean-dashboard
- blueocean-personalization

## Developing with Prerelease Versions

To test changes in blueocean-core-js, perform the following steps:
- Tick the version number in package.json and npm-shrinkwrap.json and ensure a "prelease" version specified, e.g. 0.0.90-SNAPSHOT-1
- `npm run gulp`
- `npm publish --tag beta` (the "beta" tag is important)
   - If you receive an error about the package already existing, tick the version up again, e.g. 0.0.90-SNAPSHOT-2 and repeat above steps.
- Then update the modules that reference core-js:
   - With script: `bin/cleanInstall.js @jenkins-cd/blueocean-core-js@0.0.90-SNAPSHOT-1`
   - Or manually in blueocean-web, blueocean-dashboard, and blueocean-personalization
      - `npm install @jenkins-cd/blueocean-core-js@0.0.90-SNAPSHOT-1 -S -E`
- You should see all package.json and npm-shrinkwrap.json updated to reflect the new version number.
- Push changes to your branch and ensure that the blueocean-plugin and ATH builds both pass.

## Publishing a Production Version

Once the changes to blueocean-core-js are approved via PR, perform the following steps:
- Ensure your branch is 100% up to date with master. **This is critical**, otherwise recent changes may be lost and break the app.
   - If changes to core-js were made in the interim, ideally you should merge and publish a new pre-release version to ensure builds still pass.
- Tick version numbers in package.json and npm-shrinkwrap.json to a production version, e.g. "0.0.90"
- `npm run gulp`
- `npm publish`
- Commit the changes to package.json and npm-shrinkwrap.json
- Tick the version number in package.json and npm-shrinkwrap.json and ensure a "prelease" suffix specified, e.g. 0.0.91-SNAPSHOT
- Commit the changes to package.json and npm-shrinkwrap.json
- Then update the modules that reference core-js:
   - With script: `bin/cleanInstall.js @jenkins-cd/blueocean-core-js@0.0.90`
   - Or manually in blueocean-web, blueocean-dashboard, and blueocean-personalization
      - `npm install @jenkins-cd/blueocean-core-js@0.0.90 -S -E`
- You should see all package.json and npm-shrinkwrap.json updated to reflect the new version number.
- Push changes to your branch and ensure that the blueocean-plugin and ATH builds both pass.
- Merge your PR to master.

# Running Tests

Tests are run via jest using the gulp-jest plugin. Three modes of execution are supported:

## `npm run test`

Runs jest and outputs JUnit test reports and code coverage metrics, in the 'reports' and 'coverage' dirs.
This is the "full" execution that is run in CI.

## `npm run test-fast`

Runs jest without test reports or coverage. Fastest run, useful for local development.

## `npm run test-debug`

Runs jest in debug mode listening on localhost:5858. You must attach a debugger for execution to proceed.
Test reports and coverage are skipped. 

## Running select test(s)

All of the above profiles support executing one or more tests via jest's `testPathPattern` parameter:

`npm run test-fast -- --test test/js/UrlUtils-spec.js` // one test
`npm run test-fast -- --test /capability/` // any tests in a 'capability' dir
`npm run test-fast -- --test Url` // any test with 'Url' in the name
# Blue Ocean REST API implementation

Implementation of the Blue Ocean REST API, from the `blueocean-rest` module. See [its README.md ](https://github.com/jenkinsci/blueocean-plugin/tree/master/blueocean-rest) more information.
# Web middleware

This module mostly contains middleware for serving up "/blue" GUI.
In general, you shouldn't need to modify stuff in for plugins or features as it is infrastructure. Move along.

Look for blueocean.js for excitement.

## how this works with Javascript

All runtime JavaScript artifacts are generated during the build and added to the plugin HPI.

If you wish to make JavaScript changes during development and have them picked while using the HPI plugin (`mvn hpi:run`),
then you will need to run `npm run bundle` after each change. Alternative, you can run `npm run bundle:watch` to "watch"
for changes and automatically run `npm run bundle`. This applies to all Blue Ocean modules/plugins.
Placeholder directory for adding JDL assets to the web plugin. This directory contains material for building the demo Docker image

Only the Dockerfile is not here, so that building the image is easier from the repository root.

# Jenkins Design Language (JDL)

Reusable [React] components and design elements that adhere to the Jenkins Design Language (Blue Ocean edition).

## Developing
```
npm install
npm run gulp
npm run build-storybook
npm run site-server
```

> License is MIT. Other licenses in /licenses

__[Docs Site](http://jenkinsci.github.io/jenkins-design-language/docs)__# Blue Ocean Internationalization (i18n)

Internationalization API for Blue Ocean.

see as well [i18n documentation](../docu/I18N.md) and [js-extension documentation](../js-extensions/README.md)
# blueocean-github-pipeline

## Running the proxy

1. Install nginx `brew tap homebrew/nginx && brew install nginx-full --with-sub`
2. `cd blueocean-github-pipeline`
3. `./run_proxy.sh`

Github.com should be proxied at `http://localhost:9000/api/v3/`
