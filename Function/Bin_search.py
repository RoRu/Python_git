arr = str(input("Enter array: ")).split(" ")
for i, item in enumerate(arr):
    arr[i] = int(item)
arr.sort()

search = int(input("Enter number: "))

start = 0
end = len(arr)
mid = int((start+end)/2)

while start != end:
    if(search > arr[mid]):
        start = mid+1
        mid = int((start+end)/2)
        continue
    if(search < arr[mid]):
        end = mid
        mid = int((start+end)/2)
        continue
    if(search == arr[mid]):
        print(mid)
        break

print(arr)