def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def taylor_series_method(x0, y0, x_target, n_terms):
    y_prime = x0 + y0

    y_double_prime = 1 + y_prime

    y_triple_prime = y_double_prime

    y_fourth_prime = y_triple_prime

    derivatives = [y0, y_prime, y_double_prime, y_triple_prime, y_fourth_prime]

    result = 0
    h = x_target - x0

    for i in range(min(len(derivatives), n_terms)):
        term = (derivatives[i] / factorial(i)) * (h ** i)
        result += term

    return result


x0, y0 = 0, 1
x_star = 1.0
n = 5

final_val = taylor_series_method(x0, y0, x_star, n)

print(f"\nПриближенное значение y({x_star}) ≈ {final_val:.6f}")