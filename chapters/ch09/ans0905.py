import numpy as np
import matplotlib.pyplot as plt

m, eb, d = 1.0, 6.0, 1.0

def pot(x):
    return eb*((x/d)**2 - 1)**2

def force(x):
    return -4*eb*((x/d)**2 - 1)*x/d**2

tmax, h = 5.0, 0.01
t, x, v = 0.0, 1.6, 0.0

nstep = int(tmax/h)+1
tt = np.empty(nstep)
xx = np.empty(nstep)
vv = np.empty(nstep)
for i in range(nstep):
    tt[i], xx[i], vv[i] = t, x, v
    t += h
    x += v * h * 0.5
    v += force(x) / m * h
    x += v * h * 0.5

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

ke, pe = 0.5*m*vv**2, pot(xx)
plt.plot(tt, ke, label='ke')
plt.plot(tt, pe, label='pe')
plt.plot(tt, ke+pe, label='ke+pe')
plt.xlabel('t')
plt.ylabel('energy')
plt.legend()
plt.show()

