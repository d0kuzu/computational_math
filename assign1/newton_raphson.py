def task(function, derr_function, x0: float, k):
    last = x0
    for i in range(k+1):
        last = last - (function(last)/derr_function(last))
    return last

f = lambda x: x**3 - 2*x - 5
df = lambda x: 3*x**2 - 2
print(task(f, df, float(2), 2))
