import numpy as np
import matplotlib.pyplot as plt
from ratelib import unimol_euler, unimol_rk2, unimol_rk4

k, n = 1.0, 1
tmax = 5.0
a0, b0 = 1.0, 0.0

h = float(input('Enter h: '))

tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)
plt.plot(tt, aa, label=f'[A] Euler, h={h}')

tt, aa, bb = unimol_rk2(k, n, tmax, h, a0, b0)
plt.plot(tt, aa, label=f'[A] RK-2, h={h}')

tt, aa, bb = unimol_rk4(k, n, tmax, h, a0, b0)
plt.plot(tt, aa, label=f'[A] RK-4, h={h}')

plt.plot(tt, a0*np.exp(-k*tt), '--', label='exact')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.yscale('log')
plt.show()

