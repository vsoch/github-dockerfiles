SIR Docker images
===================

This repository contains Dockerfiles related to SIR project.

- **Backend**: https://github.com/unicef/sir-poc/
- **Frontend**: https://github.com/unicef/sir-poc-fe/
 

### Trigger build:
    
To manually trigger a build you need:

   - $CIRCLE_API_TOKEN: Token to use CircleCI API. Get it at https://circleci.com/gh/unicef/sir-releases/edit#api
   - $MODULE: Must be `frontend` or `backend`
   - $TAG: Tag name of related module. It must be a tagged released availble in the related github repository:
      - https://github.com/unicef/sir-poc/releases for backend 
      - https://github.com/unicef/sir-poc-fe/releases for frontend
    
    curl --user $CIRCLE_API_TOKEN: \
        -q \
        --request POST \
        --form build_parameters[TAG]=$TAG \
        --form build_parameters[CIRCLE_JOB]=$MODULE \
        --form config=@$PWD.circleci/config.yml \
        --form notify=false \
            https://circleci.com/api/v1.1/project/github/unicef/sir-releases/tree/develop


### Docker HUB repositories:

After build, images will be availabkle at:

- **Backend**: https://hub.docker.com/r/unicef/sir-be/
- **Frontend**: https://hub.docker.com/r/unicef/sir-fe/

