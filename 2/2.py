import numpy as np
b = np.random.rand(6 , 6)
a = np.array([np.sum(b[i])/(np.min(b.T[i])) for i in range(6)])
print(a)