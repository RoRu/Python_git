import random
a = []
for i in range(7):
    a.append([random.randint(50, 150) for i in range(7)])
for i in range(7):
    for j in range(7):
        print('%5d' % a[i][j], end=" ")
    print()
input()