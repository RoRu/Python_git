def submatrix(matr, i, j):
    result = []
    k = 0
    l = 0
    m = 0
    n = 0

    for k in range(len(matr)):
        if k == i:
            l -= 1
        else:
            n = 0
            for m in range(len(matr)):
                if m == j:
                    n -= 1
                else:
                    result[l][n] = matr[k][m]
                n += 1
        l += 1
    return(result)

    def minor(matr, i, j):
        return(det(submatrix(matr, i, j)))

    def det(matr):
        if len(matr) == 2:
            return(matr[0][0] * matr[1][1] - matr[0][1] * matr[1][0])
        else:
            result = 0
            for j in range(len(matr)):
                result += (-1 ** j) * matr[0][j] * minor(matr, 0, j)
        return(result)