from os import getenv, system
from sys import argv


HOME = getenv("HOME"); PATH = f"{HOME}/Documents/ZSH/custom_command_scripts"
CMDS = ["compile", "help"]

def help() -> None: return print("Commands:\n•", [f'\n• {c}' for c in CMDS])

if __name__ == "__main__":
    cmd = argv[1] if len(argv) > 1 else None

    match cmd:
        case "compile": system(f"python3 -B {PATH}/compile.py {' '.join(argv[2:])}")
        case "edit": system(f"vim {PATH}/commands/{argv[2]}.py") if len(argv) > 2 else ...
        case "help" | None: help()
        case cmd: print(f"ccs: command not found: {cmd}")
