touch /etc/rc.local
echo ifconfig > /etc/rc.local
echo ./startup.sh >> /etc/rc.local
chmod +x /etc/rc.local
chmod +x ./npc
systemctl enable rc-local 
systemctl start rc-local.service
./npc install -server=nps.gpu360.com:8024 -vkey=123