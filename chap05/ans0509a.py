import matplotlib.pyplot as plt

tmax, h = 8.0, 0.01
kf, kb, kr = 2.0, 1.0, 0.3
t, a, b, c = 0, 1, 0, 0

tt, aa, bb, cc = [], [], [], []
while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    cc.append(c)
    t += h
    vf, vb, vr = kf * a, kb * b, kr * b
    a += (-vf + vb ) * h
    b += ( vf - vb - vr ) * h
    c +=   vr * h

plt.plot(tt, aa, label=f'[A] $k_f$={kf}, $k_b$={kb}, $k_r$={kr}')
plt.plot(tt, bb, label='[B]')
plt.plot(tt, cc, label='[C]')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()
plt.show()

