def BinSearch(arr, x):
    start = 0
    finish = len(arr) - 1
    if start == finish:
        if x == arr[start]:
            res = start
        else:
            res = -1
    elif finish - start == 1:
        if x == arr[start]:
            res = start
        elif x == arr[finish]:
            res = finish
        else:
            res = -1
    else:
        right = finish
        left = start
        middle = left + ((right - left) // 2)
        if x > arr[middle]:
            left = middle
        elif x < arr[right]:
            right = middle
        res = BinSearch(arr, x)
    return(res)

a = input('Enter array: ').split()
a = [int(a[i]) for i in range(0, len(a))]
a.sort()
x = int(input('search this number:'))
print(BinSearch(a, x))