#number 1
string = "";    add = "";    part1 = "";    part2 = ""; arr = []
add = input()
add = add + " "
a = add.count(" ")
for i in range(0, a):
    string = add[0:add.index(" ")]
    if len(string) % 2 == 0:
        part1 = string[0:(len(string) // 2)]
        part2 = string[(len(string) // 2):len(string)]
    else:
        part1 = string[0:(len(string) // 2)]
        part2 = string[(len(string) // 2) + 1:len(string)]
    print("p1 =", part1,"p2 =", part2)
    part2 = part2[::-1]
    if part1 == part2:
        print("st=", string)
    add = add[add.find(" ") + 1:len(add)]