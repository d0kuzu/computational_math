import math

func = lambda x: math.log(x)
x0, xn = 4, 5.2
n = 6

h = (xn - x0) / n

summ = 0

for i in range(n+1):
    yi = func(x0 + i*h)

    if i == 0 or i == n:
        summ += yi
    elif i % 6 == 3:
        summ += 6*yi
    elif i % 2 == 1:
        summ += 5*yi
    else:
        summ += yi

I = 3 * h/10 * summ

print(I)
