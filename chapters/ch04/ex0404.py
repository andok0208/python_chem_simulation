import matplotlib.pyplot as plt
from ratelib import unimol_euler

k, n = 1.0, 1
tmax, h = 5.0, 0.1
a0, b0 = 1.0, 0.0
tt, aa, bb = unimol_euler(k, n, tmax, h, a0, b0)
plt.plot(tt, aa)
plt.plot(tt, bb)
plt.plot(tt, aa+bb, '--')
plt.show()

