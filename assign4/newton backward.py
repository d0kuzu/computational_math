x = [
    2010,
    2015,
    2020,
    2025
]
target_x = 2023
h = [i-x[0] for i in x][1]

y = [
    16.5,
    17.5,
    18.7,
    20.0
]

dy = [y.copy()]

for j in range(len(x), 1, -1):
    dy.append([])
    for i in range(j-1):
        dy[-1].append(round(dy[-2][i+1] - dy[-2][i], 1))
[print(row) for row in dy]

u = (target_x-x[-1])/h

px = dy[0][-1]
for i in range(1, len(dy)):
    numerator = 1
    for j in range(i):
        numerator *= u+j

    denominator = 1
    for j in range(2, i+1):
        denominator *= j

    px += (numerator/denominator)*dy[i][-1]
print(px)
