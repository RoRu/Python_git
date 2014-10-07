# WIN!!!!!
a = []
n = int(input())
m = int(input())

for i in range(n):
    a.append([0 for i in range(m)])

for i in range(1, m):
    a[0][i] = a[0][i - 1] + i
    if i > n:
        a[0][i] = a[0][i - 1] + n

k = n
for i in range(1, n):
    a[i][m - 1] = a[i - 1][m - 1] + k
    k -= 1

for i in range(1, n):
    for j in range(m - 1):
        a[i][j] = a[i - 1][j + 1] + 1

for i in range(n):
    for j in range(m):
        print(a[i][j], ' ', sep = '', end = ' ')
    print('\n')
input()
# WIN!!!!