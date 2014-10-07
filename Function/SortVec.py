from random import randint
def vecsort(vrr):
    add = [];    arr = []
    c = 0
    for i in vrr:
        arr.append((i[0] ** 2 + i[1] ** 2) ** 0.5)
    arr.sort()
    for i in range(len(vrr)):
        for j in vrr:
            if arr[i] == (j[0] ** 2 + j[1] ** 2) ** 0.5:
                add.append(j)
                break
    print(add)
    print()

#main
vec = []
for i in range(4):
    vec.append([randint(4, 20) for j in range(2)])
print(vec)
print()
vecsort(vec)