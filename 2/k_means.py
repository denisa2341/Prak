import numpy as np
import matplotlib.pyplot as plt
def k_means(k, data, centre , EPS):
	labels = get_labels(k ,data , centre)
	s = 0
	for i in range(k):
		mask = (labels-i) == 0
		if len(data[mask])>0:
			cen = sum(data[mask])/len(data[mask])
			s += np.linalg.norm(cen-centre[i])
			centre[i] = cen
	if (s>EPS):
		return k_means(k ,data ,centre ,EPS)
	else:
		return centre
def get_labels(k ,data , centre):
	dist = np.empty((len(data), k))
	for i in range(len(data)):
		dist[i] = np.linalg.norm(data[i]-centre,axis = 1)
	return np.argmin(dist , axis = 1)
"""d1 = np.random.random((1000,2))
d1 = d1*100
d1[:500 , :] += (100, 100)
d2 = np.random.random((2,2))
d2 *= 100
d2 =k_means(2, d1 , d2 , 0.0001)
plt.scatter(*d1.T, c=np.where(get_labels(2,d1,d2), "green", "red"), s=20)
plt.scatter(*d2.T, c=["red", "green"], s=95, marker='*')
plt.show()"""



