import matplotlib.pyplot as plt
from ratelib import autocat_euler

k, tmax, h = 3.0, 5.0, 0.01

r0, p0 = 1.0, 0.01
tt, rr, pp = autocat_euler(k, tmax, h, r0, p0)
plt.plot(tt, rr, label=f'[R]$_0$={r0}')
plt.plot(tt, pp, label=f'[P]$_0$={p0}')

r0, p0 = 1.0, 0.001
tt, rr, pp = autocat_euler(k, tmax, h, r0, p0)
plt.plot(tt, rr, '--', label=f'[R]$_0$={r0}')
plt.plot(tt, pp, '--', label=f'[P]$_0$={p0}')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

# 別解
r0 = 1.0
for (p0, lt) in [(0.01, '-'), (0.001, '--')]:
    tt, rr, pp = autocat_euler(k, tmax, h, r0, p0)
    plt.plot(tt, rr, lt, label=f'[R]$_0$={r0}')
    plt.plot(tt, pp, lt, label=f'[P]$_0$={p0}')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

