import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure()

nstep = int(input('Enter number of steps: '))
x = 0.0
xx, ims = [], []
for _ in range(nstep):
    xx.append(x)
    x += (np.random.random() - 0.5) * 2
    im = plt.plot(xx, color='b')
    ims.append(im)
ani = animation.ArtistAnimation(fig, ims, interval=50)
plt.show()

