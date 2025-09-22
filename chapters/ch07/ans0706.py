import matplotlib.pyplot as plt
from randomwalk import rw1d

nstep, nrun = 100, 20
for _ in range(nrun):
    xx = rw1d(nstep)
    yy = rw1d(nstep)
    plt.plot(xx, yy)
plt.xlabel('step')
plt.ylabel('position')
plt.show()

# 別解
for _ in range(nrun):
    plt.plot(rw1d(nstep), rw1d(nstep))  
plt.xlabel('step')
plt.ylabel('position')
plt.show()

