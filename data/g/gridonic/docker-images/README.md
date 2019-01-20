# Docker Images

https://hub.docker.com/r/gridonic/docker/

[![](https://images.microbadger.com/badges/version/gridonic/docker:php72.svg)](https://microbadger.com/images/gridonic/docker:php72 "Get your own version badge on microbadger.com") [![](https://images.microbadger.com/badges/image/gridonic/docker:php72.svg)](https://microbadger.com/images/gridonic/docker:php72 "Get your own image badge on microbadger.com")

[![](https://images.microbadger.com/badges/version/gridonic/docker:php71.svg)](https://microbadger.com/images/gridonic/docker:php71 "Get your own version badge on microbadger.com") [![](https://images.microbadger.com/badges/image/gridonic/docker:php71.svg)](https://microbadger.com/images/gridonic/docker:php71 "Get your own image badge on microbadger.com")

[![](https://images.microbadger.com/badges/version/gridonic/docker:php70.svg)](https://microbadger.com/images/gridonic/docker:php70 "Get your own version badge on microbadger.com") [![](https://images.microbadger.com/badges/image/gridonic/docker:php70.svg)](https://microbadger.com/images/gridonic/docker:php70 "Get your own image badge on microbadger.com")

[![](https://images.microbadger.com/badges/version/gridonic/docker:php56.svg)](https://microbadger.com/images/gridonic/docker:php56 "Get your own version badge on microbadger.com") [![](https://images.microbadger.com/badges/image/gridonic/docker:php56.svg)](https://microbadger.com/images/gridonic/docker:php56 "Get your own image badge on microbadger.com")

A set of custom docker images for CI.

# Test locally

As an example, in order to build the `php70` image, run

    $ docker build -t gridonic/php70 php70
    
Then, you might want to start a basic shell in your container

    $ docker run -it gridonic/php70 /bin/bash
