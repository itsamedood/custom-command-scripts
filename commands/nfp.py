from os import system


def gen_project() -> None:
    proj_name: str = ""
    while not len(proj_name) > 0:system("clear"); proj_name = input("Project name: ")
    system(f"cd ~/Documents/Games/HaxeFlixel && flixel tpl -n %s --ide vscode" %proj_name)


if __name__ == "__main__": gen_project()
