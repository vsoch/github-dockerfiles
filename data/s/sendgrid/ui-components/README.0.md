# UI-Comp BuildKite

✨ Welcome to the UI-Comp buildkite rundown ✨

This uses some of the cooler features of buildkite like dynamic pipelines and the block step with select input attributes. We also have a rad docker-compose configuration to allow git access inside of our docker containers as well as running puppeteer (a headless chrome browser) for image-snapshot testing (takes screenshots of the output and diffs them automagically as a part of our unit tests).

## Dynamic Pipeline

The purpose of our Dynamic pipeline is mainly to determine if we need to build or publish files to NPM. We do this by monitoring the git status command for the sentinel value `[Prepublish Built]`. After the step is determined we upload our desired pipeline through the buildkite-agent commands. We filter this command to only run on the master branch because that's the only time we'll need to publish.

```bash
# theDecider.sh

set -e
# Get where the script is currently running from, through bash magic
DIRNAME=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

if git log -1 --pretty=%B | cat | grep -e '\[Prepublish Built\]'; then
    echo "Publish Time"
    buildkite-agent pipeline upload $DIRNAME/publishPipeline.yml
else
    echo "Need to build"
    buildkite-agent pipeline upload $DIRNAME/buildPipeline.yml
fi
```

## Crazy Docker-Compose

Our crazy docker-compose file. We use the default variable syntax provided by the docker-compose grammar with the ${ENVVAR:-defaultvalue} syntax to achieve flexibility and out-of-the-box ease of use. This makes it incredibly easy to override values for our ci work and provide default values for developers.

For our build process we need access to git and NodeJS. Docker makes it convenient to get the correct NodeJS dependencies but challenging to access the hosts ssh information to work with git as well as the correct access to work with those credentials.

Fortunately we did the hard work for you. In the precommand we export the userid which is what the filesystem stores on the files across mounted volumes. We assume that userid if the variable is present in the dockerfile and then we mount the user directories into the docker container so it has access to the user's information like the ssh keys, known_hosts, and other goodies.

```bash
# pre-command
export MYUID=$(id -u)
```

```Dockerfile
version: '3.3'

services:
  app:
    image: ${IMAGETAG:-docker.sendgrid.net/sendgrid/ui-components:latest}
    user: ${MYUID:-0}
    build:
     context: .
    volumes:
      # Bootstrap the buildkite users into the docker container for permissions
      - /etc/group:/etc/group:ro
      - /etc/passwd:/etc/passwd:ro
      # Add the buildkite-agent user info in for .ssh keys and known_hosts for git
      # [WARNING] This will break if they change the buildkite-agent user configuration
      - /var/lib/buildkite-agent:/var/lib/buildkite-agent
      # === Use this to run locally and get as close as we can to the build agent =====
      # ~/:[localUserPathHere]
      # Mount the working directory so docker and the host can communicate for
      # git magic (need that .git folder)
      - ./:/opt/sendgrid/ui-components/
      # Preserve the node_modules folder in the docker container because we mounted ./
      - /opt/sendgrid/ui-components/node_modules
```

## Block Step for SemVer Tagging and Publishing

This step will ask you what version you'll release and add it to the buildkite-agent meta-data collection retrievable through the command `$(buildkite-agent meta-data get "key-name")`

```yml
# publishPipeline.yml
- block: ":exploding_death_star: Request Publish :exploding_death_star:"
   fields:
     - select: "Release Type"
       key: "publish-version"
       options:
         - label: "patch"
           value: "patch"
         - label: "minor"
           value: "minor"
         - label: "major"
           value: "major"
```

We use it in the following command to publish with lerna (A node/js package management tool). It looks at the version we pass through and any of the files that were edited since the last commit to detect and generate packages with the correct version information as well as allowing us in the near future to release all of our components individually and version them automagically as well.

`lerna publish --yes --cd-version $(buildkite-agent meta-data get "publish-version")"`

### Some Niceties We Found On The Way

If you want to skip a version you can add [skip ci] to the commit comment and it will be skipped entirely (We use this on the commit when we publish because it doesn't need to be consumed by buildkite)

Artifacts are awesome. We upload our image-snapshot diffs to the buildkite artifacts so we can give anyone access to the diff'd images. You can see some of the diffs here https://buildkite.com/sendgrid/ui-components/builds/679#c4f5a481-ba71-449b-8308-9a60b76ddfb8

Managing log output can be surprisingly useful `echo "--- 🐳 Pulling the docker image"` Will collapse the following log output until it finds another section `echo "+++ 📸 Running Image Snapshots"` will create a section that is already open. This can help a lot in the usability of the build output by categorizing steps that are run most builds and keeping the important parts of your log output as visible as possible. https://buildkite.com/docs/builds/managing-log-output

https://github.com/buildkite/emojis
# Buildkite Hooks
We have pre-populated your hooks directory with example hooks. For information on what you can do with hooks, please check out buildkite's documentation: https://buildkite.com/docs/agent/hooks

Once you have what you want in your hook, you will need to remove the .sample from the file name.