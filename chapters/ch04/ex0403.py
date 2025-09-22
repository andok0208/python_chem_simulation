import numpy as np
import matplotlib.pyplot as plt

k, tmax = 1.0, 5.0
h = float(input('Enter h: '))
t, a, b = 0.0, 1.0, 0.0
tt, aa, bb = [], [], []
while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    t += h
    v = k*a
    a -= v*h
    b += v*h
tt = np.array(tt)
plt.plot(tt, aa)
plt.plot(tt, bb)
ax = np.exp(-k*tt)  # exact solution
bx = 1 - ax
plt.plot(tt, ax, '--')
plt.plot(tt, bx, '--')
#plt.yscale('log')
plt.show()

