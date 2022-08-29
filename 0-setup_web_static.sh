#!/usr/bin/env bash
# Bash script that sets up your web servers for the deploymen: (1) Install Nginx if it not already installed; (2) Create the folder /data/web_static/shared/ if it doesn’t already exist (2) Create the folder /data/web_static/releases/test/ if it doesn’t already exist; (4) Create a HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration); (5) Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran. (6) Give ownership of the /data/ folder to the ubuntu user AND group (you can assume this user and group exist). This should be recursive; everything inside should be created/owned by this user/group. (7) Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static). Restart Nginx after updating the configuration

apt-get -y update
apt-get -y install nginx
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "simple content" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sed -i "/listen 80 default_server/a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default
sed -i "/listen 80 default_server/a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enaabled/default
service nginx restart
