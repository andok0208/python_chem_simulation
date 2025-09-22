import numpy as np
import matplotlib.pyplot as plt

m, eb, d = 1.0, 6.0, 1.0

def pot(x):
    return eb*((x/d)**2 - 1)**2

xx = np.linspace(-1.6, 1.6, 100)
plt.plot(xx, pot(xx), label='V(x)')
plt.xlabel('x')
plt.ylabel('V(x)')
plt.legend()
plt.show()

