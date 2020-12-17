
import re

FILENAME = "input.txt"


def readFile():
    try:
        with open(FILENAME) as f:
            content = f.readlines()
    except:
        print("Error when reading file")
    final = []
    for i in content:
        i = (i.rstrip())
        i = re.split('[- :]', i)
        i.pop(3)
        final.append(i)
    return final


def findCorruptions(passList):
    passwords = {
        "corruptions": 0,
        "entries": 0
    }
    corruptions = 0
    for i in passList:
        state = False
        min = i[0]
        max = i[1]
        char = i[2]
        password = i[3]
        passwords["entries"] += 1
        if ((password.count(char) < int(min)) or (password.count(char) > int(max))):
            passwords["corruptions"] += 1
            state = True
        #print(("{}   {}  {}  {} {}").format(min, max, char, password, state))

    return passwords


def main():
    passList = []
    passList = readFile()
    log = findCorruptions(passList)
    print(("Found {} corruptions out of {} entries.\n{} passwords are valid.").format(log["corruptions"], log["entries"], (log["entries"] - log["corruptions"])))


if __name__ == "__main__":
    main()
