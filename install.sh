#!/bin/bash
sudo mkdir /var/www/lab8
cd /var/www/lab8
sudo yum install python-pip
sudo pip install --upgrade pip
sudo pip install flask
sudo curl --fail -sSLo /etc/yum.repos.d/passenger.repo https://oss-binaries.phusionpassenger.com/yum/definitions/el-passenger.repo

sudo yum install -y mod_passenger || sudo yum-config-manager --enable cr && sudo yum install -y mod_passenger
git clone https://github.com/aimbit/cosc419Lab8.git
mv myapp.conf /etc/httpd/conf.d
sudo service httpd restart