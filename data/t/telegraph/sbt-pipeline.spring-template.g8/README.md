
# SBT Pipeline Playframework.g8 

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![Build Status](https://jenkins-prod.api-platforms.telegraph.co.uk/job/Pipeline/job/sbt-pipeline-playframework.g8%20Pipeline/badge/icon)](https://jenkins-prod.api-platforms.telegraph.co.uk/job/Pipeline/job/sbt-pipeline-playframework.g8%20Pipeline/)

This project contains an SBT Template that contains the Pipeline template for all projects.
The main objectives of this template are:
 * Standardize projects
 * Speed up the development keeping developers away from tedious configuration
 * Configure the tools needed for the Pipeline

## How to Use
There are the steps needed to use this template:
 * Add an SSH Key to your git account
 * Install SBT - *brew install sbt*
 * Create a new project - *sbt new git@github.com:telegraph/sbt-pipeline.spring-template.g8*

## Dependencies
The project's pipeline needs the following variables to be defined on Jenkins:
 * **GITHUB_TOKEN** - Contains the GitHub Access Token
 * **JENKINS_GITHUB_CREDENTIALS_ID** - Jenkins Access to GitHub account
 * **AWS_ECR_DOCKER_ACCOUNT** - AWS ECR Docker Account
 * **AWS_ECR_DOCKER_REGISTRY** - AWS ECR Docker Registry to be used

## Issues
Unfortunately there are some issues related with jgit project. This project is a git client and at the moment ssh connections  to git, only some specific key names are being lock at ([JGit Issue](https://github.com/eclipse/jgit/blob/master/org.eclipse.jgit/src/org/eclipse/jgit/transport/JschConfigSessionFactory.java#L323)).
Therefore, in order to use our private Git Repository we need a workaround. Since JGit checks for a file called *identity*, one way of solving this issue is to copy your git public key to identity (ex: *cp ~/.ssh/git-hub_rsa.pub ~/.ssh/identity*).  

