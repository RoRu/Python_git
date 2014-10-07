def GenerateArr(n, arr):
    from random import randint
    arr = []
    arr.extend([randint(0, 100) for i in range(0, n)])
    return(arr)

def InputArr(arr):
    arr = []
    arr = input("Enter array: ").split()
    arr = [int(i) for i in arr]
    return(arr)

def Average(arr):
    aver = sum(arr) / len(arr)
    return(aver)

def Median(arr):
    arr.sort()
    if n % 2 == 0:
        med = arr[len(arr) // 2] + arr[-1]
    else:
        med = arr[len(arr) // 2]
    return(med)

def BinSearch(arr, x):
    arr.sort()
    right = len(arr)
    left = 0
    middle = right // 2
    
    while left != right:
        if x > arr[middle]:
            left = middle + 1
            middle = (left + right)//2
            continue
        if x < arr[middle]:
            right = middle
            middle = (right + left)//2
            continue
        if x == arr[middle]:
            return(middle)
            break


d = int(input("Number of elms in array: "))
a = []
GenerateArr(d, a)
print(a)
num = 0
while True:
    print('1: Generate Array\n'
            '2: Print array\n' 
            '3: sort array\n' 
            '4: max elm in array\n' 
            '5: min elm in array\n' 
            '6: sum of elms\n' 
            '7: Array Average\n' 
            '8: Array Median\n' 
            '9: Create array by myself\n'
            '10: Exit')
    num = int(input('What to do: '))
    if num == 1:
        a = GenerateArr(d, a)
    elif num == 2:
        print(a)
    elif num == 3:
        a.sort()
    elif num == 4:
        print(max(a))
    elif num == 5:
        print(min(a))
    elif num == 6:
        print(sum(a))
    elif num == 7:
        print('\n', Average(a), '\n', sep='')
    elif num == 8:
        print(Median(a))
    elif num == 9:
        InputArr(a)
    else:
        break