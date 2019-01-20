# logyard apps

apps using logyard, directly (zmq) or as a drain.

To build go components on the VM:

HOST:

    $ cd .../logyard-apps
    $ rsync -avzL ./ stackato@$VMNAME.local:/s/code/logyard_apps/ --exclude=.git*

NODE:

    sudo apt-get install -y bzr
    export GOROOT=/usr/local/go
    export PATH=$PATH:$GOROOT/bin
    workdir=$HOME/stackato/code/logyard_build
    export GOPATH=$workdir
    workdir2=$workdir/src/github.com/ActiveState/
    git clone http://github.com/ActiveState/logyard-apps/ $workdir2/logyard-apps/

    git clone http://github.com/ActiveState/logyard $workdir/src/logyard
    git clone http://github.com/ActiveState/confdis $workdir/src/confdis


    go get -tags zmq_3_x github.com/ActiveState/logyard-apps/applog_endpoint

    cd $workdir2/logyard-apps/applog-endpoint
    go install -tags zmq_3_x ./...

    ls $workdir/bin # should see applog_endpoint

# To update:

    kato stop process applog_endpoint
    cp $workdir/bin/applog_endpoint $HOME/stackato/go/bin/applog_endpoint
    kato start process applog_endpoint
