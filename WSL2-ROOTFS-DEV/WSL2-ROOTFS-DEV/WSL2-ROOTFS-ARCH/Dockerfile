# syntax=docker/dockerfile:experimental 

FROM archlinux:latest

RUN pacman -Syyuu --noconfirm
RUN pacman -Sy archlinux-keyring --noconfirm
RUN pacman -Sy base-devel base dhcpcd nano sudo --noconfirm
RUN pacman -Sy make cmake gcc go git curl wget gzip --noconfirm


RUN useradd -ms /bin/bash vault


WORKDIR /home/vault/app



RUN gpasswd -a vault wheel

RUN echo 'wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers


COPY --chown=vault:vault . /home/vault/app
RUN chmod -R 755 /home/vault/app


RUN pacman -Sy make cmake gcc go git --noconfirm