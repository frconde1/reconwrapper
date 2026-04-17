from colorama import Fore, Style, init
import re 
init(autoreset=True)
import os 
import subprocess
import sys
import textwrap

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
domregex = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'

BANNER = textwrap.indent(f"""
{Fore.RED}

                        _
                       | \
                       | |
                       | |
  |\                   | |
 /, ~\                / /
X     `-.....-------./ /
 ~-. ~  ~              |
    \             /    |
     \  /_     ___\   /
     | /\ ~~~~~   \ |
     | | \        || |
     | |\ \       || )
    (_/ (_/      ((_/



{Fore.CYAN}        Reconnaissance Automation Tool
{Fore.RED}        Herramienta de Automatización de Reconocimiento

{Style.RESET_ALL}
    """, "\t")



def info(msg):    print(f"{Fore.CYAN}[*] {msg}")
def ok(msg):      print(f"{Fore.GREEN}[+] {msg}")
def error(msg):   print(f"{Fore.RED}[-] {msg}")
def warning(msg): print(f"{Fore.YELLOW}[!] {msg}")
def presentacion(): print(BANNER) 


def check(ip):

    return re.search(regex,ip) is not None

def checkDom(dominio):
    return re.search(domregex, dominio) is not None

def clear_screen():
    # For Windows (os.name is 'nt')
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        _ = os.system('clear')


