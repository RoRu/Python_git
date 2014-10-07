arr = []
winner = []
n = int(input())
m = int(input())

for i in range(n):
    arr.append([int(input()) for j in range(m)])

for i in range(n):
    winner.append(max(arr[i]))

w = winner.count(max(winner))
print(w)
for i in range(n):
    if winner[i] == max(winner):
        print(i, end=' ')