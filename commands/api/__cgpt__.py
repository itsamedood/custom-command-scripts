from dotenv import load_dotenv
from os import environ, system
from requests import post
from sys import exit


load_dotenv("/Users/jr/Documents/ZSH/custom_command_scripts/.env")


def request(prompt: str) -> str:
    api_key = environ["OPENAI_API_KEY"]
    model = "text-davinci-003"

    res = post(f"https://api.openai.com/v1/completions", headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }, json={
        "model": model,
        "prompt": prompt,
        "max_tokens": 1000,
        "n": 1,
    }).json()

    try:
        return res["choices"][0]["text"]
    except KeyError: print(res); exit(0)


if __name__ == "__main__":
    with open("/Users/jr/Documents/ZSH/custom_command_scripts/logs/cgpt.log", 'a') as log:
        try:
            while True:
                prompt = input("👨 ")

                match prompt:
                    case ".exit": log.write("SYSTEM: Exited."); break
                    case ".clear": log.write("SYSTEM: Cleared terminal."); system("clear")
                    case prompt:
                        res = request(prompt).strip()
                        log.write("ME: \"%s\"\n" %prompt)

                        print("🤖 %s" %res)
                        log.write("CHAT-GPT: \"%s\"\n\n" %res)

        except KeyboardInterrupt: log.write("SYSTEM: KeyboardInterrupt triggered, exited.")
        except:
            print("ERROR: Connection could not be made.")
            log.write("SYSTEM: ERROR: Connection could not be made.")

        log.close()
