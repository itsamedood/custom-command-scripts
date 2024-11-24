from os import getenv, system, scandir
from sys import exit, argv


class CCSError(BaseException):
    def __init__(self, message: str) -> None: print("ccs: \033[1;31merror\033[0;0m: %s." %message); return exit(1)


HOME = getenv("HOME"); PATH = "%s/Documents/ZSH/custom_command_scripts" %HOME
CMDS = ["compile", "edit", "test", "list", "rm", "help"]


def help() -> None: print("Commands:"); [print("• %s" %c) for c in CMDS]


def test(script: str, args: str) -> None:
    if "%s.py" %script not in [s.name for s in scandir("%s/commands" %PATH)]: raise CCSError("script not found")
    system(f"python3 -B {PATH}/commands/{script}.py {args}")


def edit(args: list[str] | None):
    if args is None: system("vim %s" %PATH)

    elif args[0][0] == "-":
        match args[0][1:]:
            case "code": system(f"code {PATH}/commands/{args[1]}.py") if len(args) > 1 else system("code %s" %PATH)
            case _: raise CCSError("unknown flag: '%s'" %args[0])
    else: system(f"vim {PATH}/commands/{args[0]}.py")


if __name__ == "__main__":
    cmd = argv[1] if len(argv) > 1 else None

    match cmd:
        case "compile": system(f"ccsc {' '.join(argv[2:])}")
        case "edit": edit(argv[2:] if len(argv) > 2 else None)
        case "test": test(argv[2], ' '.join(argv[3:])) if len(argv) > 2 else ...
        case "list": [print("• %s" %f.name) for f in scandir("%s/commands" %PATH)]
        case "rm": system(f"rm {PATH}/commands/{argv[2]}.py && rm -r {PATH}/out/{argv[2]}") if len(argv) > 2 else ...
        case "help" | None: help()
        case _: raise CCSError("'%s' is not a command" %cmd)
