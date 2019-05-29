# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
from . import menu

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
        menu.menu()
    people()

#test
