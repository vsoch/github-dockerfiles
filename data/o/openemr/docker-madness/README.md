# docker-madness

## Current Goals of Repo:
1. create docker container that provides high level of OS and Web Server security for OpenEMR
2. make this docker container the default people download and the default they deploy on GCP. Merge parts of scripts / snippets into Asher's existing work on AWS
3. take lessons learned from this repo and add to documentation of OpenEMR to benefit knowledge base 
4. integrate OpenEMR tightly with GCP to make deployment extremely easy. Add Kubernetes possibly.
5. generate things that can be used by the wider OS community and not just OpenEMR

## Current Directory Structure (very likely will change):
`config-files/`
  - things like `apache2.conf`, `openemr.conf`, etc will go here.

`docker-images/`
  - `00_whole-docker/` - only for testing, everything in one dockerfile, 
  - `01_separate-dockers/` - multiple Dockerfiles that each build their own image
 
`helper-scripts/`
  - any needed shell scripts 
  
## Current Work Happening:
1. Check out the Docker Image - 1.0 project: https://github.com/openemr/docker-madness/projects/1
2. Also check out the Docker Image - 2.0 project:https://github.com/openemr/docker-madness/projects/2

##  Timeline:
  - Finish both projects listed above by March 15th, 2019
