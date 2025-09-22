import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 5000
xend, xmid = [], []
for _ in range(nrun):
    xx = rw1d(nstep)
    xend.append(xx[-1])
    xmid.append(xx[int(nstep/4)])

plt.hist(xmid, bins=50, rwidth=0.9, density=True, alpha=1.0)
plt.hist(xend, bins=50, rwidth=0.7, density=True, alpha=0.7)
plt.xlabel('position')
plt.ylabel('distribution')
plt.show()

