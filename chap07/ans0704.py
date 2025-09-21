import numpy as np
import matplotlib.pyplot as plt

nstep, nrun = 100, 20
for _ in range(nrun):
    x, y = 0.0, 0.0
    xx, yy = [], []
    for j in range(nstep):
        xx.append(x)
        yy.append(y)
        x += (np.random.random() - 0.5) * 2
        y += (np.random.random() - 0.5) * 2
    plt.plot(xx, yy)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

