FROM php:8-fpm-alpine3.14
ARG GOODUSER
ARG UID
ARG MAIL
ARG NOM

RUN echo "$GOODUSER($UID):$GROUP($GID)"

# installation bash
RUN apk --no-cache update && apk --no-cache add bash git npm

# installation de composer
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
&& php composer-setup.php --install-dir=/usr/local/bin \
&& php -r "unlink('composer-setup.php');"

# installation de symfony
RUN wget https://get.symfony.com/cli/installer -O - | bash \
&& mv /root/.symfony/bin/symfony /usr/local/bin/symfony

# Gestion user
# RUN addgroup -g $GID -S $GROUP
RUN adduser -h /home/$GOODUSER -D -s /bin/bash -u $UID $GOODUSER
USER $GOODUSER

# config git (a revoir)
RUN git config --global user.email $MAIL \
&& git config --global user.name $NOM


WORKDIR /var/www/html
