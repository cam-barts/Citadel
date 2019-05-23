# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
import menu

# Dark web tools
def dark():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    if toolSelect == "1":
        webbrowser.open("https://github.com/DedSecInside/TorBot")
    if toolSelect == "<":
        citadel.menu()
    dark()
