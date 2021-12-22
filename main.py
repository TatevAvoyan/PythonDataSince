import numpy as np

data = np.array([120, 98, 150, 65, 42, 100, 190, 220, 140, 110, 88, 89, 100, 120, 50, 180, 155, 42, 89, 77, 200, 190, 125, 98, 77, 40, 39, 59, 30, 67])

mean = np.mean(data)
new = np.array([])

for i in data:
    if mean < i:
        new = np.append(new, i)

print(new.size)
