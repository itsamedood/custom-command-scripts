from os import system
from random import randint


def hack() -> None:
    """ hAcKz!!1!11! """
    while True:
        print("\033[1;32m".join(['0' if i % 2 == 0 else '1' for i in [randint(0, 100) for _ in range(randint(5, 50))]]))


if __name__ == "__main__":
    try: hack()
    except KeyboardInterrupt: print("\033[0;0;0m"); system("clear")
