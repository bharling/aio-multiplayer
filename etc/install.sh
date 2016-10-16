#!/bin/bash
cd ~
sudo apt-get update
sudo apt-get install build-essential tcl8.5
wget http://download.redis.io/releases/redis-stable.tar.gz
tar xf redis-stable.tar.gz
tar xzf redis-stable.tar.gz
cd ~/redis-stable/
make
sudo make install
sudo ~/redis-stable/utils/install_server.sh
sudo update-rc.d redis_6379 defaults

sudo add-apt-repository -y ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python3.5
sudo apt-get install python-setuptools
sudo easy_install pip
sudo pip install virtualenv virtualenvwrapper
sudo apt-get install python3.5-dev