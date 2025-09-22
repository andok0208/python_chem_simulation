import numpy as np
import matplotlib.pyplot as plt
from fftpow import powerSpectrum
from oscillator import leapfrog

k, m, h = 1.0, 1.0, 0.01
x0, v0 = 1.0, 0.0
for nt in [100, 200, 400]:
    tmax = 2*np.pi*nt
    tt, xx, vv = leapfrog(k, m, tmax, h, x0, v0)
    dt = tt[1] - tt[0]
    f, xp  = powerSpectrum(xx, dt, [0.8, 1.2])
    print(f'df = {f[1]-f[0]:.4f}')
    plt.plot(f, xp, label=f'tmax=$2\pi$ * {nt}')

plt.xlabel('frequency')
plt.ylabel('power spectrum')
plt.legend()
plt.show()

