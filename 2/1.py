import numpy as np
b = np.random.rand(10 , 3)
a = np.array([b[i][(np.abs(b[i]-0.5)).argmin()] for i in range(10)])
