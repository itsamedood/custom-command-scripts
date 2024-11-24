# 06/04/23

from __out__ import Ansi
from os import system
from random import randint


BIBLE_PROMISES_FOR_GRADUATES: dict[str, dict[int, tuple[str, str]]] = {
    "ABILITY": {
        0: ("We are not saying that we can do this work ourselves.\nIt is God who makes us able to do all that we do.", "2 Corinthians 3:5 NCV"),
        1: ("Take a new grip with your tired hands and\nstrengthen your weak knees. Mark out a straight\npath for your feet so that those who are weak and\nlame will not fall but become strong.", "Hebrews 12:12-13 NLT"),
        2: ("\"My grace is sufficient for you, for my power is\nmade perfect in weakness.\" Therefore I will boast\nall the more gladly of my weaknesses, so that the\npower of Christ may rest upon me.", "2 Corinthians 12:9 ESV"),
    },
}


def get_random_promise() -> tuple[str, str]:
    keys = [k for k in BIBLE_PROMISES_FOR_GRADUATES.keys()]
    rand_key = keys[randint(0, len(keys)-1)]
    ints = [i for i in BIBLE_PROMISES_FOR_GRADUATES[rand_key].keys()]
    random_promise = BIBLE_PROMISES_FOR_GRADUATES[rand_key][randint(0, len(ints)-1)]

    return random_promise


def print_random_promise(promise_tuple: tuple[str, str]) -> None:
    promise, location = promise_tuple

    print(promise)
    print(f"- {Ansi.style.ITALICIZED}{Ansi.style.LIGHT}{location}{Ansi.special.RESET}")


if __name__ == "__main__": print_random_promise(get_random_promise())
