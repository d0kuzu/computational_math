A = [
    [4, 2],
    [1, 3]
]

n = len(A)

B = [
    [0.25, -0.15],
    [-0.05, 0.35]
]

E = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            E[i][j] += A[i][k] * B[k][j]
        E[i][j] -= 1 if i == j else 0

S = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
power = [[E[i][j] for j in range(n)] for i in range(n)]

eps = 0.0001
max_iter = 50

for k in range(1, max_iter + 1):
    new_power = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for m in range(n):
                new_power[i][j] += power[i][m] * E[m][j]

    for i in range(n):
        for j in range(n):
            S[i][j] += new_power[i][j]

    max_val = max(max(abs(x) for x in row) for row in new_power)
    if max_val < eps:
        print(f"Сошлось за {k} итераций")
        break

    power = new_power

inv_A = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            inv_A[i][j] += B[i][k] * S[k][j]

print("Приближённая обратная матрица:")
for row in inv_A:
    print([round(x, 4) for x in row])