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
    # 粒子1と2の間の力による運動
    dx = x[1] - x[0] - xeq  # 平衡長からの変位
    f = - k[0,1] * dx       # バネによる力
    v[0] -= f / m[0] * h    # 符号に注意
    v[1] += f / m[1] * h
    epot[istep] += 0.5 * k[0,1] * dx**2
    # 粒子2と3の間の力による運動
    dx = x[2] - x[1] - xeq
    f = - k[1,2] * dx
    v[1] -= f / m[1] * h
    v[2] += f / m[2] * h
    epot[istep] += 0.5 * k[1,2] * dx**2
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

