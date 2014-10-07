def RandomMatrix(trow, tcol):
    import random
    arr = []
    for i in range(trow):
        arr.append([random.randint(0, 50) for j in range(tcol)])
    return(arr)

def SumMx(arr, brr, srr):
    if len(arr) == len(brr) and len(arr[0]) == len(brr[0]):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                srr[i][j] = arr[i][j] + brr[i][j]
        return(srr)
    else:
        print('Error')

def PrintMx(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print('%3d' % arr[i][j], end=" ")
        print()

def TranspMx(arr):
    t = arr
    if len(arr) == len(arr[0]):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                arr[i][j] = t[j][i]
        return(arr)
    else:
        print('Error')

arr = []
brr = []
crr = []
arr = RandomMatrix(5, 5)
brr = RandomMatrix(5, 5)
crr = RandomMatrix(5, 5)
PrintMx(arr)
print()
PrintMx(brr)
print()
crr = SumMx(arr, brr, crr)
PrintMx(crr)