import numpy as np
import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 5000
xend = []
xsq = np.zeros(nstep)
for _ in range(nrun):
    xx = rw1d(nstep)
    xend.append(xx[-1])
    xsq += xx**2
plt.hist(xend, bins=50, rwidth=0.9, density=True, label='simulation')

xmax = np.max(xend)
x = np.linspace(-xmax, xmax, 200)
sigma = np.sqrt(nstep/3)
f = 1/np.sqrt(2*np.pi)/sigma*np.exp(-0.5*(x/sigma)**2)
plt.plot(x, f, label='theory', lw=3)

plt.xlabel('position')
plt.ylabel('distribution')
plt.legend()
plt.show()

plt.plot(xsq/nrun, label='simulation', lw=2)
plt.plot(np.arange(nstep-1)/3, '--', label='theory', lw=2)
plt.xlabel('step')
plt.ylabel('mean square displacement')
plt.legend()
plt.show()

