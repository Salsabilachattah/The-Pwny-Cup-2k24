FROM php:7.4-apache

RUN apt-get update 

RUN groupadd -g 1000 appuser && \
    useradd -u 1000 -g appuser -m appuser

RUN chown -R appuser:appuser /var/www/html


COPY ./challenge/* /var/www/html/

COPY flag.txt /
RUN FLAG_NAME=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 12)  && cp /flag.txt "/flag_${FLAG_NAME}_.txt" && rm /flag.txt


WORKDIR /var/www/html

USER appuser
