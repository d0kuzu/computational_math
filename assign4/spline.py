x = [
    2010,
    2015,
    2020,
    2025
]
y = [
    16.5,
    17.5,
    18.7,
    20.0
]
target_x = 2018

idx = 0
for i in range(len(x) - 1):
    if x[i] <= target_x <= x[i+1]:
        idx = i
        break

x0, x1 = x[idx], x[idx+1]
y0, y1 = y[idx], y[idx+1]

px = y0 + (target_x - x0) * (y1 - y0) / (x1 - x0)

print(f"Результат для {target_x}: {round(px, 3)}")