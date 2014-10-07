arr = []
n = int(input())
m = int(input())

for i in range(n):
    arr.append([0 for i in range(m)])

for i in range(m):
    arr[0][i] = i
    if i == m - 1:
        k = i + m

for i in range(1, n):
    for j in range(m):
        arr[i][j] = k
        if j == m - 1:
            continue
        if i % 2 != 0:
            k -= 1
        else:
            k += 1
    k = k + m

for i in range(n):
    for j in range(m):
        print(a[i][j], ' ', sep = '', end = ' ')
    print('\n')
input()