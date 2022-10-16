from sys import argv


def gen_project() -> None:  # alias nfp="cd ~/Documents/Games/HaxeFlixel && flixel tpl -n" # New Flixel Project.
    flags = [f for f in argv if f[:2] == "--"]
    params = [p for p in argv if p not in flags]

    print(f"FLAGS: {flags}\n", f"PARAMS: {params}\n")

if __name__ == "__main__": gen_project()
