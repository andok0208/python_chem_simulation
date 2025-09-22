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
gamma, kBT = 1.0, 4.0
tmax, h = 20.0, 0.1
nstep = int(tmax/h)+1

nrun = 5000
trj = np.empty((nstep, nrun))
x0, v0 = -d, 0.0
for i in range(nrun):
    tt, xx, vv = brownian(nstep, h, x0, v0)
    trj[:, i] = xx

xmax = np.max(np.abs(trj))
ngrid = 200
x = np.linspace(-xmax, xmax, ngrid)
f = np.exp(-pot(x)/kBT)
dx = x[1] - x[0]
f = f / (np.sum(f)*dx)

i1, i2, i3 = int(nstep/40), int(nstep/10), nstep-1
plt.hist(trj[i1,:], bins=50, rwidth=0.9, alpha=1.0, density=True, label=f'istep={i1}')
plt.hist(trj[i2,:], bins=50, rwidth=0.7, alpha=0.8, density=True, label=f'istep={i2}')
plt.hist(trj[i3,:], bins=50, rwidth=0.5, alpha=0.6, density=True, label=f'istep={i3}')
plt.plot(x, f, lw=3, color='red', label='Boltzmann')
plt.xlabel('x')
plt.ylabel('distribution')
plt.legend()
plt.show()

aa = np.zeros(nstep)
bb = np.zeros(nstep)
for i in range(nstep):
    for j in range(nrun):
        if trj[i,j] < 0.0: 
            aa[i] += 1
        else: 
            bb[i] += 1
plt.plot(tt, aa/nrun, lw=3, label='A')
plt.plot(tt, bb/nrun, lw=3, label='B')
plt.xlabel('t')
plt.ylabel('population')
plt.legend()
plt.show()

