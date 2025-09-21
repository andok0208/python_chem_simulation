import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 5000
xend = []
for _ in range(nrun):
    xx = rw1d(nstep)
    xend.append(xx[-1])

plt.hist(xend, bins=50, rwidth=0.9)
plt.xlabel('position')
plt.ylabel('distribution')
plt.show()

