import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 101)
plt.plot(x, np.exp(x))
plt.plot(x, np.exp(-x))
plt.plot(x, x*0, '--')
plt.plot([0,0], [-1,8], '--')
plt.show()

