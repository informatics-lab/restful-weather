# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 5000, host: 5000 

   config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get update
     sudo apt-get install -y python-dev python-pip
     sudo pip install flask
   SHELL
end
