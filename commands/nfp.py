from os import system


def gen_project() -> None:  # alias nfp="cd ~/Documents/Games/HaxeFlixel && flixel tpl -n" # New Flixel Project.
    proj_name: str = ""
    while not len(proj_name) > 0: proj_name = input("Project name: ")

    system(f"cd ~/Documents/Games/HaxeFlixel && flixel tpl -n {proj_name} --ide vscode")

# Do you get Deja Vu?
if __name__ == "__main__": gen_project()
