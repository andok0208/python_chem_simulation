import numpy as np
import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 5000
trj = []
for _ in range(nrun):
    xx = rw1d(nstep)
    trj.append(xx)
trj = np.array(trj)
print(trj.shape)
plt.hist(trj[:,10], bins=50, rwidth=0.9, density=True, alpha=1.0)
plt.hist(trj[:,30], bins=50, rwidth=0.7, density=True, alpha=0.8)
plt.hist(trj[:,-1], bins=50, rwidth=0.5, density=True, alpha=0.7)
plt.xlabel('position')
plt.ylabel('distribution')
plt.show()

