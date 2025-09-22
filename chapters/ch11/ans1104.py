import numpy as np
import matplotlib.pyplot as plt
from fftpow import powerSpectrum

# プログラムリスト4を挿入
nparticle = 3
xeq = 1.0
x =  np.array([-xeq, 0.0, xeq])
x += np.array([-0.2, 0.0, 0.2])  # 対称伸縮
#x += np.array([0.1, -0.1, 0.1])  # 逆対称伸縮
v = np.zeros(nparticle)
m = np.array([4.0, 3.0, 4.0])
k = np.zeros((nparticle, nparticle))
k[0,1], k[1,2] = 1.0, 1.0
tmax, h = 500.0, 0.001

nstep = int(tmax / h) + 1
tt = np.empty(nstep)
xx = np.empty((nstep, nparticle))
vv = np.empty((nstep, nparticle))
ekin = np.empty(nstep)
epot = np.zeros(nstep)
t = 0.0
for istep in range(nstep):
    tt[istep] = t
    xx[istep,:] = x
    vv[istep,:] = v
    t += h
    x += v * h * 0.5
    # 粒子iとjの間の力による運動
    for i in range(nparticle-1):
        for j in range(i+1, nparticle):
            dx = x[j] - x[i] - xeq
            f = - k[i,j] * dx
            v[i] -= f / m[i] * h
            v[j] += f / m[j] * h
            epot[istep] += 0.5 * k[i,j] * dx**2
    x += v * h * 0.5
    ekin[istep] = 0.5 * np.sum(m * v**2)

# 以下のように表示範囲を制限するとよい
nplot = int(nstep/10)
for i in range(nparticle-1):
    plt.plot(tt[:nplot], xx[:nplot,i+1]-xx[:nplot,i],
             label=f'particle {i+1}-{i+2}')
plt.legend()
plt.show()

# 以下が今回の主要部分
dt = tt[1] - tt[0]
for i in range(nparticle-1):
    f, xp = powerSpectrum(xx[:,i+1]-xx[:,i], dt, [0.0, 4.0])
    plt.plot(f,xp, label=f'particle {i+1}-{i+2}')
plt.xlabel('frequency')
plt.ylabel('power spectrum')
plt.legend()
plt.show()

# 演習11-3追加部分
xb1 = xx[:,1] - xx[:,0]
xb2 = xx[:,2] - xx[:,1]
xs = xb1 + xb2
xa = xb1 - xb2
plt.plot(tt[:nplot], xs[:nplot], label='sym stretch')
plt.plot(tt[:nplot], xa[:nplot], label='asym stretch')
plt.xlabel('time')
plt.ylabel('coordinate')
plt.legend()
plt.show()

f, xp = powerSpectrum(xs, dt, [0.0,2.5])
plt.plot(f, xp, label='sym stretch')
f, xp = powerSpectrum(xa, dt, [0.0,2.5])
plt.plot(f, xp, label='asym stretch')
plt.xlabel('frequency')
plt.ylabel('power spectrum')
plt.legend()
plt.show()

"""
# 図11.7
nplot2 = int(nstep/4)
plt.axes().set_aspect('equal')
plt.plot(xb1[:nplot2], xb2[:nplot2])
plt.show()
plt.axes().set_aspect('equal')
plt.plot(xs[:nplot2], xa[:nplot2])
plt.show()
"""

