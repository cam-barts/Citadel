# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time

init(autoreset=True)

def menu():
    print()
    print(""" ███████╗███╗   ██╗ ██████╗██╗   ██╗ ██████╗██╗      ██████╗ ██████╗ ██╗   ██╗
 ██╔════╝████╗  ██║██╔════╝╚██╗ ██╔╝██╔════╝██║     ██╔═══██╗██╔══██╗╚██╗ ██╔╝
 █████╗  ██╔██╗ ██║██║      ╚████╔╝ ██║     ██║     ██║   ██║██████╔╝ ╚████╔╝ 
 ██╔══╝  ██║╚██╗██║██║       ╚██╔╝  ██║     ██║     ██║   ██║██╔═══╝   ╚██╔╝  
 ███████╗██║ ╚████║╚██████╗   ██║   ╚██████╗███████╗╚██████╔╝██║        ██║   
 ╚══════╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝    ╚═════╝╚══════╝ ╚═════╝ ╚═╝        ╚═╝   """)
    print(" An encyclopedia of OSINT tools")
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
        
        # Recon Tools
        def recon():
            time.sleep(0.5)
            toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
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
            recon()
        recon()
    if directory == "2":
        print(Fore.YELLOW + " People search tools" + Fore.WHITE + " - extract OSINT from multiple databases")
        print()
        print(Fore.CYAN + " [1]" + Fore.WHITE + " Skiptracer - scrape PII paywall sites on a ramen noodle budget")
        print(Fore.CYAN + " [2]" + Fore.WHITE + " LittleBrother - information gathering tool for EU persons")
        print(Fore.CYAN + " [3]" + Fore.WHITE + " SocialScan - check email addresses across all social platforms")
        print(Fore.CYAN + " [4]" + Fore.WHITE + " Sherlock - search username availability across all social platforms")
        print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
        print()
        
        # People tools
        def people():
            time.sleep(0.5)
            toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
            if toolSelect == "1":
                webbrowser.open('https://github.com/xillwillx/skiptracer') # Go to SkipTracer GitHub page
            elif toolSelect == "2":
                webbrowser.open('https://github.com/lulz3xploit/LittleBrother') # Go to LittleBrother GitHub page
            elif toolSelect == "3":
                webbrowser.open('https://github.com/iojw/socialscan') # Go to SocialScan GitHub page
            elif toolSelect == "4":
                webbrowser.open('https://github.com/sherlock-project/sherlock') # Go to Sherlock Github page
            elif toolSelect == "<":
                menu()
            people()
        people()
    if directory == "3":
        
        # Social tools
        def socialMenu():
            print(Fore.YELLOW + " Social media tools" + Fore.WHITE + " - collect OSINT from various social media platforms")
            print()
            print(Fore.CYAN + " [1]" + Fore.WHITE + " Facebook")
            print(Fore.CYAN + " [2]" + Fore.WHITE + " Twitter")
            print(Fore.CYAN + " [3]" + Fore.WHITE + " Instagram")
            print(Fore.CYAN + " [4]" + Fore.WHITE + " SnapChat")
            print(Fore.CYAN + " [5]" + Fore.WHITE + " Reddit")
            print(Fore.CYAN + " [6]" + Fore.WHITE + " LinkedIn")
            print(Fore.CYAN + " [7]" + Fore.WHITE + " YouTube")
            print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
            print()
        socialMenu()
        def social():
            time.sleep(0.5)
            toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
            print()
            
            # Facebook
            if toolSelect == "1":
                print(Fore.YELLOW + " Facebook tools")
                print()
                print(Fore.CYAN + " [1]" + Fore.WHITE + " Entropy - Facebook OSINT Collection and Analysis Tool")
                print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
                print()
                def facebookSelect():
                    time.sleep(0.5)
                    facebookSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
                    print()
                    if facebookSelect == "1":
                        webbrowser.open("https://github.com/andrew-vii/Entro.py")
                    elif facebookSelect == "<":
                        socialMenu()
                facebookSelect()
                
            # Twitter
            elif toolSelect == "2":
                print(Fore.YELLOW + " Twitter tools")
                print()
                print(Fore.CYAN + " [1]" + Fore.WHITE + " Twint - an advanced Twitter scraper")
                print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
                print()
                def twitterSelect():
                    time.sleep(0.5)
                    twitterSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
                    print()
                    if twitterSelect == "1":
                        webbrowser.open("https://github.com/twintproject/twint")
                    elif twitterSelect == "<":
                        socialMenu()
                twitterSelect()
                
            # Instagram
            elif toolSelect == "3":
                print(Fore.YELLOW + " Instagram tools")
                print()
                print(Fore.CYAN + " [1]" + Fore.WHITE + " InstaLooter - Instagram scraper for photos and videos (no-API)")
                print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
                print()
                def instagramSelect():
                    time.sleep(0.5)
                    instagramSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
                    print()
                    if instagramSelect == "1":
                        webbrowser.open("https://github.com/althonos/InstaLooter")
                    elif instagramSelect == "<":
                        socialMenu()
                instagramSelect()
            elif toolSelect == "4":
                print(" SnapChat tools")
            elif toolSelect == "5":
                print(" Reddit tools")
            elif toolSelect == "6":
                print(" LinkedIn tools")
            elif toolSelect == "7":
                print(" YouTube tools")
            elif toolSelect == "<":
                menu()
            social()
        social()
    if directory == "4":
        print(" Paste site tools - collect OSINT from multiple paste sites")
        print()
        print(Fore.CYAN + " [1]" + Fore.WHITE + " Scavenger - a crawler bot for credential leaks")
        print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
        print()
        
        # Paste tools
        def paste():
            time.sleep(0.5)
            toolSelect = input(Fore.YELLOW + " Select: ")
            print()
            if toolSelect == "1":
                webbrowser.open("https://github.com/rndinfosecguy/Scavenger")
            if toolSelect == "<":
                menu()
            paste()
        paste()
    if directory == "5":
        print(" Dark web tools - collect OSINT from dark web sources")
        print()
        print(Fore.CYAN + " [1]" + Fore.WHITE + " TorBot - dark web OSINT tool")
        print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
        print()
        
        # Dark web tools
        def dark():
            time.sleep(0.5)
            toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
            if toolSelect == "1":
                webbrowser.open("https://github.com/DedSecInside/TorBot")
            if toolSelect == "<":
                menu()
            dark()
        dark()
    if directory == "x":
        exit()
menu()
