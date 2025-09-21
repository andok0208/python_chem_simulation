import numpy as np
import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 3000
xsq = np.zeros(nstep)
for _ in range(nrun):
    xx = rw1d(nstep)
    xsq += xx**2
plt.plot(xsq/nrun)
plt.xlabel('step')
plt.ylabel('mean square displacement')
plt.show()

