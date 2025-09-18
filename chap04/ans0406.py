import numpy as np
import matplotlib.pyplot as plt

k, tmax = 1.0, 5.0
h = float(input('Enter h: '))
a0, b0 = 1.0, 0.0
t, a, b = 0.0, a0, b0
tt, aa, bb = [], [], []

while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    t += h
    v = k*a**2
    a -= v*h
    b += v*h

tt = np.array(tt)
aa = np.array(aa)
bb = np.array(bb)
plt.plot(tt, 1/aa, label=f'1/[A] with h={h}')
plt.plot(tt,   1/a0+k*tt, '--', label='exact')
plt.xlabel('Time')
plt.ylabel('1/[A]')
plt.legend()
plt.show()

