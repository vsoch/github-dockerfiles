# testnodejs

[![](https://images.microbadger.com/badges/image/superbuddy/testnodejs.svg)](https://microbadger.com/images/superbuddy/testnodejs "Get your own image badge on microbadger.com")

This container runs node.js test.

+ The dependencies are installed in the Dockerfile.
+ Tests are .sh scripts (example included).
+ Everything should [exit](http://www.tldp.org/LDP/abs/html/exitcodes.html) with `0` when all succeed.
+ The default tests are included in the docker.
+ The repository specific tests are in the `test` directory inside the repo.

## Launching the docker
```
docker run -it --rm -v repo_dir_on_host:/repo superbuddy/testnodejs
```
