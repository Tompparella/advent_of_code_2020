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
        final.append(i)
    return final



def findTrees(tree_map):
    trees = 0
    x = 0
    y = 0
    while True:
        x += 3
        y += 1

        if y > (len(tree_map)-1):
            break

        if x > (len(tree_map[y])-1):
            x -= len(tree_map[y])

        if tree_map[y][x] == "#":
            trees += 1
            temp = list(tree_map[y])
            temp[x] = "X"
            tree_map[y] = "".join(temp)
            #tree_map[y][x] = "X"

        else:
            temp = list(tree_map[y])
            temp[x] = "O"
            tree_map[y] = "".join(temp)
            #tree_map[y][x] = "O"     
          
        print(tree_map[y])

    return trees




def main():
    tree_map = readFile()
    trees = findTrees(tree_map)
    print("You came across {} trees!".format(trees))




if __name__ == "__main__":
    main()