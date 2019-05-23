# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
import citadel

# Paste tools
def paste():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: ")
    print()
    if toolSelect == "1":
        webbrowser.open("https://github.com/rndinfosecguy/Scavenger")
    if toolSelect == "<":
        citadel.menu()
    paste()
