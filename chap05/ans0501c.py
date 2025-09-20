import matplotlib.pyplot as plt
from ratelib import unimol_euler, bimol_euler

tmax, h = 5.0, 0.01
k = 1.0
a0, c0 = 1.0, 0.0
b0 = float(input('Enter b0 for bimol: '))
tt, aa, bb, cc = bimol_euler(k, tmax, h, a0, b0, c0)
plt.plot(tt, aa, label='[A] bimol')
plt.plot(tt, bb, label='[B]')
plt.plot(tt, cc, label='[C]')

n = 2
b0 = 0.0
tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)
plt.plot(tt, aa, '--', label=f'[A] unimol n={n}')
plt.plot(tt, bb, '--', label='[B]')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

