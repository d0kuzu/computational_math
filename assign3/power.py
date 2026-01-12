A = [
    [4, 1, 0],
    [1, 3, 1],
    [0, 1, 2]
]

n = len(A)

x = [1.0, 1.0, 1.0]

eps = 0.0001
max_iter = 100
prev_lambda = 0.0

print("Итерации степенного метода:")

for k in range(max_iter):
    y = [0.0] * n
    for i in range(n):
        for j in range(n):
            y[i] += A[i][j] * x[j]

    lambda_new = 0.0
    for i in range(n):
        if abs(x[i]) > 1e-10:
            lambda_new = y[i] / x[i]
            break

    norm = 0.0
    for val in y:
        norm += val * val
    norm = norm ** 0.5

    if norm < 1e-12:
        print("Вектор стал нулевым — ошибка")
        break

    for i in range(n):
        x[i] = y[i] / norm

    print(f"Итерация {k + 1:2d} | λ ≈ {lambda_new:10.6f} | вектор: {[round(v, 4) for v in x]}")

    if abs(lambda_new - prev_lambda) < eps:
        print(f"\nСошлось за {k + 1} итераций")
        break

    prev_lambda = lambda_new

print(f"\nλ: {lambda_new:.6f}")
print("вектор (нормированный):", [round(v, 6) for v in x])