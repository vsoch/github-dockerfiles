A Jenkins plugin which implements reusable pipeline flows for Jenkins X

## Using in declarative pipelines

```groovy
pipeline {
  agent {
    kubernetes {
      label "jx-maven"
    }
  }
  stages {
    stage('Maven Release') {
      steps {
        mavenFlow {
        }
      }
    }
  }
}
```

## Using in scripted pipelines

```groovy
node {
  stage('Maven Release') {
    mavenFlow {
    }
  }
}
```