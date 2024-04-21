import os
import sys
import cmd
import subprocess
import logging
import argparse
import os.path
import pathlib
import time 
import json

from time import sleep
from pathlib import Path
from cmd import Cmd
from os.path import join, isdir, isfile, exists
from subprocess import Popen, PIPE
from json import load, dump





curr_dir = os.getcwd()
cfg_path = curr_dir + '.cfgs'





with open(curr_dir + "\\.cfgs" + "\\config.json", 'r') as f:
    cfg = json.load(f)  # load the json file
    f.close()


print("Current Directory: " + curr_dir)
print("Config-File: " + cfg_path)
print("HUB-Docker-User: " + cfg["user"])
print("HUB-Docker-Password: " + cfg["pass"])

print("RootFS-Builder-Directory: " + cfg["parent_dir"])
print("RootFS-Arch-Directory: " + cfg["arch"])
print("RootFS-Arch2-Directory: " + cfg["arch2"])
print("RootFS-Ubuntu-Directory: " + cfg["ubuntu"])


distro = "arch"


class Main(cmd.Cmd):

    prompt = 'WSL-ROOTFS-BUILDER> '

    doc_header = ""
    undoc_header = ""


    def do_export(self, line):
        print('Running export-command!')
        os.system("docker ps")
        x = input("Enter the container-id: ")
        n = input("Enter the name of the container: ")
        os.system("docker export " + x + " > /mnt/c/Users/black/" + n + ".tar")

        

    def do_ps(self, line):
        print('Running ps-command!')
        os.system("docker ps")

    def do_dist(self, line):
        print("Current Build-target: " +  distro)
        distro == line
        print(distro)
        print(line)
 



    def do_set(self, line):
        print('Setting environment variable: %s' % line)
        os.environ[line] = '1'

    def do_unset(self, line):
        print('Unsetting environment variable: %s' % line)
        del os.environ[line]

    def do_save(self, line):
        print('Saving environment variables to file: %s' % line)
        os.chdir(cfg_path)
        with open(line, 'w') as f:
            for key, value in os.environ.items():
                f.write(f'{key}={value}\n')


    def do_load(self, line):
        print('Loading environment variables from file: %s' % line)
        os.chdir(cfg_path)
        with open(line, 'r') as f:
            for line in f:
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

    def do_help(self, line):
        print('Available commands:')
        print('  help')
        print('  run')
        print('  ls = list images')
        print('  rmi')
        print('  rm')
        print('  ps')
        print('  build')
        print('  cbuild')
        print("  tag")
        print("  push")
        print("  pull")
        print('  set')
        print('  unset')
        print('  save')
        print('  load')
        print('  clear')
        print('  exit')
        
    def do_exit(self, line):
        print('Exiting!')
        sys.exit(0)


    def do_ls(self, line):
        print('Running list-command!')
        os.system("docker images")

    def do_rmi(self, line):
        print('Running rmi-command!')
        os.system("docker images")
        print("Choose the image you want to remove!")
        image_name = input("Enter the image name: ")
        release = input("Enter the release-version: ")
        os.system("docker rmi blackleakzde/" + image_name + ":" + release + "  -f")


    def do_rm(self, line):
        print('Running rmi-command!')
        os.system("docker container ls -a")
        print("Choose the image you want to remove!")
        container_name = input("Enter the Containername: ")
        os.system("docker rm blackleakzde/" + container_name + "  -f")

    def do_push(self, line):
        print('Running push-command!')
        image_name = input("Enter the image name: ")
        release = input("Enter the release-version: ")
        os.system("docker tag blackleakzde/" + image_name + ":" + release + " blackleakzde/" + image_name + ":" + release)
        os.system("docker push blackleakzde/" + image_name + ":" + release)

    def do_pull(self, line):
        print('Running pull-command!')
        image_name = input("Enter the image name: ")
        release = input("Enter the release-version: ")
        print("Pulling image: " + image_name + ":" + release)
        os.system("docker pull " + image_name + ":" + release)


    def do_run(self, line):
        print('Running build-command: %s' % line)
        os.system(line)




    def do_build(self, line):
        print('Running build-command: %s' % line)
        print("Attention! > Pls make sure you have a Dockerfile in the current directory")
        print("Current Directory: " + os.getcwd())
        file_exists = os.path.exists('Dockerfile')
        if file_exists:
            print("Dockerfile exists!")
        else:
            print("Dockerfile does not exist! plz. move dir!°")
            print("Usuall Dockerfile-Dir: " + cfg["parent_dir"] + " " + cfg["arch"] + " " + cfg["arch2"] + " " + cfg["ubuntu"])
            dir = input("Enter the dockerfile_dir: ")
            os.chdir(dir)
            print("Current Directory: " + os.getcwd())
            os.system("ls -la")
            file_exists = os.path.exists('Dockerfile')

            if file_exists:
                print("Dockerfile exists!")
                print("Start building!")
                image_name = input("Enter the image name: ")
                release = input("Enter the release-version: ")
                os.system("docker build -t blackleakzde/" + image_name + ":" + release + " .")
                os.system("docker build -t blackleakzde/" + image_name + ":" + release + " .")
            

        #dockerfile_dir = input("Enter the dockerfile_dir: ")
        #os.chdir(dockerfile_dir)
        

    def do_cbuild(self, line):
        print('Running build-command: %s' % line)
        print("Attention! > Pls make sure you have a Dockerfile in the current directory")
        file_exists = os.path.exists('docker-compose.yml')
        if file_exists:
            print("Compose receip exists!")
        else:
            print("Compose receip does not exist! plz. move dir!°")
            print("Usuall Dockerfile-Dir: " + cfg["parent_dir"] + " " + cfg["arch"] + " " + cfg["arch2"] + " " + cfg["ubuntu"])
            dir = input("Enter the dockerfile_dir: ")
            os.chdir(dir)

        
    

        image_name = input("Enter the image name: ")
        release = input("Enter the release-version: ")
        os.system("docker compose up -d")



def loop():
    try:
        Main().cmdloop()
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    loop()