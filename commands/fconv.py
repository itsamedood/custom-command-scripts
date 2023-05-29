from os import system, getcwd
from sys import argv


system(f"python3 -B /Users/jr/Documents/ZSH/custom_command_scripts/commands/api/__fconv__.py %s --cwd={getcwd()}"
        %(' '.join(argv[1:]) if len(argv) > 1 else '--help'))
