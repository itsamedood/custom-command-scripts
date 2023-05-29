from os import system, getenv, scandir
from sys import argv


HOME = getenv("HOME")
PATH = "%s/Documents/ZSH/custom_command_scripts/commands" %HOME
THIS = "%s/Documents/ZSH/custom_command_scripts" %HOME
existing_scripts = [es.name[:-3] for es in scandir(PATH) if es.name[-3:] == ".py"]
flags = [a[2:] for a in argv if a[:2] == "--"]

def analyze_flags() -> dict[str, list[str]]:
    flag_map: dict[str, list[str]] = {}

    for flag in flags:
        has_eqs = len([e for e in flag if e == '=']) > 0

        match flag.split('=')[0] if has_eqs else flag:
            case "exclude":
                if not has_eqs: raise Exception("Flag 'exclude' requires argument.")
                flag_map["exclude"] = flag.split('=')[1].split(',')

            case "help": ...

    return flag_map

def get_files_to_compile() -> list[str]: return [f for f in argv if f in existing_scripts
    or f == "all" or f == "self"]

def compile_scripts(_files: list[str], _exclude: list[str]) -> None:
    for f in _files:
        if f == "self":
            print(f"\033[1;33mCompiling compile.py...\033[0;0m")
            system(f"cxfreeze --target-dir ./out/ccsc --target-name ccsc {THIS}/compile.py")
            print(f"\033[1;32mCompiled compile.py!\033[0;0m")

        else:
            if f not in _exclude and not f[:1] == "__":
                print(f"\033[1;33mCompiling {f}.py...\033[0;0m")
                system(f"cxfreeze --target-dir ./out/{f} --target-name {f} {PATH}/{f}.py")
                print(f"\033[1;32mCompiled {f}.py!\033[0;0m")

def run(_flags_map: dict[str, list[str]]) -> ...:
    try: global exclude; exclude = _flags_map["exclude"]
    except KeyError: exclude = []

    files = get_files_to_compile()
    if len(files) < 1: print("Files not found or none were given.")
    compile_scripts(
        ["self"] if "self" in files else existing_scripts if "all" in files or "*" in files else files, exclude
    )


if __name__ == "__main__": run(analyze_flags())
