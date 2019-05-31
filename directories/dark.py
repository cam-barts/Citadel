# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu
import subprocess

# Dark web tools
def dark():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    print()
    if toolSelect == "1":
        print(Fore.RED + " TorBot - a dark web OSINT tool")
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
            webbrowser.open('https://github.com/DedSecInside/TorBot')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE + "Downloading TorBot")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/DedSecInside/TorBot.git'])
        elif view_or_download == "<":
            menu.menu()
    elif toolSelect == "2":
        print(Fore.RED + " Onioff - an onion url inspector for inspecting deep web links")
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
            webbrowser.open('https://github.com/k4m4/onioff')
        elif view_or_download == "2":
            print(Fore.CYAN + " [+] " + Fore.WHITE +  "Downloading Onioff")
            time.sleep(0.5)
            print()
            subprocess.call(['git', 'clone', 'https://github.com/k4m4/onioff.git'])
        elif view_or_download == "<":
            menu.menu()
    # elif toolSelect == "2":
    #     webbrowser.open("https://github.com/k4m4/onioff")
    elif toolSelect == "<":
        menu.menu()
    dark()
