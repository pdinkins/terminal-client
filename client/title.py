# terminal-client/client/title.py

import shutil

# Horizontal Title Bar
def title_bar():
    print("=" * shutil.get_terminal_size().columns)

# Title Bar Information
def title():
    title_bar()
    print('__ORION_NET_____\t\t____', dt1.dt())
    if __title_stat[0] == 0:
        print('\t\t|__LOGIN')
        title_bar()
    
    elif __title_stat[0] == 1:
        print('\t\t|__LOGIN_FAILED__')
        title_bar()
    
    elif __title_stat[0] == 2:
        print('\t\t|__NODE_ADMIN___|')
        print("\t\t\t\t|__", platform.platform())
        print("\t\t\t\t|__", "Python Version:",platform.python_version())
        print("\t\t\t\t|__", platform.machine())
        title_bar()