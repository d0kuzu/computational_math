import math

func = lambda x: math.sin(x)
x0, xn = 0, math.pi/2
n = 10  # должно быть четное для Симпсона

h = (xn - x0) / n

summ = func(x0) + func(xn)

for i in range(1, n):
    if i % 2 == 0:
        summ += 2 * func(x0 + i * h)
    else:
        summ += 4 * func(x0 + i * h)

area = h/3 * summ
print(area)
