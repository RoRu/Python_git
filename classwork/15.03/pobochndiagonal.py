#1 class work
n = int(input())
arr = []
k = 1
for i in range(n):
    arr.append([0 for i in range(n)])
for i in range(0, n):
    arr[i][n - i - 1] = k
    k = k +1
for i in range(0, n):
    print(arr[i]) 