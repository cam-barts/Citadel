# -*- coding: utf-8 -*-
from colorama import init
from colorama import Fore
import webbrowser
import time
import citadel

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
            # SnapChat
            elif toolSelect == "4":
                print(Fore.YELLOW + " SnapChat tools")
                print()
                print(Fore.CYAN + " [1]" + Fore.WHITE + " SnapStory - Scrape media from public SnapChat stories")
                print(Fore.CYAN + " [<]" + Fore.WHITE + " Main Menu")
                print()
                def snapSelect():
                    time.sleep(0.5)
                    snapSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
                    print()
                    if snapSelect == "1":
                        webbrowser.open("https://github.com/sdushantha/SnapStory")
                    elif snapSelect == "<":
                        socialMenu()
                snapSelect()

            # Reddit
            elif toolSelect == "5":
                    print(Fore.YELLOW + " Reddit tools")
                    print()
                    print(Fore.CYAN + " [1]" + Fore.WHITE + " Universal Reddit Scraper - Scrape Reddit posts using Reddit API")
                    print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
                    print()
                    def redditSelect():
                        time.sleep(0.5)
                        redditSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
                        print()
                        if redditSelect == "1":
                            webbrowser.open("https://github.com/JosephLai241/Universal-Reddit-Scraper")
                        elif redditSelect == "<":
                            socialMenu()
                    redditSelect()

            # LinkedIn
            elif toolSelect == "6":
                print(Fore.YELLOW + " LinkedIn tools")
                print()
                print(Fore.CYAN + " [1]" + Fore.WHITE + " LinkedIn2Username - generate username lists from companies on LinkedIn")
                print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
                print()
                def linkedinSelect():
                    linkedinSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
                    print()
                    if linkedinSelect == "1":
                        webbrowser.open("https://github.com/initstring/linkedin2username")
                    elif linkedinSelect == "<":
                        socialMenu()
                linkedinSelect()

            # YouTube
            elif toolSelect == "7":
                print(Fore.YELLOW + " YouTube tools")
                print()
                print(Fore.CYAN + " [1]" + Fore.WHITE + " YouTube DL - download YouTube videos from terminal ")
                print(Fore.CYAN + " [<]" + Fore.WHITE + " Main menu")
                print()
                def youtubeSelect():
                    youtubeSelect = input(Fore.YELLOW + " Select: " + Fore.WHITE)
                    print()
                    if youtubeSelect == "1":
                        webbrowser.open("https://github.com/ytdl-org/youtube-dl")
                    elif youtubeSelect == "<":
                        socialMenu()
                youtubeSelect()
            elif toolSelect == "<":
                citadel.menu()
            social()
    social()
