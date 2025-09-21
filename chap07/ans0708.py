import numpy as np
import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep = 100
for nrun in [100, 1000, 10000]:
    xsq = np.zeros(nstep)
    for _ in range(nrun):
        xx = rw1d(nstep)
        xsq += xx**2
    plt.plot(xsq/nrun, label=f'nrun={nrun}')
plt.xlabel('step')
plt.ylabel('mean square displacement')
plt.legend()
plt.show()

