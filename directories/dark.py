# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu

# Dark web tools
def dark():
    time.sleep(0.5)
    toolSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
    if toolSelect == "1":
        webbrowser.open("https://github.com/DedSecInside/TorBot")
    elif toolSelect == "2":
        webbrowser.open("https://github.com/k4m4/onioff")
    elif toolSelect == "<":
        menu.menu()
    dark()
