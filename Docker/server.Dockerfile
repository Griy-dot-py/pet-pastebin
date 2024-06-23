FROM nginx:1.26.0-perl

COPY public /var/www/public
COPY config/nginx.conf /etc/nginx/nginx.conf
