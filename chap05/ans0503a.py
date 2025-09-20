import matplotlib.pyplot as plt

k, tmax, h = 3.0, 5.0, 0.01
t, r, p = 0.0, 1.0, 0.01
tt, rr, pp = [], [], []
while t <= tmax:
    tt.append(t)
    rr.append(r)
    pp.append(p)
    t += h
    v = k*r*p
    r -= v*h
    p += v*h

plt.plot(tt, rr, label='[R]')
plt.plot(tt, pp, label='[P]')
plt.legend()
plt.show()

