pipeline

- build docker
- push to repository (ecr/jfrog)

deploy version

- create new task definition
- create/update service definition

or deploy latest

- stop task (asg 1:1:1) - asg will restart with latest
