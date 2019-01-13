# kubernit

Currently still in working progress.

## Building with virtualbox

Build the iso's by running:

```
make all
```

Build a new vm in virtualbox with type `Linux` and version `Linux 2.6 / 3.x / 4.x (64 bit)`. Extend the memory size to about `8192MB` and add a `8GB` disk. Before running attach the iso and add the hostonly network we created at the start and a `network nat` on the the second adapter.

Run though each kubernit node `master0`, `worker0`, `worker1` and `storage0`. Now you can start each VM starting with `master0`.
