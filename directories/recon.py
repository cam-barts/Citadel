# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu

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
    elif toolSelect == "6":
        webbrowser.open('https://github.com/netevert/pockint') # Go to SpiderFoot homepage
    elif toolSelect == "<":
        menu.menu()
    recon()
