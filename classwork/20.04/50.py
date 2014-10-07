from random import randint
arr  = []
arr = [randint(-5, 5) for i in range(8)]
for i in arr:
    print(i, end=" ")
k = -1
for i in range(len(arr)):
    if arr[i] < 0 and i > 0:
        arr.insert(0, arr[i])
        del(arr[i])
print()
del(arr[-1])
for i in arr:
    print(i, end=" ")