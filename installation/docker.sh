#! /bin/bash

user=$(whoami)

curl https://get.docker.com | sudo bash
sudo usermod -aG docker $user
sudo systemctl docker start
sudo systemctl docker enable

sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

echo "Please restart your terminal"