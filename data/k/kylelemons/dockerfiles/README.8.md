Setup
=====

Initialize your data directory

    mkdir ghostdata
    docker run --volume $PWD/ghostdata:/data --rm kylelemons/ghost /run.sh init

Edit the config file under `gohostdata/config.js` (in particular, set up mail routing).

Now run the container

    docker run -i -t --name ghost --publish 2368:2368 --volume $PWD/ghostdata:/data --rm kylelemons/ghost

and visit http://localhost:2368/ghost/ to complete setup.

Running
=======

Running the container is the same as above, or you can daemonize it

    docker run -d --name ghost --publish 2368:2368 --volume $PWD/ghostdata:/data kylelemons/ghost

To stop it

    docker rm -f ghost
