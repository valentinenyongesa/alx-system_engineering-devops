#!/usr/bin/env bash

sudo apt-get update
sudo apt-get install -y nginx

custom_hostname=$(hostname)

cat <<EOL | sudo tee /etc/nginx/sites-available/default
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        # Your existing configuration here

        # Add the custom HTTP header
        add_header X-Served-By $custom_hostname;
    }
}
EOL

sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

sudo service nginx restart
