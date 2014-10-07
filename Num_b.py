arr = []
flag = ''
a = int(input())
b = int(input())
m = int(input())
r0 = int(input())
arr.append(r0)
i = 0
while True:
    i += 1
    arr.append((arr[i - 1] * a + b) % m)
    for j in range(len(arr) - 1):
        if arr[i] == arr[j]:
            print(i - j)
            flag = 'break'
            break
    if flag == 'break':
        break