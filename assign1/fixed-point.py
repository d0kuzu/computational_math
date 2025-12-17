def task(function, g, stop=0.001):
    # if function(1) < 0:
    #     first = 1
    #     second = 2
    # else:
    #     first = 2
    #     second = 1
    last = (1 + 2) / 2  # (first + second) / 2

    i = 1
    while True:
        current = g(last)
        print(f"iteration {i}: {current}")

        if current - last < stop:
            return current

        last = current
        i+=1

f = lambda x: x**3 - x - 2
g = lambda x: (x+2)**(1/3)
print(round(task(f, g), 3))