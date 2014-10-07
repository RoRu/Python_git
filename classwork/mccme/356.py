import random

arr = []
s = []
n = int(input())

for i in range(n):
    arr.append([random.randint(5, 20) for i in range(n)])

for i in range(n):
    print(arr[i])

for i in range(n):
    s.append(sum(arr[i]))

for i in range(n):
    if s[i] == max(s):
        print(max(s), i)
        break
input()