import matplotlib.pyplot as plt
from ratelib import brussel_euler

A, B = 1, 3

x0, y0 = 1, 1
tmax, h = 30, 0.01

tt, xx, yy = brussel_euler(A, B, tmax, h, x0, y0)
plt.plot(tt, xx, label='[X]')
plt.plot(tt, yy, label='[Y]')
plt.title(f'X$_0$=Y$_0$={x0}, A={A}, B={B}')
plt.xlabel('time')
plt.ylabel('[X], [Y]')
plt.legend()
plt.show()

plt.plot(xx, yy, label=f'X$_0$={x0}, Y$_0$={y0}')
plt.title(f'A={A}, B={B}')
plt.xlabel('[X]')
plt.ylabel('[Y]')
plt.legend()
plt.show()

