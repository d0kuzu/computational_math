def task(function, stop=0.001):
    if function(1) < 0:
        first = 1
        second = 2
    else:
        first = 2
        second = 1

    i = 1
    while True:
        print("iteration ", i)
        answer = (first + second)/2

        width = second - first
        print("first ", first, " second ", second)
        print("width ", width)
        if width < stop:
            return answer

        func_answer = function(answer)
        if func_answer < 0:
            first = answer
        else:
            second = answer
        print("function answer ", func_answer)
        print("\n")
        i+=1


f = lambda x: x**3 - x - 2
print("answer", round(task(f), 3))