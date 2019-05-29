from utils import WebNavMenu, SuperMenu, banner, announce
from tools import * # Import the dictionaries of tools


def main():
    """Main function of the Citadel program

    It generates WebNavMenus based on the dictionaries in the "tools.py" file, and then generates a SuperMenu for all of the WebNavMenus
    Class definitions can be found in the "utils.py" file
    """
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

    # Create the main menu from the sub menus
    main_menu = SuperMenu(
        "Main Menu",
        sub_menus=[recon_menu, people_menu, social_menu, paste_menu, dark_menu],
    )
    main_menu.show_menu()


if __name__ == "__main__":
    banner() # Display the banner
    announce("New tools available in the Citadel: POCKINT, InstaLoader, CardPwn, Onioff")
    main()
