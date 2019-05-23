from utils import WebNavMenu, SuperMenu, banner
from tools import *


def main():
    recon_menu = WebNavMenu(
        "Recon Menu",
        "- all in one OSINT tools that serve multiple functions",
        recon_tools,
    )
    people_menu = WebNavMenu(
        "People search tools", " - extract OSINT from multiple databases", people_tools
    )
    social_menu = WebNavMenu(
        "Social media tools",
        " - collect OSINT from various social media platforms",
        social_tools,
    )
    paste_menu = WebNavMenu(
        "Paste site tools", "  - collect OSINT from multiple paste sites", paste_tools
    )
    dark_menu = WebNavMenu(
        "Dark web tools", " - collect OSINT from dark web sources", dark_tools
    )
    main_menu = SuperMenu(
        "Main Menu",
        sub_menus=[recon_menu, people_menu, social_menu, paste_menu, dark_menu],
    )
    main_menu.show_menu()


if __name__ == "__main__":
    banner()
    main()
