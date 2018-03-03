FROM ubuntu:xenial-20180112.1

COPY ./install_dockbox_prereqs.sh /tmp/install_dockbox_prereqs.sh
RUN apt-get update && \
    apt-get -y install sudo && \
    yes "Y" | /tmp/install_dockbox_prereqs.sh

ARG USER_NAME
ARG USER_ID
ARG USER_GID

RUN useradd -ms /bin/bash $USER_NAME && echo "$USER_NAME:$USER_NAME" | chpasswd && adduser $USER_NAME sudo
RUN usermod -u $USER_ID $USER_NAME
RUN groupmod -g $USER_GID $USER_NAME

USER $USER_NAME
