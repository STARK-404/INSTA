
# ---------------- Imports
import os
import shutil

try:
    import pyzipper
    import colorama
    from rich import print
    from rich.panel import Panel
    import re
except ImportError:
    _ = os.system('pip install colorama' if os.name == 'nt' else 'pip3 install colorama')
    _ = os.system('pip install pyzipper' if os.name == 'nt' else 'pip3 install pyzipper')
    _ = os.system('pip install rich' if os.name == 'nt' else 'pip3 install rich')
    _ = os.system('pip install instaloader' if os.name == 'nt' else 'pip3 install instaloader')
import pyzipper
import sys
from time import sleep
from getpass import getpass
from colorama import Fore
from rich.panel import Panel
from rich import print
import os
os.system("git pull")

# -------------------Colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r

# ------------------banners
logo = Panel('''
[bold red]•[bold green]•[bold white]•
[bold green].d8888. d88888b d888888b db    db d8888b. 
[bold green]88'  YP 88'     `~~88~~' 88    88 88  `8D 
[bold green]`8bo.   88ooooo    88    88    88 88oodD' 
[bold green]  `Y8b. 88~~~~~    88    88    88 88~~~   
[bold green]db   8D 88.        88    88b  d88 88      
[bold green]`8888Y' Y88888P    YP    ~Y8888P' 88      
                                         ''' +'\n[bold red] <[bold white]/[bold red]> [bold green]STARK[bold green] [bold red] <[bold white]/[bold red]>')


def banner():
    print(logo)

def cls_clear_func():
    os.system('cls' if os.name=='nt' else 'clear')

def exixting_directory_file(file):
    if os.path.exists(file):
        os.remove(file)

def designprint(samaywrite):
    print(logo)
    print("[bold red]"+"└─> "+'[bold white]'+"[bold green]"+samaywrite)

def front_design():
    cls_clear_func()
    banner()

front_design()


class Setup:
    def __init__(self,user):
        self.data = user
    def mainFile(self):
        self.save = self.data
        try:
            with pyzipper.AESZipFile('Stark.zip', 'r', compression=pyzipper.ZIP_DEFLATED,
                                     encryption=pyzipper.WZ_AES) as extracted_zip:
                extracted_zip.extractall(pwd=str.encode(self.save))
            designprint('Password Correct !')
            sleep(2.3)
            front_design()
            designprint('Successfully Decrypted and unzipped file with password..')
            sleep(3.0)
            exixting_directory_file('Sincryption.zip')
            os.system('python main.py' if os.name=='nt' else 'python3 main.py')
        except Exception as samay:
            designprint('Password Incorrect !')
            print("[•]Contact Admin For Password!")
            print("[!] You Have Been Redirected To Adin Suoport!!")
            os.system("xdg-open https://instagram.com/mr_lalu_1232/")
            os.system('python Run.py' if os.name=='nt' else 'python3 Run.py')


try:
    user_ezip_unzipping = getpass(r+"└─"+w+"\033[1;37mEnter the password of Zipfile : "+r).strip()
except:
    pass

if __name__ == '__main__':
    exixting_directory_file('main.py')
    main_start = Setup(user_ezip_unzipping)
    main_start.mainFile()





