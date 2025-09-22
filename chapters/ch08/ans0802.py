import numpy as np
import matplotlib.pyplot as plt
from langevin import maruyama
#from langevin import maruyama_uni  # 演習8-4

m, gamma, kBT = 1.0, 1.0, 1.0
tmax, h = 100, 0.1
x0, v0 = 0.0, 0.0
nrun = int(input('Enter nrun: '))

xend, xmid = [], []
for _ in range(nrun):
    #v0 = np.random.normal() * np.sqrt(kBT/m)
    tt, xx, vv = maruyama(m, gamma, kBT, tmax, h, x0, v0)
    #tt, xx, vv = maruyama_uni(m, gamma, kBT, tmax, h, x0, v0)  # 演習8-4
    xend.append(xx[-1])
    nmid = int((len(xx)-1)/4)
    xmid.append(xx[nmid])
plt.hist(xmid, bins=30, rwidth=0.8, alpha=1.0, density=True, 
        label=f't={tt[nmid]:.1f}')
plt.hist(xend, bins=30, rwidth=0.5, alpha=0.9, density=True, 
        label=f't={tt[-1]:.1f}')
xmax = np.max(np.abs(xend))
x = np.linspace(-xmax, xmax, 200)
for n in [nmid, -1]:
    sigma = np.sqrt(2*kBT/gamma*tt[n])
    g = 1/np.sqrt(2*np.pi)/sigma*np.exp(-0.5*x**2/sigma**2)
    plt.plot(x, g, linewidth=3)
plt.xlabel('x')
plt.ylabel('distribution')
plt.legend()
plt.show()

