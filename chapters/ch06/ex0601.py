import matplotlib.pyplot as plt

p1, q1, p2, q2 = 1.0, 1.0, 1.0, 1.0
tmax, h = 20, 0.01
a0, b0 = 2.0, 1.0
t, a, b = 0.0, a0, b0
tt, aa, bb = [], [], []
while t <= tmax:
    tt.append(t)
    aa.append(a)
    bb.append(b)
    t += h
    a += ( p1 - q1 * b) * a * h
    b += (-p2 + q2 * a) * b * h

plt.plot(tt, aa)
plt.plot(tt, bb)
plt.show()
plt.plot(aa, bb)
plt.show()

plt.plot(tt, aa, label='A (prey)')
plt.plot(tt, bb, label='B (predator)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()

plt.plot(aa, bb, label=f'A$_0$={a0}, B$_0$={b0}')
plt.xlabel('A (prey)')
plt.ylabel('B (predator)')
plt.legend()
plt.show()

