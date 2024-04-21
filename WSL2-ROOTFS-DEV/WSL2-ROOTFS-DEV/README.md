# WSL-ROOTFS BUILD ENV


# Distributions:

- Arch Linux (x2)
- Ubuntu



# Parent-folder: 
#                "C:\Users\black\Development_Prorotype\WSL-Blackzspace.de\WSL-ROOTFS-DEV"


# WSL2- Ubuntu 

# Directory: "WSL-ROOTFS-UBUNTU"



# Simple Build-Script:


Bash:

```sh

export HOST_UID=$(id -u)
export HOST_GID=$(id -g)

read -p "img > " img
read -p "release > " release

docker build --build-arg UID=$HOST_UID --build-arg GID=$HOST_GID -t $img:$release .

```