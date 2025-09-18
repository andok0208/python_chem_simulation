import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 12*np.pi, 100)
x = t*np.cos(t)
y = t*np.sin(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(x, y, z)
plt.show()

