func = lambda x: 1/(1 + x**2)
x0, xn = 0, 6
n = 6

h = (xn - x0) / n

summ1 = 0
summ2 = 0

for i in range(3, n, 3):
    summ1 += func(x0 + i*h)

for i in range(1, n, 3):
    summ2 += func(x0 + i*h)
    summ2 += func(x0 + (i+1)*h)

I = 3 * h/8 * (func(x0) + func(xn) + 2*summ1 + 3*summ2)
print(I)
