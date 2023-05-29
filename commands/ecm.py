# Every Cent Matters, a personal money tracker.
from os import system, getenv
from os.path import exists

HOME = getenv("HOME")
PATH = "%s/Documents/ZSH/custom_command_scripts" %HOME
DOTFILE = "%s/dotfiles/.ecm" %PATH

def setup() -> None: ...


if __name__ == "__main__":
    if not exists(DOTFILE):
        system("touch %s" %DOTFILE)
        setup()

    else:
        with open(DOTFILE, 'r') as dotecm:
            text = dotecm.readlines()

            if len(text) < 1: setup()
