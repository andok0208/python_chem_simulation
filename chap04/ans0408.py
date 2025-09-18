import matplotlib.pyplot as plt
from ratelib import unimol_euler

k = 1.0
tmax, h = 5.0, 0.1
a0, b0 = 1.0, 0.0

n = 1
tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)
plt.plot(tt, aa, label=f'[A], n = {n}')
plt.plot(tt, bb, label=f'[B], n = {n}')

n = 2
tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)
plt.plot(tt, aa, '--', label=f'[A], n = {n}')
plt.plot(tt, bb, '--', label=f'[B], n = {n}')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

