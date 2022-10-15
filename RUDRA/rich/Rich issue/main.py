from rich import *

import cmd2


class FirstApp(cmd2.Cmd):
    """A simple cmd2 application."""
 
'''   super().__init__(multiline_commands=['echo'], persistent_history_file='cmd2_history.dat', startup_script="scripts/startup.txt", use_ipython=True)
    
    self.locals_in_py = True


    self.intro = style("Welcome to cmd2 intigrated with rich: ", fg='blue', bg='white', bold=True)

    self.locals_in_py = True

    self.default_category = 'cmd2 Built-in-commands'''


if __name__ == '__main__':
    import sys
    c = FirstApp()
    sys.exit(c.cmdloop())