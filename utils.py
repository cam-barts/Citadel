from colorama import Fore, init
import webbrowser

init(autoreset=True)


def banner():
    banner = """
  ██████╗██╗████████╗ █████╗ ██████╗ ███████╗██╗
 ██╔════╝██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║
 ██║     ██║   ██║   ███████║██║  ██║█████╗  ██║
 ██║     ██║   ██║   ██╔══██║██║  ██║██╔══╝  ██║
 ╚██████╗██║   ██║   ██║  ██║██████╔╝███████╗███████╗
  ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
  """
    print(banner)


def menu_option(selector, option):
    """Generates a standardized menu option
    
    Keyword Arguments:
    selector -- The number the user will press to select the option
    option -- The text of the option
    """
    print(Fore.CYAN + " [" + selector + "]" + Fore.WHITE + " " + option + "")


def get_sanitized_selection(prompt, selection, num_options):
    """Validates Selection by user

    Keyword Arguments:
    prompt -- What does the input ask for
    selection -- What the user selects
    num_options -- The number of available options for the prompt
    
    Returns:
    If the user selects "x", return none (handled later as an exit)
    If the user selects an option outside of range of options, recurse
    If the user selects valid option, return the option selected
    """
    if selection == "x":
        return
    try:
        if int(selection) in range(1, num_options + 1):
            return int(selection)
        else:
            selection = input(prompt)
            return get_sanitized_selection(prompt, selection, num_options)
    except ValueError:
        selection = input(prompt)
        return get_sanitized_selection(prompt, selection, num_options)


class Menu(object):
    """Base Menu Class
    
    Attributes:
    title -- The menu title
    description -- The menu description
    options -- List of options the user can select on the list
    
    """
    def __init__(self, title="", description="", options=[]):
        """Initializes a super menu, giving all sub menus an attribute that points back to it so that the user can navigate back to the super menu

        Parameters:
        options -- List of options the menu will display
        """
        self.title = title
        self.description = description
        self.options = options

    def show_menu(self):
        """Displays the menu to the screen and prompts sanitized user input

        Returns:
        selection -- User selection from menu
        """
        print(Fore.YELLOW + self.title + " " + Fore.WHITE + self.description + "\n") # Standardized Display of title and description
        for option in self.options: # For each option in list of options, write a menu option, adjusting for zero based indexing
            indx = self.options.index(option)
            menu_option(str(indx + 1), option)
        print("\n" + Fore.RED + " [x]" + Fore.WHITE + " Exit") # Standardized exit for prompt
        selection = get_sanitized_selection(
            "Select a directory: ", 0, len(self.options)
        )
        return selection
    
    def __str__(self):
        """String and Repr methods for debugging lists"""
        return self.title

    def __repr__(self):
        return self.title



class SuperMenu(Menu):
    """Class for menu that navigates to other menus based on user selection
    """
    def __init__(self, title="", description="", sub_menus=[]):
        """Initializes a super menu, giving all sub menus an attribute that points back to it so that the user can navigate back to the super menu

        Parameters:
        sub_menus -- List of menu objects this menu instance will navigate to
        """
        self.sub_menus = sub_menus
        for menu in self.sub_menus: # Let all sub menus point back to this menu instance
            menu.super_menu = self
        return super().__init__(
            title=title,
            description=description,
            options=[str(menu) for menu in sub_menus],
        )

    def show_menu(self):
        """Shows menu and handles user selection

        Returns:
        If the user selects "x", exit the program
        If the user selects valid menu, show that menu
        """
        menu_option = super().show_menu()
        if menu_option: # Handling in the sanitized input returns a number only if it is valid
            return self.sub_menus[menu_option - 1].show_menu()
        else: # If the user selects "x", the sanitized input will return nothing, menu_option will be false, so exit the program
            exit(0)


class WebNavMenu(Menu):
    """Class for handling menus where options navigate to webpages
    """
    def __init__(self, title="", description="", tools={}):
        """Initializes a menu with a dictionary of OSINT Tools as options

        Parameters:
        tools -- dictionary of OSINT Tools, where keys are names of the tools and values the urls to those tools
        """
        self.tools = tools
        return super().__init__(
            title=title, description=description, options=list(tools.keys()) # Make the options a list of the tool names
        )

    def show_menu(self):
        """Shows menu and handles user selection

        Returns:
        If the user selects "x", return to the super menu
        If the user selects valid menu, navigate to that tools page
        """
        menu_option = super().show_menu()
        if menu_option:
            tools = list(self.tools.keys())
            dict_key = tools[menu_option - 1] # Adjusting for zero based index 
            webbrowser.open(self.tools[dict_key])
        else:
            self.super_menu.show_menu() # Navigate to the webpage
