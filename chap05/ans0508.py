import numpy as np
import matplotlib.pyplot as plt
from ratelib import toeq_euler

tmax, h = 3.0, 0.1
a0, b0 = 1, 0

kf, kb = 2.0, 1.0
tt, aa, bb = toeq_euler(kf, kb, tmax, h, a0, b0)
plt.plot(tt, aa, label=f'[A] $k_f$ = {kf}, $k_b$ = {kb}')
plt.plot(tt, bb, label='[B]')

aoo = kb*a0/(kf+kb)
ax = (a0-aoo)*np.exp(-(kf+kb)*tt) + aoo
bx = a0 - ax
plt.plot(tt, ax, '--')
plt.plot(tt, bx, '--')

kf, kb = 1.0, 2.5
tt, aa, bb = toeq_euler(kf, kb, tmax, h, a0, b0)
plt.plot(tt, aa, label=f'[A] $k_f$ = {kf}, $k_b$ = {kb}')
plt.plot(tt, bb, label='[B]')

aoo = kb*a0/(kf+kb)
ax = (a0-aoo)*np.exp(-(kf+kb)*tt) + aoo
bx = a0 - ax
plt.plot(tt, ax, '--')
plt.plot(tt, bx, '--')

plt.title(f'h={h}')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

# 別解
for (kf, kb) in [(2.0, 1.0), (1.0, 2.5)]:
    tt, aa, bb = toeq_euler(kf, kb, tmax, h, a0, b0)
    plt.plot(tt, aa, label=f'[A] $k_f$ = {kf}, $k_b$ = {kb}')
    plt.plot(tt, bb, label='[B]')
    aoo = kb*a0/(kf+kb)
    ax = (a0-aoo)*np.exp(-(kf+kb)*tt) + aoo
    bx = a0 - ax
    plt.plot(tt, ax, '--')
    plt.plot(tt, bx, '--')

plt.title(f'h={h}')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

