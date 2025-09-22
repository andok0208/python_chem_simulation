import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 100000
xend, yend = [], []
for _ in range(nrun):
    xx = rw1d(nstep)
    yy = rw1d(nstep)
    xend.append(xx[-1])
    yend.append(yy[-1])

plt.hist2d(xend, yend, bins=[100,100], density=True, cmap=plt.cm.jet)
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

