import numpy as np
import matplotlib.pyplot as plt
from ratelib import lotka_euler

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

pq = 1.0, 1.0, 1.0, 1.0
tmax, h = 20, 0.01

c0 = 0
for (a0, b0) in [(2.0, 1.0), (1.0, 3.0), (3.0, 2.0)]:
    tt, aa, bb = lotka_euler(pq, tmax, h, a0, b0)
    c0 += 1
    cc = c0 * np.ones(len(tt))
    ax.plot(aa, bb, cc, label=f'A$_0$={a0}, B$_0$={b0}')

plt.xlabel('A (prey)')
plt.ylabel('B (predator)')
plt.show()

