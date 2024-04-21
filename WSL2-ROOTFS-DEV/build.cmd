title WSL-ROOTFS Docker Builder
color 0b
@echo off
@echo Building WSL-ROOTFS Docker Image!..

set /p CONTAINER_NAME="Enter Container Name: "
set /p CONTAINER_TAG="Enter Container Tag: "
set /p CONTAINER_VERSION="Enter Container Version: "
set /p DOCKER_USER="Enter Docker-Username: "
set /p IMAGE_NAME="Enter Image Name: "



export HOST_UID=$(id -u)
export HOST_GID=$(id -g)


docker build --build-arg UID=$HOST_UID --build-arg GID=$HOST_GID -t %IMAGE_NAME% .