import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

nstep = 100
x, y, z = 0.0, 0.0, 0.0
xx, yy, zz = [], [], []
for _ in range(nstep):
    xx.append(x)
    yy.append(y)
    zz.append(z)
    x += (np.random.random() - 0.5) * 2
    y += (np.random.random() - 0.5) * 2
    z += (np.random.random() - 0.5) * 2
ax.plot(xx, yy, zz)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

