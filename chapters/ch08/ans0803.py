import numpy as np
import matplotlib.pyplot as plt
from langevin import maruyama
#from langevin import maruyama_uni  # 演習8-4

m, gamma, kBT = 1.0, 1.0, 1.0
tmax, h = 100, 0.1
x0, v0 = 0.0, 0.0

for nrun in [500, 1000]:
    xsq = np.zeros(int(tmax/h)+1)
    for _ in range(nrun):
        #v0 = np.random.normal() * np.sqrt(kBT/m)
        tt, xx, vv = maruyama(m, gamma, kBT, tmax, h, x0, v0)
        #tt, xx, vv = maruyama_uni(m, gamma, kBT, tmax, h, x0, v0)  # 演習8-4
        xsq += xx**2
    plt.plot(tt, xsq/nrun, label=f'nrun={nrun}')
diffc = kBT/gamma
plt.plot(tt, 2*diffc*tt, label='2Dt')
plt.xlabel('time')
plt.ylabel('mean square displacement')
plt.legend()
plt.show()

