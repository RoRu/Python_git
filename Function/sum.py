def sum(x,y):
       
    if x > 0:
        s = sum(x - 1, y + 1)
        return(s)
    else:
        s = y
        return(s)


a = int(input())
b = int(input())
print(sum(a,b))   