from random import randint
arr = []
koord = []
arr = [randint(1, 15) for i in range(8)]
for i in arr:
    print(i, end=' ')
print()
for i in range(0, len(arr), +2):
    print(i)
    koord.append((arr[i] ** 2) + (arr[i + 1] ** 2))
for i in koord:
    print(i, end=' ')
result = max(koord) ** (1/2)
print(result)