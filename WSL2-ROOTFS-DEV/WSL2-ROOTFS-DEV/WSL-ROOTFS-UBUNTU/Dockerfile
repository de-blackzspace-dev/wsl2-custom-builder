FROM ubuntu
ARG UID
ARG GID

# Update the package list, install sudo, create a non-root user, and grant password-less sudo permissions
RUN apt update && \
    apt install -y sudo && \
    addgroup --gid $GID debian && \
    adduser --uid $UID --gid $GID --disabled-password --gecos "" debian && \
    echo 'sudo ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers \
    gpasswd -a debian sudo

# Set the non-root user as the default user
USER debian

WORKDIR /home/debian/app
# Copy files into the container and set the appropriate permissions
COPY --chown=debian:sudo . /home/debian/app
RUN chmod -R 755 /home/debian/app