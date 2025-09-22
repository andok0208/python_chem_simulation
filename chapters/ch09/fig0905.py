import numpy as np
import matplotlib.pyplot as plt

m, eb, d = 1.0, 6.0, 1.0

def pot(x):
    return eb*((x/d)**2 - 1)**2

def force(x):
    return -4*eb*((x/d)**2 - 1)*x/d**2

tmax, h = 5.0, 0.01
nstep = int(tmax/h)+1

tt = np.empty(nstep)
xx = np.empty((nstep, 2))
vv = np.empty((nstep, 2))
x0 = [1.4, 1.6]

for j in range(2):
    t, x, v = 0.0, x0[j], 0.0
    for i in range(nstep):
        tt[i], xx[i,j], vv[i,j] = t, x, v
        t += h
        x += v * h * 0.5
        v += force(x) * h
        x += v * h * 0.5

for j in range(2):
    plt.plot(tt, xx[:,j], label=f'x0={x0[j]}')
plt.xlabel('time')
plt.ylabel('x')
plt.legend()
plt.show()

for j in range(2):
    plt.plot(xx[:,j], vv[:,j], label=f'x0={x0[j]}')
plt.xlabel('x')
plt.ylabel('v')
plt.legend()
plt.show()

for j in range(2):
    ke, pe = 0.5*m*vv[:,j]**2, pot(xx[:,j])
    plt.plot(tt, ke, label='ke')
    plt.plot(tt, pe, label='pe')
    plt.plot(tt, ke+pe, label='ke+pe')
    plt.title(f'x0={x0[j]}')
    plt.xlabel('time')
    plt.ylabel('energy')
    plt.legend()
    plt.show()

