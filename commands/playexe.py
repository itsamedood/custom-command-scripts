from inquirer import List, prompt
from os import getenv, scandir, system
from os.path import exists


EXE_DIR = "%s/Documents/Games/WINE" %getenv("HOME")


def get_games() -> list[str]: return [g.name for g in scandir(EXE_DIR) if g.is_file() and g.name[-4:] == ".exe"]


def choose_game() -> str:
  game: dict[str, str] | None = prompt([List("game", message="Which game do you wanna play?", choices=get_games(), carousel=True)])

  if game is not None: return game["game"]
  else: raise Exception("choose a game!")


def launch_game(_game: str) -> None:
  print("Running %s..." %_game)
  system(f"wine {EXE_DIR}/{_game} > /dev/null 2>&1")  # Silence output from WINE.
  print("Bye!")


if __name__ == "__main__": launch_game(choose_game())
