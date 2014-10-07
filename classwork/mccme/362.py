arr = []
n = int(input())
m = int(input())
for i in range(n):
    arr.append([0 for i in range(m)])

for i in range(n):
    for j in range(m):
        arr[0][j] = arr[i][0] = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] != 1:
            arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

for i in range(n):
    for j in range(m):
        print('%3d' % arr[i][j], end=" ")
    print()
input()