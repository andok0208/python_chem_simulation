import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

nstep = int(input('Enter number of steps: '))
x, y = 0.0, 0.0
xx, yy, ims = [], [], []
for _ in range(nstep):
    xx.append(x)
    yy.append(y)
    x += (np.random.random() - 0.5) * 2
    y += (np.random.random() - 0.5) * 2
    im = plt.plot(xx, yy, color = 'b')
    ims.append(im)
ani = animation.ArtistAnimation(fig,ims,interval=100)
plt.show()

