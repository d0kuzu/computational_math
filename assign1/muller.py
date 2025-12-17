import math

def task(func, stop=0.001):
    a = 0
    step = 1
    while func(a)*func(a+step) > 0:
        a += step
    c = a + step
    b = (a + c)/2

    i = 0
    while True:
        print(f"iteration {i}")
        h1 = b - a
        h2 = c - b

        q1 = (func(b) - func(a)) / h1
        q2 = (func(c) - func(b)) / h2

        d = (q2 - q1) / (h2 + h1)
        b = q2 + h2 * d

        denom1 = b + math.sqrt(b**2 - 4 * func(c) * d)
        denom2 = b - math.sqrt(b**2 - 4 * func(c) * d)
        denom = denom1 if abs(denom1) > abs(denom2) else denom2

        answer = c - (2 * func(c)) / denom

        if abs(answer - c) < stop:
            return answer

        a = b
        b = c
        c = answer

        i += 1

function = lambda x: math.cos(x) - x * math.e**x
print(round(task(function), 3))
