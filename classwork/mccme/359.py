import random

arr = []
winner = []
n = int(input())
m = int(input())
for i in range(n):
    arr.append([random.randint(4, 10) for j in range(m)])
for i in range(n):
    winner.append(max(arr[i]))

w = winner.count(max(winner))
print(w)
input()