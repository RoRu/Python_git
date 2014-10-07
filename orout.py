import random
a = []
a.extend([a.append([random.randint(1, 20) for i in range(0, 5)])
               for i in range(0, 4)])
for i in range(0, 4):
    print(a[i])