import os
import sys
import subprocess
import os.path


import cmd


from cmd import Cmd

curr = os.getcwd()

wsl_distrolauncher = curr + "WSL-DistroLauncher-DEV"

class Main(cmd.Cmd):


    prompt = 'WSL2-DistroLauncher-Builder > '



    def do_run(self, arg):
        print("RUN")
        os.system('python3 ./build.py')



    def do_build(self, arg):
        print("BUILD")
        target = input("Enter Targetfolder: ")
       
        os.system('cd ' + wsl_distrolauncher)
        os.system('./build.bat')

    def do_clone(self, arg):
        print("CLONEING SOURCE_REPO!!!")
        if os.path.exists('WSL-DistroLauncher'):
            print("Directory Exists")
            name = "WSL-DistroLauncher-New"
        else:
            name = "WSL-DistroLauncher"


        os.system('git clone https://github.com/Microsoft/WSL-DistroLauncher.git ' + name)



def loop():
    try:
        Main().cmdloop()    
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':  
    loop()