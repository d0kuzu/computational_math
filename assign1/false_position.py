import math


def task(func, stop=0.001):
    a = 0
    b = 0
    step = 1
    while not func(a) * func(a+step) < 0:
        a += step
    b = a + step


    i = 1
    while True:
        print(f"a: {a} b: {b}")
        answer = round((a * func(b) - b * func(a))/(func(b) - func(a)), 5)
        print(f"iteration {i}: {answer}")
        print(f"func of: {round(func(answer), 5)}")
        print("")

        if abs(func(answer)) < stop:
            return answer

        if answer < 0:
            a = answer
        else:
            b = answer
        i += 1

function = lambda x: 2 * math.e**x * math.sin(x) - 3
print(round(task(function), 3))