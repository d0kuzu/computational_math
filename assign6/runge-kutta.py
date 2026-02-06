def f(x, y):
    return x ** 2 + y ** 2


def runge_kutta_4(x0, y0, h, x_target):
    x = x0
    y = y0
    steps = int((x_target - x0) / h)

    print(f"Начальные условия: x0={x0}, y0={y0}, h={h}\n")

    for i in range(steps):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        y = y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h

    return y


result_rk4 = runge_kutta_4(1, 1.2, 0.05, 1.05)
print(f"\nИтог RK4: y(1.05) ≈ {result_rk4:.4f}")