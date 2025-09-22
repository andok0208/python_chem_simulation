import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

nstep = int(input('Enter number of steps: '))
x, y, z = 0.0, 0.0, 0.0
xx, yy, zz, ims = [], [], [], []
for _ in range(nstep):
    x += (np.random.random() - 0.5) * 2
    y += (np.random.random() - 0.5) * 2
    z += (np.random.random() - 0.5) * 2
    xx.append(x)
    yy.append(y)
    zz.append(z)
    im = ax.plot(xx, yy, zz, color = 'b')
    ims.append(im)
ani = animation.ArtistAnimation(fig,ims,interval=100)
plt.show()

