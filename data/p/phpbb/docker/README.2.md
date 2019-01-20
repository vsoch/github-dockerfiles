PHP - build
===========

Image to prepare the code for the tests (composer, build directories...)

Composer:
```
docker run \
    --volume $(pwd):/data \
    --volume ~/.composer:/composer \
    --workdir /data \
    --rm \
    -ti \
    phpbb/build sh -c 'cd phpBB; COMPOSER_HOME=/composer php ../composer.phar install --dev'
```

Phing prepare:
```
docker run \
    --volume $(pwd):/data \
    --workdir /data \
    --rm \
    -ti \
    phpbb/build sh -c 'cd build; ../phpBB/vendor/bin/phing clean prepare'
```
