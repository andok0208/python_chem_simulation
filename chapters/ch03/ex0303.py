import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

t = np.linspace(0, 12*np.pi, 100)
x = t*np.cos(t)
y = t*np.sin(t)
z = t

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ims = []
for i in range(len(t)):
    ims.append(ax.plot(x[:i], y[:i], z[:i], color='b'))

ani = animation.ArtistAnimation(fig, ims, interval=1)
plt.show()

