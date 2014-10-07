def RandomMatrix(trow, tcol):
    from random import randint
    arr = []
    for i in range(trow):
        arr.append([randint(0, 50) for j in range(tcol)])
    return(arr)

def PrintMx(arr):
    for i in arr:
        for j in i:
            print('%3d' % j, end=" ")
        print()

def MxScalar(arr, k):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] = arr[i][j] * k
    return(arr)

def SumMx(arr, brr, srr):
    if len(arr) == len(brr) and len(arr[0]) == len(brr[0]):
        crr = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                crr.append(arr[i][j] + brr[i][j])
        return(crr)
    else:
        print('Error')

def ReadMx(arow, acol):
    matr = []
    for i in range(arow):
        matr.append([0 for j in range(acol)])
    for i in range(arow):
        for j in range(acol):
            matr[i][j] = int(input())
    return(matr)

def TranspMx(arr):
    t = arr
    if len(arr) == len(arr[0]):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                arr[i][j] = t[j][i]
        return(arr)
    else:
        print('Error')

def IsSymmetric(arr):
    if len(arr) == len(arr[0]):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j] != arr[j][i]:
                    s = False
                    break
            if s == False:
                break
            if i == n - 1:
                s = True
    else:
        print('Error')
    return(True)

def GetRow(arr, no):
    for i in range(len(arr[0])):
        print("%3d" % arr[no][i], end=" ")

def GetCol(arr, no):
    for i in range(len(arr)):
        print("%3d" % arr[i][no], end=" ")

def Pascal_triangle(k):
    arr = []
    for i in range(k):
        arr.append([0 for i in range(k)])
    for i in range(k):
        arr[i][i] = 1
        arr[i][0] = 1
    for i in range(k):
        for j in range(k):
            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
    return(arr)

def MultMx(arr, brr, srr):
    if len(arr) == len(brr) and len(arr[0]) == len(brr[0]):
        crr = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                crr.append(arr[i][j] * brr[i][j])
        return(srr)
    else:
        print('Error')

def CutXY(arr, x, y):
    del(arr[x])
    for i in range(len(arr)):
        del(arr[i][y])
    return(arr)

arr = RandomMatrix(5, 5)
PrintMx(arr)