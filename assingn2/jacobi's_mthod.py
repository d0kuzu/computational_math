a = [[2, 1, 1], [1, 3, -1], [-1, 1, 2]]
b = [6, 0, 3]

x = [0.0] * len(b)

eps = 0.001
max_iter = 1000

for iter in range(max_iter):
    new_x = [0.0] * len(b)
    for i in range(len(a)):
        sum_other = 0.0
        for j in range(len(a[i])):
            if j != i:
                sum_other += a[i][j] * x[j]
        new_x[i] = (b[i] - sum_other) / a[i][i]

    max_diff = 0.0
    for i in range(len(x)):
        diff = abs(new_x[i] - x[i])
        if diff > max_diff:
            max_diff = diff
    x = new_x[:]

    if max_diff < eps:
        print(f"Сошлось за {iter + 1} итераций")
        break

print(x)