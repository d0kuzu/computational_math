def task(xs, ys, target_x):
    p = 0
    for i in range(len(xs)):
        L = 1
        for j in range(len(xs)):
            if i == j:
                continue
            L *= (target_x - xs[j])/(xs[i] - xs[j])
        p += y[i]*L
    return p


func = lambda a: 1/a
x = [ 1, 1.5, 4 ]
y = [ func(i) for i in x ]

print(task(x, y, 2))
print(abs(task(x, y, 2) - func(2)))
