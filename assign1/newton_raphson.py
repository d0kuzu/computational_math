def task(function, derr_function, x0: float, stop=0.001):
    last = x0

    i = 1
    while True:
        print(f"iteration {i}")
        answer = last - (function(last)/derr_function(last))
        if answer - last < stop:
            return answer
        last = answer

f = lambda x: x**3 - 2*x - 5
df = lambda x: 3*x**2 - 2
print(task(f, df, float(2), 2))
