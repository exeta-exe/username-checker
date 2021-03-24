import os
import requests
from colorama import Fore
import easygui



def username():
    file = open("usernames.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace("\n", "")
    
def banner():
    os.system('cls')
    print(f"""{Fore.RED}
  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
 ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
 ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
 ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
 ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
  [*] GITHUB: exeta-exe
  [*] DISCORD: ~/usr/nobaz#8473
    """)

banner()
print(" how many names do you want to check?...")
b = input(" >>> ")
os.system('cls')
banner()
print(" LINK EXAMPLE: https://github.com/")
link = input(" >>> ")

openfile = easygui.fileopenbox()
if openfile == None:
    print(Fore.RED + 'FATAL ERROR: File is missing')
    exit()
file = open(openfile, 'r')
count = 0
while True:
    line = file.readline()
    count += 1
    if count == b:
        print(Fore.GREEN + 'DONE!')
        break
    if not line:
        break
    line = line.replace("\n", "")
    r = requests.get(link + line)
    if r.status_code == 200:
        print(Fore.RED + "[TAKEN] {}".format(line))
    elif r.status_code == 404:
        print(Fore.GREEN + "[AVAILABLE] {}".format(line))
    else:
        print(Fore.WHITE + "[UNUSABLE] {}".format(line))

