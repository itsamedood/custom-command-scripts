def colors_16(_color: str) -> str: return f"\033[2;{_color}m {_color}\033[0;0m "
def colors_256(_color: int) -> str:
    color = str(_color).ljust(3, " ")

    if _color % 16 == 0: return f"\033[38;5;{_color}m {color}\033[0;0m\n "
    return f"\033[38;5;{_color}m {color}\033[0;0m "

if __name__ == "__main__":
    print("The 16 colors scheme:\n", " ".join([colors_16(str(x)) for x in range(30, 38)]), "\n\n")
    print("The 256 colors scheme:\n", " ".join([colors_256(x) for x in range(256)]))
