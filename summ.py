import random
a = []
sum = 0
for i in range(0, 5):
    a.append([random.randint(1, 40) for i in range(0, 5)])
    for j in range(0, 5):
        sum = sum + a[i][j]
print(sum)