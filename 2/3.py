import numpy as np
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
a = np.max(x[(np.argwhere(x[:-1] == 0) + 1)])
print(a)