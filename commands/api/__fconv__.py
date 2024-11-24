"""
fconv -> File Converter
Doesn't work rn :(
"""


from base64 import b64encode
from dotenv import load_dotenv; load_dotenv()
from os import environ
from requests import post as POST
from sys import argv


def get_args() -> tuple[str, str, str]:
    cwd, file, newExt = '', '', ''

    for arg in argv[1:]:
        if len(arg) > 1 and arg[:2] == "--":
            split = arg.split('=')
            if len(split) < 2:
                match arg[2:]:
                    case "help":
                        print('\n'.join([
                            "Usage:",
                            "fconv <flag(s)>\n",
                            "Flags:",
                            "--help",
                            "--version",
                            "--cwd=<cwd>",
                            "╭─ --file=<file>",
                            "╰─ --newExt=<extension>",
                        ]))

                    case "version": print("fconv\nVersion 0.0.1")
                    case arg: raise Exception("Missing '='.")

            elif len(split) >= 3: raise Exception("Too many '='.")
            else:
                flag, value = split[0][2:], split[1]

                match flag:
                    case "cwd": cwd = value
                    case "file": file = value
                    case "newExt": newExt = value

        else: raise Exception("Invalid argument: '%s'." %arg)

    return (cwd, file, newExt)


def convert():
    BASE_URL = "https://api.convertio.co/convert"

    cwd, file, newExt = get_args()
    encoded_data = ''

    with open(f"{cwd}/{file}", "rb") as of: encoded_data = b64encode(of.read()).decode("utf-8")

    payload = {
        "apikey": environ["CONVERTIO_API_KEY"],
        "input": "base64",
        "outputformat": newExt,
        "file": encoded_data,
        "filename": file
    }

    res = POST(BASE_URL, data=payload)

    if res.ok:
        resjson = res.json()
        for keys in resjson:
            print(keys)

    else:
        resjson = res.json()

        with open("/Users/jr/Documents/ZSH/custom_command_scripts/logs/fconv.log", 'w') as log:
            log.write(resjson["error"])

        print("Failed with code %s, check `logs/fconv.log` for details." %resjson["code"])


if __name__ == "__main__": convert()
