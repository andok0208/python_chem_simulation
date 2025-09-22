import matplotlib.pyplot as plt
from ratelib import conseq_euler

tmax, h = 5.0, 0.01

k1, k2 = 1.0, 10.0
a0, b0, c0 = 1.0, 0.0, 0.0
tt, aa, bb, cc = conseq_euler(k1, k2, tmax, h, a0, b0, c0)
plt.plot(tt, aa, label='[A]')
plt.plot(tt, bb, label=f'[B] k$_1$={k1}, k$_2$={k2}')
plt.plot(tt, cc, label='[C]')

k1, k2 = 1.0, 0.8
tt, aa, bb, cc = conseq_euler(k1, k2, tmax, h, a0, b0, c0)
plt.plot(tt, bb, '--', label=f'[B] k$_1$={k1}, k$_2$={k2}')
plt.plot(tt, cc, '--', label='[C]')
plt.plot(tt, aa+bb+cc, '--', label='[A]+[B]+[C]')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

# 別解
for (k2, lt) in [(10.0, '-'), (0.8, '--')]:
    tt, aa, bb, cc = conseq_euler(k1, k2, tmax, h, a0, b0, c0)
    plt.plot(tt, aa, label='[A]')
    plt.plot(tt, bb, lt, label=f'[B] k$_1$={k1}, k$_2$={k2}')
    plt.plot(tt, cc, lt, label='[C]')
    plt.plot(tt, aa+bb+cc, lt, label='[A]+[B]+[C]')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

