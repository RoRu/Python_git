arr = []
a = int(input())
n = int(input())
c = 0
for i in range(0, n):
    arr.append(a + i)
for i in arr:
    if (i ** 0.5) % 1 == 0:
        c += 1
        continue
    else:
        x = ((i / 2) ** 0.5) // 1
        for j in range(int(x), 0, -1):
            if i % (j ** 2) == 0:
                c = c + i / (j ** 2)
                break 
print(int(c))