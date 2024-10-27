FROM php:7.4-apache

RUN apt-get update 

COPY ./challenge/* /var/www/html/


RUN echo "shellmates{tYPE_jugGlINg_byp4ss_Php_l0GgIng} " > /flag.txt && \
    chown www-data:www-data /flag.txt && \
    chmod 600 /flag.txt


RUN echo "DirectoryIndex jugjug.html" >> /etc/apache2/apache2.conf

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf


RUN chmod -R 755 /var/www/html


WORKDIR /var/www/html
