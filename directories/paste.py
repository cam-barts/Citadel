# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu
import subprocess

init(autoreset=True)

# Paste tools
def paste():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    print()
    if toolSelect == "1":
        print(Fore.RED + " Scavenger - a crawler bot for credential leaks")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu"
        ]
        print(*options,sep='\n')
        print()
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/rndinfosecguy/Scavenger')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading Scavenger")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/rndinfosecguy/Scavenger.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "2":
        print(Fore.RED + " CardPwn - OSINT Tool to find breached credit card information")
        print()
        options = [
        Fore.CYAN + " [1]" + Fore.WHITE + " View the tool",
        Fore.CYAN + " [2]" + Fore.WHITE + " Download the tool",
        Fore.CYAN + " [<]" + Fore.WHITE + " Main menu",
        ]
        print(*options,sep='\n')
        print()
        view_or_download = input(Fore.YELLOW + " Select: " + Fore.WHITE)
        print()
        if view_or_download == "1":
            webbrowser.open('https://github.com/itsmehacker/CardPwn')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE +  "Downloading CardPwn")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/itsmehacker/CardPwn.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "<":
        menu.menu()
    paste()
