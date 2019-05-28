# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu

# Paste tools
def paste():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    print()
    if toolSelect == "1":
        webbrowser.open("https://github.com/rndinfosecguy/Scavenger")
    elif toolSelect == "2":
        webbrowser.open("https://github.com/itsmehacker/CardPwn")
    elif toolSelect == "<":
        menu.menu()
    paste()
