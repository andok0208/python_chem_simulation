import matplotlib.pyplot as plt

k, tmax, h = 1.0, 5.0, 0.01
t, a, b = 0.0, 1.0, 0.0
tt, aa, bb, cc = [], [], [], []
while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    cc.append(a+b)
    t += h
    v = k*a**2  # 変更はこの行のみ
    a -= v*h
    b += v*h
plt.plot(tt, aa)
plt.plot(tt, bb)
plt.plot(tt, cc)
plt.show()

