import matplotlib.pyplot as plt
from ratelib import unimol_euler

k, n = 1.0, 1
tmax, h = 5.0, 0.1
a0, b0 = 1.0, 0.0

tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)

plt.plot(tt, aa, label=f'[A], k = {k}')
plt.plot(tt, bb, label=f'[B], k = {k}')

k = 0.7
tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)

plt.plot(tt, aa, '--', label=f'[A], k = {k}')
plt.plot(tt, bb, '--', label=f'[B], k = {k}')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

