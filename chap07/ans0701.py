import numpy as np
import matplotlib.pyplot as plt

nstep = 100
x, y = 0.0, 0.0
xx, yy = [], []
for _ in range(nstep):
    xx.append(x)
    yy.append(y)
    x += (np.random.random() - 0.5) * 2
    y += (np.random.random() - 0.5) * 2
plt.plot(xx, yy)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

