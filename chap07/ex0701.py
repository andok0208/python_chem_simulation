import numpy as np
import matplotlib.pyplot as plt

nstep = 100
x = 0.0
xx = []
for _ in range(nstep):
    xx.append(x)
    x += (np.random.random() - 0.5) * 2
plt.plot(xx)
plt.xlabel('step')
plt.ylabel('position')
plt.show()

