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

a = input("Enter array: ").split()
a = [int(a[i]) for i in range(0, len(a))]
print(a)
n = int(input("Enter searching number: "))
print(BinSearch(a, n))