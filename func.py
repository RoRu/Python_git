def phi(x):

    """posledovatelnost' Phibonachi"""

    if x == 1 or x == 2:
        b = 1
        return(b)
    else:	
        b = phi(x-1) + phi(x-2)
        return(b)
a = int(input())
print(phi(a))