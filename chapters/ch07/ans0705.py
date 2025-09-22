import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 20
for _ in range(nrun):
    plt.plot(rw1d(nstep))
plt.xlabel('step')
plt.ylabel('position')
plt.show()

