import math

A = [
    [4, 1, 0],
    [1, 3, 1],
    [0, 1, 2]
]

n = len(A)

V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

eps = 1e-9
max_iter = 1000

for iter in range(max_iter):
    max_val = 0.0
    p, q = 0, 1

    for i in range(n):
        for j in range(i + 1, n):
            if abs(A[i][j]) > max_val:
                max_val = abs(A[i][j])
                p, q = i, j

    if max_val < eps:
        print(f"Сошлось за {iter} итераций")
        break

    tau = (A[q][q] - A[p][p]) / (2 * A[p][q])
    t = 1.0 / (abs(tau) + math.sqrt(1 + tau * tau))
    if tau < 0:
        t = -t

    c = 1.0 / math.sqrt(1 + t * t)
    s = t * c

    for i in range(n):
        if i != p and i != q:
            api = A[p][i]
            aqi = A[q][i]
            A[p][i] = A[i][p] = c * api - s * aqi
            A[q][i] = A[i][q] = s * api + c * aqi

    app = A[p][p]
    aqq = A[q][q]
    apq = A[p][q]

    A[p][p] = c * c * app - 2 * s * c * apq + s * s * aqq
    A[q][q] = s * s * app + 2 * s * c * apq + c * c * aqq
    A[p][q] = A[q][p] = 0.0

    for i in range(n):
        vpi = V[i][p]
        vqi = V[i][q]
        V[i][p] = c * vpi - s * vqi
        V[i][q] = s * vpi + c * vqi

print("\nдиагональ A:")
for i in range(n):
    print(f"λ[{i}] ≈ {A[i][i]:12.6f}")

for i in range(n):
    print(f"Вектор для λ[{i}]: {[round(V[j][i], 6) for j in range(n)]}")