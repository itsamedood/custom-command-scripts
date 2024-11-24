from os import system
from sys import argv


if __name__ == "__main__": [system("python3 -B compile.py %s" %a) for a in argv[1:]]
