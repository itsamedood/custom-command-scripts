from random import randint


def hack() -> None:
    """hAcKz!!1!11!"""

    while True:
        data = ""

        for _ in range(randint(5, 50)): data += "0" if randint(0, 100) % 2 == 0 else "1"
        print(f"\033[0;32m{data}\033[0m")


if __name__ == "__main__": hack()
