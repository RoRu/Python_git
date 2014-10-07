import random
a = []
flag = False
n = int(input("Number of rows and columns: "))
n = random.randint(1, 20)
print('Nobody cares. It is ', n, '.', sep = '')
n1 = n
j = 0
for i in range(0, n):
    a.append([random.randint(1, 20) for i in range(0, n1)])
for i in range(0, len(a)):
    sum = 0
    for j in range(0, len(a[i])):
        if j != i:
            sum  = sum + a[i][j]
        if a[i][i] >= sum:
            flag = True
        else:
            flag = False
for i in range(0, n):
    print(a[i])
print(flag)