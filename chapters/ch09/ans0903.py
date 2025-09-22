import matplotlib.pyplot as plt
from oscillator import leapfrog

k, m = 1.0, 1.0
tmax, h = 30, 0.1
x0, v0 = 1.0, 0.0
tt, xx, vv = leapfrog(k, m, tmax, h, x0, v0)

plt.plot(tt, xx, label='x')
plt.plot(tt, vv, label='v')
plt.xlabel('t')
plt.ylabel('x, v')
plt.legend()
plt.show()

plt.plot(xx, vv, label='x-v')
plt.xlabel('x')
plt.ylabel('v')
plt.legend()
plt.show()

ke, pe = 0.5*m*vv**2, 0.5*k*xx**2
plt.plot(tt, ke, label='ke')
plt.plot(tt, pe, label='pe')
plt.plot(tt, ke+pe, label='ke+pe')

plt.xlabel('t')
plt.ylabel('energy')
plt.legend()
plt.show()

