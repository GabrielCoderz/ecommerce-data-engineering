# startup-script.sh
#! /bin/bash

# Install Htop (monitoring hardware tool)
sudo apt install htop -y

## Install Git
sudo apt update
sudo apt install -y git

# Install Docker
sudo apt install apt-transport-https lsb-release ca-certificates curl gnupg -y
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io
sudo usermod -aG docker ${USER}

sudo systemctl enable docker

# Copy git repository and Up mage_ai
git clone https://github.com/GabrielCoderz/ecommerce-data-engineering.git /home/${USER}/ecommerce-data-engineering
cd /home/${USER}/ecommerce-data-engineering

sudo docker-compose up -d mage_ai
