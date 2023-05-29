plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()_-+={}[]\\;:'\"<>,./?"
cipher = "XYZABCDEFGHIJKLMNOPQRSTUVW `~!@#$%^&*()_-+={}[]\\;:'\"<>,./?"


def encodeCaesarCipher(text = "the QUICK brown FOX jumps OVER the LAZY dog."):
    finalString = ''

    for l in range(len(text)):
        for a in range(len(plain)):
            if text[l] == plain[a]: finalString += cipher[a]
            elif text[l] == plain[a].lower(): finalString += cipher[a].lower()
    return finalString


def decodeCaesarCipher(text = "qeb NRFZH yoltk CLU grjmp LSBO qeb IXWV ald."):
    finalString = ''

    for l in range(len(text)):
        for a in range(len(cipher)):
            if text[l] == cipher[a]: finalString += plain[a]
            elif text[l] == cipher[a].lower(): finalString += plain[a].lower()
    return finalString


if __name__ == "__main__":
    while True:
        option = input("Encode or decode? (e/d) ")

        if option == 'e':
            text = input("Text to encode: ")
            print(encodeCaesarCipher(text))
            break
        elif option == 'd':
            text = input("Text to decode: ")
            print(decodeCaesarCipher(text))
            break
        else: continue
