import numpy as np
import matplotlib.pyplot as plt


def pot(x):
    return eb*((x/d)**2 - 1)**2


def force(x):
    return -4*eb*((x/d)**2 - 1)*x/d**2


m, eb, d = 1.0, 6.0, 1.0
tmax, h = 50.0, 0.01
x0, v0 = 1.6, 0.0
t, x, v = 0.0, x0, v0

#gamma, kBT = 0.01, 1.0
gamma = float(input('Enter gamma : '))
kBT   = float(input('Enter kBT   : '))

nstep = int(tmax/h)+1
tt = np.empty(nstep)
xx = np.empty(nstep)
vv = np.empty(nstep)
for i in range(nstep):
    tt[i], xx[i], vv[i] = t, x, v
    t += h
    x += v * h * 0.5
    v += force(x) / m * h
    v += - gamma / m * v * h
    v += np.sqrt(2 * kBT * gamma * h) * np.random.normal() / m
    x += v * h * 0.5
tt, xx, vv = map(np.array, (tt, xx, vv))

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

