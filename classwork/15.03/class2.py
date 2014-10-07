n = int(input())
arr = []
for i in range(0, n):
    arr.append([0 for i in range(n)])
for i in range(0, n):
    k = n
    for j in range(i, -1, -1):
        arr[i][j] = k
        k -= 1
for i in range(0, n):
    print(arr[i])
input()