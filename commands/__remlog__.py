import inquirer
from os import system


SAVED = {
    "My Desktop": "192.168.1.253",
    "Alijahs Fedora Desktop": "10.0.0.127"
}

def get_ip() -> str | None:
    questions = [
        inquirer.List("ip", message="Which IP are you connecting to?", choices=[k for k in SAVED.keys()])
    ]

    answer = inquirer.prompt(questions)
    return SAVED[answer["ip"]] if answer is not None else None

if __name__ == "__main__":
    ip = get_ip()
    if ip is None: raise Exception("could not get ip :(")

    print("Connecting to %s" %ip)
    system("putty %s" %ip)
