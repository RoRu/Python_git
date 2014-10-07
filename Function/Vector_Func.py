"""functions for work with scalars"""
from random import randint
def sumvec(x1, y1, x2, y2, xres, yres):
    xres = x1 + x2
    yres = y1 + y2
    print(xres, yres)

def scalarvec(x1, y1, k, xres, yres):
    xres, yres = (x1 * k), (y1 * k)
    print(xres, yres)

def scalarmult(x1, y1, x2, y2):
    return(x1* x2 + y1 * y2)

def lengthvec(x1, y1):
    return((x1 ** 2 + y1 ** 2) ** 0.5)

def writevec(x1, y1):
    print("(", x1, ";", y1, ")", end="")

def readvec(x1, y1):
   x1 = int(input())
   y1 = int(input())
   return(x1, y1)

def vecsort(vrr):
    add = [];    arr = []
    c = 0
    for i in vrr:
        arr.append((i[0] ** 2 + i[1] ** 2) ** 0.5)
    arr.sort()
    for i in range(len(vrr)):
        for j in vrr:
            if arr[i] == (j[0] ** 2 + j[1] ** 2) ** 0.5:
                add.append(j)
                break
    return(add)
    print(add, "/n")

#main
x = int(input())
y = int(input())
while True:
    print('1: Generate Array\n'
            '2:' 
            '3: '
            '4:ray\n' 
            '5:ray\n' 
            '6:' 
            '7:\n' 
            '8:n' 
            '9:Entrer vector by myself\n'
            '10: Exit')
    num = int(input('What to do: '))