import numpy as np
import matplotlib.pyplot as plt

k, tmax, h = 1.0, 5.0, 0.01
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
aa = np.array(aa)
bb = np.array(bb)
plt.plot(tt, aa)
plt.plot(tt, bb)
plt.plot(tt, aa+bb)
plt.show()

