import numpy as np
import matplotlib.pyplot as plt
from ratelib import conseq_euler

tmax, h = 5.0, 0.01
a0, b0, c0 = 1.0, 0.0, 0.0

k1, k2 = 1.0, 6.0
tt, aa, bb, cc = conseq_euler(k1, k2, tmax, h, a0, b0, c0)
plt.plot(tt, cc, label=f'[C] k$_1$={k1} k$_2$={k2}')
plt.plot(tt, (1-np.exp(-k1*tt))*a0, '--', label='[C] approx.')

k1, k2 = 4.0, 0.4
tt, aa, bb, cc = conseq_euler(k1, k2, tmax, h, a0, b0, c0)
plt.plot(tt, cc, label=f'[C] k$_1$={k1} k$_2$={k2}')
plt.plot(tt, (1-np.exp(-k2*tt))*a0, '--', label='[C] approx.')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

