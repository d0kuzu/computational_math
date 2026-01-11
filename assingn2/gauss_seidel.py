a = [[3, -1, 2], [1, 4, -1], [2, 1, 5]]
b = [7, 8, 9]

x = [0.0] * len(b)

eps = 0.001
max_iter = 1000

for iter in range(max_iter):
    old_x = x[:]
    for i in range(len(a)):
        sum_other = 0.0
        for j in range(len(a[i])):
            if j != i:
                sum_other += a[i][j] * x[j]
        x[i] = (b[i] - sum_other) / a[i][i]

    max_diff = 0.0
    for i in range(len(x)):
        diff = abs(x[i] - old_x[i])
        if diff > max_diff:
            max_diff = diff

    if max_diff < eps:
        print(f"Сошлось за {iter + 1} итераций")
        break

print(x)