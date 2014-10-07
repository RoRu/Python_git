#number 2
st = input()
arr = []
st = st + " "
arr = list(st)
i = 0
for i in range(len(arr) - 2):
    if arr[i] == " " and arr[i + 2] == " ":
        print(i)
        arr[i + 1] = " "
st = "".join(arr)
print(st)