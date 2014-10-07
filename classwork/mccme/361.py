arr = []
n = int(input())
m = int(input())
n -= 1
m -= 1
a = 0

for i in range(n):
    arr.append([0 for j in range(m)])
j = 0
for i in range(n):
    a = i
    arr[i][j] = a * j
    if j < m:
        a = a - 1
        j = j - 1
    else:
        j = 0
for i in range(n):
    for j in range(m):
        print('%3d' % arr[i][j], end=" ")
    print()