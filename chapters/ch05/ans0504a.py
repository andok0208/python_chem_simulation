import matplotlib.pyplot as plt

k1, k2 = 2, 1
tmax, h = 5.0, 0.01
t, a, b, c = 0.0, 1.0, 0.0, 0.0
tt, aa, bb, cc = [], [], [], []
while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    cc.append(c)
    t += h
    v1, v2 = k1 * a, k2 * b
    a += -v1 * h
    b += (v1 - v2) * h
    c +=  v2 * h

plt.plot(tt, aa, label='[A]')
plt.plot(tt, bb, label='[B]')
plt.plot(tt, cc, label='[C]')
plt.legend()
plt.show()

