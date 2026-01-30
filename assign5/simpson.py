import math

func = lambda x: math.sqrt(x)
x0, xn = 0, 8
n = 4

h = (xn - x0) / n

summ1 = 0
summ2 = 0

for i in range(1, n, 2):
    summ1 += func(x0 + i*h)

for i in range(2, n, 2):
    summ2 += func(x0 + i*h)

I = h/3 * (func(x0) + 4*summ1 + 2*summ2 + func(xn))
print(I)
