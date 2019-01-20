#Play Docker Demo

This is a very simple demo to show how you can run a Docker container that runs
a [simple](https://github.com/rolandtritsch/scala-play-hello) Scala Play App.

* Install docker -- http://www.docker.io/ and make the hello world demo work
* From the cloned docker repo/dir run `vagrant halt` to shutdown the docker env
* Clone this repository
* Go back to the docker repo/dir and edit the `VagrantFile` and add a shared folder to point to the play-docker-dome you just cloned. You also need to forward the ports from vagrant to your host OS ...
`
Vagrant::Config.run do |config|
  # Setup virtual machine box. This VM configuration code is always executed.
  config.vm.box = BOX_NAME
  config.vm.box_url = BOX_URI

  config.ssh.forward_agent = true

  # Provision docker and new kernel if deployment was not done.
  # It is assumed Vagrant can successfully launch the provider instance.
  if Dir.glob("#{File.dirname(__FILE__)}/.vagrant/machines/default/*/id").empty?

  # ...

  end

  # add the following lines ...
  config.vm.share_folder "play-docker-demo", "/play-docker-demo", "<on-your-box>/play-docker-demo", :create=>true
  config.vm.forward_port 9902, 9903
end
`
* In the example we are making the port forwarding explicit ...
    * Are starting the play app in docker on port 9901 and forward that port to 9902
    * In vagrant we forward port 9902 to port 9903, means at the end you should be able to access the app on port 9903
* We have tested this with VirtualBox on a Mac and we also had to beef up the size of the VM ...
`
config.vm.provider :virtualbox do |vb|
  config.vm.box = BOX_NAME
  config.vm.box_url = BOX_URI
  vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  # add the following line ...
  vb.customize ["modifyvm", :id, "--memory", 8192]
end
`
* Get the play app up and running ...
`vagrant up`
`vagrant ssh`
`cd /play-docker-demo`
`sudo docker build -t=base base`
`sudo docker build -t=play-hello play-hello`
`sudo docker build -t=play-hello-run play-hello-run`
`sudo docker run -p 0.0.0.0:9902:9901 play-hello-run`
* Load the URL below into your browser ...
`http://localhost:9903`