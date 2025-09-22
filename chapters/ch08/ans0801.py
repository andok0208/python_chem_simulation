import numpy as np
import matplotlib.pyplot as plt
from langevin import maruyama

m, gamma, kBT = 1.0, 1.0, 1.0
tmax, h = 100, 0.1
x0, v0 = 0.0, 0.0

nrun = int(input('Enter nrun: '))
for i in range(nrun):
    #v0 = np.random.normal() * np.sqrt(kBT/m)
    tt, xx, vv = maruyama(m, gamma, kBT, tmax, h, x0, v0)
    plt.plot(xx)
plt.xlabel('time')
plt.ylabel('position')
plt.show()

