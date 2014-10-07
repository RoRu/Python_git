n = int(input('Enter number of friends: '))
s = []
arr = []
for i in range(0, n):
    s.append(input('Enter codes: '))
for i in range(1, n):
    noms = []
    for j in range(len(s[1])):
        if s[0][j] == s[i][j]:
            noms.append(s[0][j])
        else:
            break
    arr.append(''.join(noms))
min = len(arr[0])
for i in range(1, len(arr)):
    if len(arr[i]) < min:
        min = len(arr[i])
print(min)