# meedan/fdupes

`FROM ubuntu 12.04` which includes an `fdupes` which allows hardlinking with `-L`

#### EXAMPLE

```
docker run -i -t --rm -v /home/${USER}/dir/to/fdupes:/home/${USER}/dir/to/fdupes meedan/fdupes
```
