import numpy as np
import matplotlib.pyplot as plt

nparticle = 3  # 粒子数
xeq = 1.0      # 平衡における隣接粒子間の距離
x =  np.array([-xeq, 0.0, xeq])        # 座標
x += np.array([-0.1, 0.2, -0.3])       # 変位
v = np.zeros(nparticle)                # 速度
m = np.array([3.0, 1.0, 2.0])          # 質量
k = np.zeros((nparticle, nparticle))
k[0,1] = 1.0  # 粒子1と2の間のバネ定数
k[1,2] = 1.0  # 粒子2と3の間のバネ定数

tmax, h = 30.0, 0.001
nstep = int(tmax / h) + 1
tt = np.empty(nstep)
xx = np.empty((nstep, nparticle)) # 2次元配列
vv = np.empty((nstep, nparticle))
ekin = np.empty(nstep)
epot = np.zeros(nstep)  # ゼロで初期化
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

for i in range(nparticle):
    plt.plot(tt, xx[:,i])
plt.xlabel('time')
plt.ylabel('x')
plt.show()
plt.plot(tt, ekin, label='ke')
plt.plot(tt, epot, label='pe')
plt.plot(tt, ekin+epot, label='ke+pe')
plt.xlabel('time')
plt.ylabel('energy')
plt.legend()
plt.show()

