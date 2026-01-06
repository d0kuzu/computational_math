a = [[1,1,1], [2,-3,4], [3,4,5]]
b = [9, 13, 40]

for i in range(len(a)):
    row = a[i].copy()
    rowB = b[i]
    pivot = a[i][i]

    if pivot != 1:
        for j in range(len(row)):
            row[j] /= pivot
        rowB /= pivot

        b[i] = rowB
        a[i] = row

    for j in range(len(a)):
        if j != i:
            coef = a[j][i]
            for k in range(len(a[j])):
                a[j][k] = a[j][k] - coef * row[k]
            b[j] = b[j] - coef * rowB
print(a)
print(b)