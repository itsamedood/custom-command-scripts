from os import system, getenv, scandir
from sys import argv


HOME = getenv("HOME"); PATH = f"{HOME}/Documents/ZSH/custom_command_scripts/commands"
existing_scripts = [es.name[:-3] for es in scandir(PATH) if es.name[-3:] == ".py"]
flags = [a for a in argv if a[:2] == "--"]

def get_files_to_compile() -> list[str]: return [f for f in argv if f in existing_scripts or f == "all"]

def compile_script(_files: list[str]) -> list[str]:
    for f in _files: print(f"\033[1;33mCompiling {f}.py...\033[0;0m"); system(f"cxfreeze --target-dir ./out/{f} --target-name {f} {PATH}/{f}.py")
    return _files


if __name__ == "__main__":
    files = get_files_to_compile()
    if len(files) < 1: raise Exception("No files given to compile.")

    [print(f"\033[1;32mCompiled {s}.py!\033[0;0m") for s in compile_script(existing_scripts if "all" in files else files)]
