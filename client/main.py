# terminal-client

import platform
import os
import shutil
import datetime

class Interface:
    """
    Terminal Interface
    """
    def __init__(self):
        self.__operating_system = platform.system()
    
    # Horizontal Title Bar
    def __title_bar(self):
        print("=" * shutil.get_terminal_size().columns)

    # Title Bar Information
    def __title(self):
        self.__title_bar()
        print('_TERMINAL_UI_____\t\t____', datetime.datetime.now())
        print('\t\t|_____ADMIN_____|')
        print("\t\t\t\t|__", platform.platform())
        print("\t\t\t\t|__", "Python Version:",platform.python_version())
        print("\t\t\t\t|__", platform.machine())
        self.__title_bar()

    # Determine the system and clear the terminal screen
    def __clear(self):
        if self.__operating_system == 'Darwin':
            os.system('clear')
        elif self.__operating_system == 'Windows':
            os.system('cls')

    # Clears the screen then displays the title bar
    def display(self):
        self.__clear()
        self.__title()


if __name__ == "__main__":
    ui = Interface()
    ui.display()

