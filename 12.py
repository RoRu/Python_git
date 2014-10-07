#number 3
st = input()
arr = []
add = []
arr = st.split(" ")
for i in range(len(arr)):
    add.append(len(arr[i]))
ma = add.index(max(add))
print(arr[ma])
mi = add.index(min(add))
print(arr[mi])