func = lambda x: 1 / (1 + x**2)
x0, xn = 0, 6
n = 4  # строго 4

h = (xn - x0) / n

I = 2*h/45 * (
    7*func(x0)
    + 32*func(x0 + h)
    + 12*func(x0 + 2*h)
    + 32*func(x0 + 3*h)
    + 7*func(xn)
)

print(I)
