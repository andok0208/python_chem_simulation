import numpy as np
import matplotlib.pyplot as plt
from fftpow import powerSpectrum
from oscillator import leapfrog

k, m = 1.0, 1.0
tmax, h = 2*np.pi*100, 0.01
x0, v0 = 1.0, 0.0

tt, xx, vv = leapfrog(k, m, tmax, h, x0, v0)

dt = tt[1] - tt[0]
f, xp  = powerSpectrum(xx, dt, [0, 2])
print(f'df = {f[1]-f[0]:.4f}')
plt.plot(f, xp)
plt.xlabel('frequency')
plt.ylabel('power spectrum')
plt.show()

