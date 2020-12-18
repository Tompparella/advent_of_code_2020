FILENAME = "input.txt"


def readFile():
    try:
        with open(FILENAME) as f:
            content = f.readlines()
    except:
        print("Error when reading file")
    stripped_list = []
    final = []
    list_end = 0
    index = 0

    for i in content:
        print(i)
        #print("Entry: {}".format(i))

        if ((i == "\n")):
            temp = stripped_list[list_end:index]
            list_end = index
            temp = list(filter(None, temp))
            unified = []
            string = ''
            for x in temp:
                string += (x+" ")
            unified.append(string)
           # temp = ",".join(temp)
           # temp = temp.replace(",", " ")
            final.append(unified)
            # print(unified)

        elif ((index == len(content)-1)):
            i = i.rstrip()
            stripped_list.append(i)
            temp = stripped_list[list_end:]
            #print("Last: {}".format(temp))
            list_end = index
            temp = list(filter(None, temp))
            unified = []
            string = ''
            for x in temp:
                string += (x+" ")
            unified.append(string)
           # temp = ",".join(temp)
           # temp = temp.replace(",", " ")
            final.append(unified)
            # print(unified)

        i = i.rstrip()
        stripped_list.append(i)
        index += 1

    return final


def analyzeData(data):
    analyzedData = {
        "invalid": 0,
        "total": 0
    }

    for i in data:
        i = "".join(i)
        fields = 0
        #passport = i.split(" ")
        state = True

        # for x in passport:

        if "ecl" in i:
            fields += 1
        if "pid" in i:
            fields += 1
        if "eyr" in i:
            fields += 1
        if "hcl" in i:
            fields += 1
        if "byr" in i:
            fields += 1
        if "iyr" in i:
            fields += 1
        if "hgt" in i:
            fields += 1

        if fields != 7:
            analyzedData["invalid"] += 1
            state = False
        analyzedData["total"] += 1

        #print("{} ----- {}".format(i, state))

    return analyzedData


def main():
    data = readFile()
    analyzedData = analyzeData(data)
    print("Number of passports analyzed in total: {}\nNumber of invalid passports: {}\nNumber of valid passports: {}".format(
        analyzedData["total"], analyzedData["invalid"], analyzedData["total"]-analyzedData["invalid"]))


if __name__ == "__main__":
    main()
