def f(x, y):
    return y


def modified_euler_table(x0, y0, h, x_target):
    x = x0
    y = y0

    steps = int((x_target - x0) / h)

    for n in range(steps):
        y_p = y + h * f(x, y)

        y_next = y + (h / 2.0) * (f(x, y) + f(x + h, y_p))

        x = x + h
        y = y_next

    return y


result = modified_euler_table(x0=0.0, y0=1.0, h=0.1, x_target=1.0)
print(f"\nИтог в точке x=1.0: {result:.4f}")