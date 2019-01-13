[![Build Status](https://travis-ci.org/makoto-nagai/docker-pyspark-pytest.svg?branch=master)](https://travis-ci.org/makoto-nagai/docker-pyspark-pytest)

## Overviews
* [makoto-nagai/docker-pyspark: Docker image of Apache Spark with its Python interface, pyspark.](https://github.com/makoto-nagai/docker-pyspark)
    * Base docker image
* pytest
    * 3.1.2
* pytest-cov
    * latest
* pytest-mock
    * 1.6.2
* pytest-pep8
    * latest
* pytest-faker
    * 2.0.0

To run `pytest`, you need to replace `repository_name` with your name of repository (more specifically directory name).

```
docker run -it --volume $(pwd):/tmp/repository_name --workdir /tmp/repository_name makotonagai/pyspark-pytest pytest
```

or by using short option

```
docker run -it -v $(pwd):/tmp/repository_name -w /tmp/repository_name makotonagai/pyspark-pytest pytest
```

For instance, run the examples,

```
docker run -it --volume $(pwd)/example:/tmp/example --workdir /tmp/example makotonagai/pyspark-pytest pytest
```


## Notes
If you change the version of pytest, you need to add git-tag to the commit.
For instance, if the version of pytest is `3.1.2`, you need to execute the following commands.

```
git tag -a pytest-3.1.2
git push origin pytest-3.1.2
```

Then you can push your commits to the remote repository.

