import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 101)
print(x)
y = x**2
plt.plot(x, y)
plt.show()
x = np.linspace(0, 2*np.pi, 40)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.plot(x, 0*x, '--')
#plt.plot(x, 0*x, '-.')  # 演習3-4
#plt.plot(x, 0*x, ':')
plt.show()

