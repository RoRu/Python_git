#pascal triangle
n = int(input())
arr = []
for i in range(0, n):
    arr.append([0 for i in range(n)])
for i in range(0, n):
    arr[i][i] = 1
    arr[i][0] = 1
for i in range(2, n):
    for j in range(1, i):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
for i in range(0, n):
    print(arr[i])
input()