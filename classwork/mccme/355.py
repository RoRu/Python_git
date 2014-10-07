import random

arr = []
s = ""
n = int(input())

for i in range(n):
    arr.append([0 for i in range(n)])

for i in range(0, n):
    print(arr[i]) 

for i in range(n):
    for j in range(n):
        if arr[i][j] != arr[j][i]:
            s = 'no'
            break
    if s == 'no':
        break
    if i == n - 1:
        s = 'yes'
print(s)
input()