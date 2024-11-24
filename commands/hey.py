from __hey__ import *
from os import getenv
from os.path import exists
from sys import argv, exit


# Simple commands.
COMMANDS = ["run", "exec", "nvm", "config", "rename"]
DOTFILE = "%s/dotfiles/.hey" %getenv("CCS")


def init() -> None:
  name = ''
  while len(name) < 1: name = input("What will you call me? (Ex. computer, program, etc.)")
  with open(DOTFILE, 'a') as dotfile: dotfile.write("name=%s" %name)
  exit(0)


def read_dotfile() -> dict[str, str]:
  properties: dict[str, str] = {}

  with open(DOTFILE, 'r') as dotfile:
    lines = dotfile.readlines()

    for i, line in enumerate(lines):
      if '=' in line:
        pv = line.split()
        prop, val = pv[0], pv[1]

        if len(prop) < 1: raise Exception("Missing property name @ line %s" %i)
        if len(val) < 1: raise Exception("Missing value name @ line %s" %i)

        properties[prop] = val

  return properties


def handle_command(_cmd: str) -> None:
  match _cmd:
    case "run": ...
    case "exec": ...
    case "config": ...
    case "rename": ...
    case "nvm": ...
    case _: ...


if __name__ == "__main__":
  if not exists(DOTFILE): init()
  if len(argv) < 1: exit(0)

  config = read_dotfile()

  if argv[1] == config["name"]:
    command = input("How can I help you, %s?" %getenv("USER"))
