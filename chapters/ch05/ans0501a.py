import matplotlib.pyplot as plt

k, tmax, h = 1.0, 5.0, 0.01
t, a, b, c = 0.0, 1.0, 1.1, 0.0
tt, aa, bb, cc = [], [], [], []
while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    cc.append(c)
    t += h
    v = k*a*b
    a -= v*h
    b -= v*h
    c += v*h

plt.plot(tt, aa, label='[A]')
plt.plot(tt, bb, label='[B]')
plt.plot(tt, cc, label='[C]')
plt.legend()
plt.show()

