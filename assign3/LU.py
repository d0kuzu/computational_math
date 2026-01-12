A = [
    [2, 1, 1],
    [4, -6, 0],
    [-2, 7, 2]
]

n = len(A)

matrix = [row[:] for row in A]

for i in range(n):
    for j in range(i + 1, n):
        factor = matrix[j][i] / matrix[i][i]

        matrix[j][i] = factor

        for k in range(i, n):
            matrix[j][k] -= factor * matrix[i][k]


def get_L_and_U(matrix, n):
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i > j:
                L[i][j] = matrix[i][j]
            elif i == j:
                L[i][j] = 1.0
                U[i][j] = matrix[i][j]
            else:
                U[i][j] = matrix[i][j]

    return L, U


L, U = get_L_and_U(matrix, n)

print("A:")
for row in matrix:
    print([round(x, 4) for x in row])

print("\nL:")
for row in L:
    print([round(x, 4) for x in row])

print("\nU:")
for row in U:
    print([round(x, 4) for x in row])