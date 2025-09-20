import matplotlib.pyplot as plt
from ratelib import unimol_euler, bimol_euler

tmax, h = 5, 0.01

k = 0.1
a0, b0, c0 = 1.0, 10.0, 0.0
tt, aa, bb, cc = bimol_euler(k, tmax, h, a0, b0, c0)
plt.plot(tt, aa, label='[A] bimol excess [B]$_0$')
plt.plot(tt, cc, label='[C]')

k = 1.0
n = 1
b0 = 0.0
tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)
plt.plot(tt, aa, '--', label=f'[A] unimol n={n}')
plt.plot(tt, bb, '--', label='[B]')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

