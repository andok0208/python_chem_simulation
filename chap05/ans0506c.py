import matplotlib.pyplot as plt

kf, kb = 2, 1
tmax, h = 3.0, 0.01
t, a, b = 0.0, 1.0, 0.0
tt, aa, bb = [], [], []
while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    t += h
    vf, vb = kf * a, kb * b
    a += (-vf + vb) * h
    b += ( vf - vb) * h

plt.plot(tt, aa, label='[A]')
plt.plot(tt, bb, label='[B]')
plt.legend()
plt.show()

