from datetime import datetime
from sys import exit, argv
from time import sleep

def print_and_sleep(t: tuple[str, int]) -> None: print("• %s\n" %t[0]); sleep(t[1])

def countdown() -> None:
    print("CREED ON 3."); sleep(1)
    print("1..."); sleep(1)
    print("2..."); sleep(1)
    print("3...\n"); sleep(1)

def do_creed() -> int:
    CREED: list[tuple[str, int]] = [
        ("I am an Army Junior ROTC Cadet.", 1),
        ("I will always conduct myself to bring credit to my family, country, school\nand the Corps of Cadets.", 2),
        ("I am loyal and patriotic.", 1),
        ("I am the future of the United States of America.", 2),
        ("I do not lie, cheat, or steal and will always be accountable\nfor my actions and deeds.", 3),
        ("I will always practice good citizenship and patriotism.", 2),
        ("I will work hard to improve my mind and strengthen my body.", 2),
        ("I will seek the mantle of leadership and stand prepared to uphold\nthe Constitution and the American way of life.", 4),
        ("May God grant me the strength to always live by this creed.", 3)
    ]

    countdown(); [print_and_sleep(s) for s in CREED]
    with open(argv[1], 'w') as creedfile: creedfile.write('👌'); return 0

if __name__ == "__main__":
    try:
        if len(argv) < 1: raise Exception("need path arg.")

        with open(argv[1], 'r') as creedfile:
            if datetime.today().weekday() == 2:
                exit(do_creed()) if not len(creedfile.read()) > 0 else ...
            else:
                with open(argv[1], 'w') as creedfile: creedfile.write('')

    except IndexError: print("\n\033[31mYou may not run this program manually.\033[0m"); exit(1)
    except KeyboardInterrupt: print("\n\033[31mInterrupted. How dare you.\033[0m"); exit(1)
