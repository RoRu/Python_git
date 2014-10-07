n = int(input())
arr = []

for i in range(n):
    arr.append([0 for i in range(n)])

for i in range(0, n):
    arr[i][n - i - 1] = 1

for i in range(0, n):
    for j in range(0, n):
        if j > i:
            arr[n - i - 1][j] = 2

for i in range(0, n):
    print(arr[i])
input()