#!/bin/bash
# This script sets up the web server for the deployment of web_static.

# Check if Nginx is installed. If not, install it.
if ! command -v nginx &> /dev/null; then
	    apt-get update
	        apt-get install -y nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate the symbolic link to 'current'
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of /data/ to ubuntu user and group recursively
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ at /hbnb_static
# The configuration file for nginx on Ubuntu 20.04 is located at /etc/nginx/sites-available/default
sed -i '/server_name _;/a \    location /hbnb_static/ {\n        alias /data/web_static/current/;\n    }\n' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
service nginx restart

# Exit with success status
exit 0

