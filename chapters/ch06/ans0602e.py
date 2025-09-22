import numpy as np
import matplotlib.pyplot as plt
from ratelib import brussel_euler

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

A, B = 1, 3
tmax, h = 30, 0.01

z0 = 0
for (x0, y0) in [(1.5, 3), (3, 4), (1, 1)]:
    tt, xx, yy = brussel_euler(A, B, tmax, h, x0, y0)
    z0 += 1.0
    zz = z0 * np.ones(len(tt))
    ax.plot(xx, yy, zz, label=f'X$_0$={x0}, Y$_0$={y0}')
plt.title(f'A={A}, B={B}')
plt.xlabel('[X]')
plt.ylabel('[Y]')
plt.show()

