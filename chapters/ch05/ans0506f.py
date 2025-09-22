import matplotlib.pyplot as plt
from ratelib import toeq_euler

tmax, h = 3.0, 0.01
a0, b0 = 1, 0

kf, kb = 2.0, 2.0
tt, aa, bb = toeq_euler(kf, kb, tmax, h, a0, b0)
plt.plot(tt, aa, label=f'[A] $k_f$ = {kf}, $k_b$ = {kb}')
plt.plot(tt, bb, label='[B]')

print(f'kf/kb = {kf/kb:.3f}')
print(f'K = {bb[-1]/aa[-1]:.3f}')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

