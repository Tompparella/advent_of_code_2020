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



def findTrees(origin_map, x_move, y_move):
    tree_map = []
    tree_map.extend(origin_map)
    trees = 0
    x = 0
    y = 0
    while True:
        x += x_move
        y += y_move

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
    return trees




def main():
    tree_map = readFile()

    trees1 = findTrees(tree_map, 1, 1)
    trees2 = findTrees(tree_map, 3, 1)
    trees3 = findTrees(tree_map, 5, 1)
    trees4 = findTrees(tree_map, 7, 1)
    trees5 = findTrees(tree_map, 1, 2)

    print("{} {} {} {} {}".format(trees1,trees2,trees3,trees4,trees5))
    trees_total = trees1+trees2+trees3+trees4+trees5
    trees_multiply = trees1*trees2*trees3*trees4*trees5
    print("You came across {} trees!\nMultiplied total: {}".format(trees_total, trees_multiply))




if __name__ == "__main__":
    main()