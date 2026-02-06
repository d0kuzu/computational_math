def f(x, y):
    return y


def euler_method(x0, y0, h, x_n):
    x = x0
    y = y0

    n = int((x_n - x0) / h)

    for i in range(n):
        f_val = f(x, y)
        y_next = y + h * f_val

        y = y_next
        x = x + h

    print("-" * 45)
    print(f"Итоговый результат y({x_n}) ≈ {y:.4f}")
    return y


x_start = 0.0
y_start = 1.0
step = 0.1
target = 1.0

final_y = euler_method(x_start, y_start, step, target)