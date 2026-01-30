func = lambda x: 1 / (1 + x**2)
x0, xn = 0, 6
n = 4

h = (xn - x0) / n

summ = 0

for i in range(n+1):
    yi = func(x0 + i*h)

    if i == 0 or i == n:
        summ += 7*yi
    elif i % 2 == 1:
        summ += 32*yi
    elif i % 4 == 2:
        summ += 12*yi
    else:
        summ += 14*yi

I = 2 * h/45 * summ

print(I)
