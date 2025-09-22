import numpy as np
import matplotlib.pyplot as plt


def brownian(nstep, h, x0, v0):
    t, x, v = 0.0, x0, v0
    tt = np.empty(nstep)
    xx = np.empty(nstep)
    vv = np.empty(nstep)
    for i in range(nstep):
        tt[i], xx[i], vv[i] = t, x, v
        t += h
        x += v * h * 0.5
        v += force(x) / m * h
        v += - gamma / m * v * h
        v += np.sqrt(2 * kBT * gamma * h) \
           * np.random.normal() / m
        x += v * h * 0.5
    return tt, xx, vv


def pot(x):
    return eb*((x/d)**2 - 1)**2


def force(x):
    return -4*eb*((x/d)**2 - 1)*x/d**2


m, eb, d = 1.0, 6.0, 1.0
gamma, kBT = 0.1, 4.0
tmax, h = 50.0, 0.01
nstep = int(tmax/h)+1
x0, v0 = 0.0, 0.0
nrun = 2000
xend = []
for _ in range(nrun):
    tt, xx, vv = brownian(nstep, h, x0, v0)
    xend.append(xx[-1])

plt.hist(xend, bins=50, rwidth=0.9, density=True)

xmax = np.max(xend)
ngrid = 200
x = np.linspace(-xmax, xmax, ngrid)
f = np.exp(-pot(x)/kBT)
dx = x[1] - x[0]
f = f / (np.sum(f)*dx)
plt.plot(x, f, lw=3, label='Eq.(10.3)')

plt.xlabel('x')
plt.ylabel('distribution')
plt.legend()
plt.show()

