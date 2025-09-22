import numpy as np
import matplotlib.pyplot as plt
from fftpow import powerSpectrum


tmax, ndat = 2*np.pi*100, 2000
tt = np.linspace(0, tmax, ndat)
c1, c2 = 0.9, 0.8
xx = np.sin(tt) + c1*np.sin(1.3*tt) + c2*np.cos(0.7*tt)

nplot = int(ndat/10)
plt.plot(tt[:nplot], xx[:nplot])
plt.xlabel('t')
plt.ylabel('x(t)')
plt.show()

dt = tt[1] - tt[0]
f, xp  = powerSpectrum(xx, dt, [0.0, 2.0])
plt.plot(f, xp)
plt.plot(f, np.ones(len(f)),       '--', label=f'{1.0:.2f}')
plt.plot(f, np.ones(len(f))*c1**2, '--', label=f'{c1**2:.2f}')
plt.plot(f, np.ones(len(f))*c2**2, '--', label=f'{c2**2:.2f}')
plt.xlabel('frequency')
plt.ylabel('power spectrum')
plt.legend()
plt.show()

