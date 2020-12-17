import re

FILENAME = "input.txt"
NUMBER = 2020

# I know this is not needed, but I just wanted to practice it.
def quickSort(A):

    length = len(A)
    if (length <= 1):
        return A
    else:
        pivot = A.pop()

    items_greater = []
    items_lower = []

    for i in A:
        if (i > pivot):
            items_greater.append(i)
        else: items_lower.append(i)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

def findMatch(numbers):

    matches = []
    for i in numbers:
        for y in reversed(numbers):
            for x in numbers:
                if (i + y + x == NUMBER):
                    match = {
                        "first": i,
                        "second": y,
                        "third": x
                    }
                    return match

def readFile():
    try:
        with open(FILENAME) as f:
            content = f.readlines()
    except:
        print("Error when reading file")

    a_list = []
    for i in content:
        i = i.rstrip()
        i = int(i)
        a_list.append(i)

    a_list = quickSort(a_list)

    return a_list

def main():
    a_list = readFile()
    match = findMatch(a_list)
    if (match):
        print("{} + {} + {} = {}\nMultiplied: {}".format(match["first"], match["second"], match["third"], NUMBER, match["first"] * match["second"] * match["third"]))

if (__name__ == "__main__"):
    main()