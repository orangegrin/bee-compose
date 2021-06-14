./npc uninstall
./npc install -server=nps.gpu360.com:8024 -vkey=niceday
npc start
touch /etc/rc.local
echo '#!/bin/bash' > /etc/rc.local
echo 'ifconfig' >> /etc/rc.local
echo `pwd`'/startup.sh' >> /etc/rc.local
chmod a+x /etc/rc.local
chmod a+x -R ./
./build-compose.sh 10 #default 10 node

#install docker
apt-get update
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null


apt-get update
apt-get install docker-ce docker-ce-cli containerd.io docker-compose -y


systemctl enable rc-local 
systemctl start rc-local.service
