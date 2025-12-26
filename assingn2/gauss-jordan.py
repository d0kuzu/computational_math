def determinant(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        return -1

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0.0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        sign = 1 if j % 2 == 0 else -1
        det += sign * matrix[0][j] * determinant(minor)

    return det

a = [[1,1,1], [2,-3,4], [3,4,5]]
b = [9, 13, 40]

for i in range(len(a)):
    for j in range(len(a[i])):


