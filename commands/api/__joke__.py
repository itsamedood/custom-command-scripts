from enum import Enum
from json import loads
from random import randint
from requests import get


url = "https://v2.jokeapi.dev/joke/Any"


class JokeCategory(Enum):
    PROGRAMMING = "Programming"
    MISC = "Misc"
    DARK = "Dark"
    PUN = "Pun"
    SPOOKY = "Spooky"
    CHRISTMAS = "Christmas"


class JokeType(Enum):
    SINGLE = "single"
    TWOPART = "twopart"


class JokeData:
    error: bool
    category: JokeCategory
    type: JokeType
    joke: str | None
    setup: str | None
    delivery: str | None
    flags: dict[str, bool]
    safe: bool
    id: int
    lang: str

    def __init__(self, data) -> None:
        self.__data = data
        self.category = JokeCategory(data["category"])
        self.type = JokeType(data["type"])
        self.joke = data["joke"] if "joke" in data else None
        self.setup = data["setup"] if "setup" in data else None
        self.delivery = data["delivery"] if "delivery" in data else None
        self.flags = data["flags"]
        self.id = data["id"]
        self.lang = data["lang"]

    def json(self): return self.__data


def display_joke(joke_data: JokeData) -> None:
    if joke_data.joke: print("\033[1;32m%s\033[0;0;0m" %joke_data.joke)
    else:
        print("\033[2m%s\033[0;0;0m" %joke_data.setup)
        print("\033[1;32m%s\033[0;0;0m" %joke_data.delivery)

joke_data: JokeData = None

try:
    res = get(url)
    joke_data = JokeData(res.json())
    display_joke(joke_data)

except: print("Couldn't get a joke!")
