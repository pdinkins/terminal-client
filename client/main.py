# terminal-client

import platform
import os


class Interface:
    """
    title and menu objects are required to instantiate the Interface class
    """
    def __init__(self, title, menu):
        self.__title = title
        self.__menu = menu
    
    # Determine the system and clear the terminal screen
    def clear():
        ops = platform.system()
        if ops == 'Darwin':
            os.system('clear')
        else:
            os.system('cls')

    # Clears the screen then displays the title bar
    def refresh_screen():
        clear()
        title()

