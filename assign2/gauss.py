a = [[1, 2, 1], [0, 2, 5], [3, 4, 1]]
b = [4, 6, 7]

# a = [[1, 2, 3], [2, 5, 2], [4, 1, -2]]
# b = [6, 4, -4]

for i in range(len(a)):
    for j in range(len(a)):
        if j > i:
            coef = a[j][i] / a[i][i]

            for k in range(len(a[j])):
                a[j][k] -= coef*a[i][k]
            b[j] -= coef*b[i]

for i in range(len(a)-1, -1, -1):
    num = b[i]
    for j in range(len(a[i])-1, -1, -1):
        if j > i:
            num -= a[i][j] * b[j]
    b[i] = num / a[i][i]

print(b)