#number 5 (2 mas)
from random import randint
arr = []
add = []
for i in range(20):
    arr.append(randint(43, 81))
print(arr)
for i in arr:
    add.append(i // 10)
for i in range(20):
    for j in range(add[i]):
        print("*", end="")
    print()