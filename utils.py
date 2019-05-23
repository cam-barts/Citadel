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
    print(Fore.CYAN + " [" + selector + "]" + Fore.WHITE + " " + option + "")


def get_sanitized_selection(prompt, selection, num_options):
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
    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def show_menu(self):
        print(Fore.YELLOW + self.title + " " + Fore.WHITE + self.description + "\n")
        for i in self.options:
            indx = self.options.index(i)
            menu_option(str(indx + 1), i)
        print("\n" + Fore.RED + " [x]" + Fore.WHITE + " Exit")
        selection = get_sanitized_selection(
            "Select a directory: ", 0, len(self.options)
        )
        return selection

    def __init__(self, title="", description="", options=[]):
        self.title = title
        self.description = description
        self.options = options


class SuperMenu(Menu):
    def __init__(self, title="", description="", options=[], sub_menus=[]):
        self.sub_menus = sub_menus
        for menu in self.sub_menus:
            menu.super_menu = self
        return super().__init__(
            title=title,
            description=description,
            options=[str(menu) for menu in sub_menus],
        )

    def show_menu(self):
        menu_option = super().show_menu()
        if menu_option:
            return self.sub_menus[menu_option - 1].show_menu()
        else:
            exit(0)


class WebNavMenu(Menu):
    def __init__(self, title="", description="", tools={}):
        self.tools = tools
        return super().__init__(
            title=title, description=description, options=list(tools.keys())
        )

    def show_menu(self):
        menu_option = super().show_menu()
        if menu_option:
            tools = list(self.tools.keys())
            dict_key = tools[menu_option - 1]
            webbrowser.open(self.tools[dict_key])
        else:
            self.super_menu.show_menu()
