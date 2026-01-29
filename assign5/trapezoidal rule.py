import math

func = lambda x: math.sin(x)
x0, xn = 0, math.pi/2
n = 10

h = (xn - x0)/n

summ = 0
for i in range(1, n):
    summ += func(x0 + i * h)

area = h/2 * (func(x0) + summ*2 + func(xn))

print(area)
