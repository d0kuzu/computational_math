def f(x, y):
    return x + y


def picard_method(x0, y0, x_target, n_iterations, steps=1000):
    dx = (x_target - x0) / steps
    x_grid = [x0 + i * dx for i in range(steps + 1)]

    phi_prev = [y0] * (steps + 1)

    for n in range(1, n_iterations + 1):
        phi_next = [y0]

        current_integral = 0.0

        for i in range(1, steps + 1):
            f_prev_point = f(x_grid[i - 1], phi_prev[i - 1])
            f_curr_point = f(x_grid[i], phi_prev[i])

            current_integral += (f_prev_point + f_curr_point) * 0.5 * dx

            phi_next.append(y0 + current_integral)

        phi_prev = list(phi_next)

    return phi_prev[-1]


result = picard_method(x0=0, y0=1, x_target=1.0, n_iterations=3)
print(result)