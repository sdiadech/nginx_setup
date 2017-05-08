#sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
#sudo /etc/init.d/nginx restart

mkdir -p /home/box/web/etc/
mkdir -p /home/box/web/uploads/
mkdir -p /home/box/web/public/css/
mkdir -p /home/box/web/public/img/
mkdir -p /home/box/web/public/js/

# Configure NGINX
sudo rm -rf /etc/nginx/nginx.conf
sudo rm -rf /etc/nginx/sites-enabled/default
cp nginx.conf /home/box/web/etc
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf

# Run NGINX
sudo /etc/init.d/nginx restart