import numpy as np

data = np.arange(1, 100)

print(data[(data % 3 == 0) & (data % 5 == 0)])
