def task(function, x0, x1, n=5):
    prelast = x0
    last = x1
    i = 0
    while True:
        fpl = function(prelast)
        fl = function(last)

        lastcont = last

        last = round(last - (fl*(last - prelast)/(fl - fpl)), 6)

        prelast = lastcont
        print("iteration ", i+1, " value ", last)
        if last == prelast:
            print(i, "iterations")
            break
        i+=1
    pass

f = lambda x: x**3 - 2*x - 5
task(f, 2, 3)