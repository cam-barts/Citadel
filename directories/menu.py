# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
import recon
from people import *
from social import *
from paste import *
from dark import *


init(autoreset=True)

def menu():
    print()
    print("""  ██████╗██╗████████╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║
 ██║     ██║   ██║   ███████║██║  ██║█████╗  ██║
 ██║     ██║   ██║   ██╔══██║██║  ██║██╔══╝  ██║
 ╚██████╗██║   ██║   ██║  ██║██████╔╝███████╗███████╗
  ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝    """)
    print(" A library of OSINT tools")
    print()
    print(Fore.CYAN + " [1]" + Fore.WHITE + " Recon tools")
    print(Fore.CYAN + " [2]" + Fore.WHITE + " People search tools")
    print(Fore.CYAN + " [3]" + Fore.WHITE + " Social media tools")
    print(Fore.CYAN + " [4]" + Fore.WHITE + " Paste site tools")
    print(Fore.CYAN + " [5]" + Fore.WHITE + " Dark web tools")
    print()
    print(Fore.RED + " [x]" + Fore.WHITE + " Exit")
    print()
    directory = input(" Select a directory: ")
    print()
    if directory == "1":
        print(Fore.YELLOW + " Recon tools" + Fore.WHITE + " - all in one OSINT tools that serve multiple functions")
        print()
        print(Fore.CYAN + " [1]" + Fore.WHITE + " Photon - an incredibly fast crawler designed for OSINT")
        print(Fore.CYAN + " [2]" + Fore.WHITE + " GasMask - an all in one OSINT gathering tool")
        print(Fore.CYAN + " [3]" + Fore.WHITE + " Kamerka - build an interactive map of cameras from Shodan")
        print(Fore.CYAN + " [4]" + Fore.WHITE + " FinalRecon - an OSINT tool for all in one web reconnaissance")
        print(Fore.CYAN + " [5]" + Fore.WHITE + " SpiderFoot - automate OSINT from hundreds of sources")
        print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
        print()
        recon()

    elif directory == "2":
        print(Fore.YELLOW + " People search tools" + Fore.WHITE + " - extract OSINT from multiple databases")
        print()
        print(Fore.CYAN + " [1]" + Fore.WHITE + " Skiptracer - scrape PII paywall sites on a ramen noodle budget")
        print(Fore.CYAN + " [2]" + Fore.WHITE + " LittleBrother - information gathering tool for EU persons")
        print(Fore.CYAN + " [3]" + Fore.WHITE + " SocialScan - check email addresses across all social platforms")
        print(Fore.CYAN + " [4]" + Fore.WHITE + " Sherlock - search username availability across all social platforms")
        print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
        print()
        people()

    elif directory == "3":
        socialMenu()
        social()

    elif directory == "4":
        print(" Paste site tools - collect OSINT from multiple paste sites")
        print()
        print(Fore.CYAN + " [1]" + Fore.WHITE + " Scavenger - a crawler bot for credential leaks")
        print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
        print()
        paste()

    elif directory == "5":
        print(" Dark web tools - collect OSINT from dark web sources")
        print()
        print(Fore.CYAN + " [1]" + Fore.WHITE + " TorBot - dark web OSINT tool")
        print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
        print()
        dark()

    elif directory == "x":
        exit()
menu()
