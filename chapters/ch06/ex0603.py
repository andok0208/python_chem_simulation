import matplotlib.pyplot as plt
from ratelib import lotka_euler

pq = 1.0, 1.0, 1.0, 1.0
tmax, h = 20, 0.01
for (a0, b0) in [(2.0, 1.0), (1.0, 3.0), (3.0, 2.0)]:
    tt, aa, bb = lotka_euler(pq, tmax, h, a0, b0)
    plt.plot(aa, bb)
plt.show()

