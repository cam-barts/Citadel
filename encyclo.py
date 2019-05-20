# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time

init(autoreset=True)

def menu():
    print()
    print("""███████╗███╗   ██╗ ██████╗██╗   ██╗ ██████╗██╗      ██████╗ ██████╗ ██╗   ██╗
██╔════╝████╗  ██║██╔════╝╚██╗ ██╔╝██╔════╝██║     ██╔═══██╗██╔══██╗╚██╗ ██╔╝
█████╗  ██╔██╗ ██║██║      ╚████╔╝ ██║     ██║     ██║   ██║██████╔╝ ╚████╔╝ 
██╔══╝  ██║╚██╗██║██║       ╚██╔╝  ██║     ██║     ██║   ██║██╔═══╝   ╚██╔╝  
███████╗██║ ╚████║╚██████╗   ██║   ╚██████╗███████╗╚██████╔╝██║        ██║   
╚══════╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝    ╚═════╝╚══════╝ ╚═════╝ ╚═╝        ╚═╝   """)
    print("An encyclopedia of OSINT tools")
    print()
    print(Fore.CYAN + "[1]" + Fore.WHITE + " Recon tools")
    print(Fore.CYAN + "[2]" + Fore.WHITE + " People search tools")
    print(Fore.CYAN + "[3]" + Fore.WHITE + " Social media tools")
    print(Fore.CYAN + "[4]" + Fore.WHITE + " Paste site tools")
    print(Fore.CYAN + "[5]" + Fore.WHITE + " Dark web tools")
    print()
    print(Fore.YELLOW + "Ctrl + C to exit")
    print()
    directory = input("Select a directory: ")
    print()
    if directory == "1":
        print("Recon tools - all in one OSINT tools that serve multiple functions")
        print()
        print("[1]" + " Photon - an incredibly fast crawler designed for OSINT")
        print("[2]" + " GasMask - an all in one OSINT gathering tool")
        print("[3]" + " Kamerka - build an interactive map of cameras from Shodan")
        print("[4]" + " FinalRecon - an OSINT tool for all in one web reconnaissance")
        print("[5]" + " SpiderFoot - automate OSINT from hundreds of sources")
        print("[<]" + " Main menu")
        print()
        def recon():
            time.sleep(1)
            toolSelect = input("Select: ")
            if toolSelect == "1":
                webbrowser.open('https://github.com/s0md3v/Photon') # Go to Photon GitHub page
            elif toolSelect == "2":
                webbrowser.open('https://github.com/twelvesec/gasmask') # Go to GasMask GitHub page
            elif toolSelect == "3":
                webbrowser.open('https://github.com/woj-ciech/kamerka') # Go to Kamerka GitHub page
            elif toolSelect == "4":
                webbrowser.open('https://github.com/thewhiteh4t/FinalRecon') # Go to FinalRecon GitHub page
            elif toolSelect == "5":
                webbrowser.open('https://spiderfoot.net') # Go to SpiderFoot homepage
            elif toolSelect == "<":
                menu()
            elif toolSelect == "x":
                exit()
            recon()
        recon()
    if directory == "2":
        print("People search tools - extract OSINT from multiple databases")
        print()
        print("[1]" + " Skiptracer - scrape PII paywall sites on a ramen noodle budget")
        print("[2]" + " LittleBrother - information gathering tool for EU persons")
        print("[<]" + " Main menu")
        print()
        def people():
            time.sleep(1)
            toolSelect = input("Select: ")
            if toolSelect == "1":
                webbrowser.open('https://github.com/xillwillx/skiptracer') # Go to SkipTracer GitHub page
            elif toolSelect == "2":
                webbrowser.open('https://github.com/lulz3xploit/LittleBrother') # Go to LittleBrother GitHub page
            elif toolSelect == "<":
                menu()
            people()
        people()
    if directory == "3":
        def socialMenu():
            print("Social media tools - collect OSINT from various social media platforms")
            print()
            print("[1]" + " Facebook")
            print("[2]" + " Twitter")
            print("[3]" + " Instagram")
            print("[4]" + " SnapChat")
            print("[5]" + " Reddit")
            print("[6]" + " LinkedIn")
            print("[7]" + " YouTube")
            print("[<]" + " Main menu")
            print()
        socialMenu()
        def social():
            time.sleep(1)
            toolSelect = input("Select: ")
            if toolSelect == "1":
                print("Facebook tools")
                print()
                print("[1]" + " Entropy - Facebook OSINT Collection and Analysis Tool")
                print("[<]" + " Main menu")
                print()
                facebookSelect = input("Select: ")
                if facebookSelect == "1":
                    webbrowser.open("https://github.com/andrew-vii/Entro.py")
                elif facebookSelect == "<":
                    socialMenu()
            elif toolSelect == "2":
                print()
                print("Twitter tools")
            elif toolSelect == "3":
                print()
                print("Instagram tools")
            elif toolSelect == "4":
                print()
                print("SnapChat tools")
            elif toolSelect == "5":
                print()
                print("Reddit tools")
            elif toolSelect == "6":
                print()
                print("LinkedIn tools")
            elif toolSelect == "7":
                print()
                print("YouTube tools")
            elif toolSelect == "<":
                menu()
            social()
        social()
    if directory == "4":
        print("Paste site tools - collect OSINT from multiple paste sites")
        print()
        print("[1]" + " Scavenger - a crawler bot for credential leaks")
        print("[<]" + " Main menu")
        print()
        def paste():
            time.sleep(1)
            toolSelect = input("Select: ")
            if toolSelect == "1":
                webbrowser.open("https://github.com/rndinfosecguy/Scavenger")
            if toolSelect == "<":
                menu()
            paste()
        paste()
    if directory == "5":
        print("Dark web tools - collect OSINT from dark web sources")
        print()
        print("[1]" + " TorBot - dark web OSINT tool")
        print("[<]" + " Main menu")
        print()
        def dark():
            time.sleep(1)
            toolSelect = input("Select: ")
            if toolSelect == "1":
                webbrowser.open("https://github.com/DedSecInside/TorBot")
            if toolSelect == "<":
                menu()
            dark()
        dark()
menu()
