import random
arr = []
n = int(input())
for i in range(n):
    arr.append([random.randint(1, 10) for i in range(n)])
for i in range(n):
    print(arr[i])
m = arr[0][0]
mi = 0
mj = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] > m:
            m = arr[i][j]
            mi = i
            mj = j
print(m, '\n', mi, ' ', mj, sep = '')
input()