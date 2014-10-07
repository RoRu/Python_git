#number 4 (1 mas)
from random import randint
sect = []  
mark = []
ma = 0
ob = 0
n = int(input())
for i in range(n):
    a = input("name of section:")
    sect.append(a)
    d = int(input("number of marks:"))
    mark.append(d)
print(sum(mark))
ma = mark.index(max(mark))
print(sect[ma], max(mark))