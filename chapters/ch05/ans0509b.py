import matplotlib.pyplot as plt
from ratelib import preeq_euler

tmax, h = 8.0, 0.01
a0, b0, c0 = 1, 0, 0
kf, kb, kr = 2.0, 1.0, 0.3
tt, aa, bb, cc = preeq_euler(kf, kb, kr, tmax, h, a0, b0, c0)

plt.plot(tt, aa, label=f'[A] $k_f$={kf}, $k_b$={kb}, $k_r$={kr}')
plt.plot(tt, bb, label='[B]')
plt.plot(tt, cc, label='[C]')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

plt.plot(tt, bb/aa, label='[B]/[A]')
plt.xlabel('Time')
plt.ylabel('[B]/[A]')
plt.legend()
plt.show()

