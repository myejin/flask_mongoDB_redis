#!/bin/bash
curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
sudo echo "deb http://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org redis-server python3 python3-pip 
sudo systemctl start mongod
sudo systemctl enable mongod
sudo pip3 install redis flask Flask-WTF Flask-Session Flask-PyMongo pytest
sudo service redis-server restart