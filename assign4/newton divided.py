x = [
    300,
    304,
    305,
    307
]
target_x = 301

y = [
    2.4771,
    2.4829,
    2.4843,
    2.4871
]

dy = [y.copy()]

for j in range(len(x), 1, -1):
    dy.append([])
    for i in range(1, j):
        # print(dy[-2][-i])
        # print(dy[-2][-(i+1)])
        # print("_")
        # print(x[-i])
        # print(x[-(i+len(dy)-1)])
        # print(i)
        # print(len(dy))
        dy[-1].append(round((dy[-2][-i] - dy[-2][-(i+1)])/(x[-i]-x[-(i+len(dy)-1)]), 4))
    print("____")
[print(row) for row in dy]

px = dy[0][0]
for i in range(1, len(dy)):
    coef = 1
    for j in range(i):
        coef *= target_x - x[j]

    px += coef*dy[i][0]
print(px)
