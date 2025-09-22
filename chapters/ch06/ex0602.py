import matplotlib.pyplot as plt
from ratelib import lotka_euler

pq = 1.0, 1.0, 1.0, 1.0
tmax, h = 20, 0.01
a0, b0 = 2.0, 1.0
tt, aa, bb = lotka_euler(pq, tmax, h, a0, b0)

plt.plot(tt, aa)
plt.plot(tt, bb)
plt.show()
plt.plot(aa, bb)
plt.show()

