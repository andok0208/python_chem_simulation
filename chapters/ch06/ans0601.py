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
    va = ( p1 - q1 * b) * a
    vb = (-p2 + q2 * a) * b
    a += va * h
    b += vb * h

plt.plot(tt, aa, label=f'A (prey) h={h}')
plt.plot(tt, bb, label='B (predator)')
plt.xlabel('Time', fontsize=16)
plt.ylabel('Population', fontsize=16)
plt.legend(fontsize=12)
plt.savefig('ans0601a.png')
plt.show()

plt.plot(aa, bb, label=f'A$_0$={a0} B$_0$={b0} h={h}')
plt.xlabel('A (prey)', fontsize=16)
plt.ylabel('B (predator)', fontsize=16)
plt.legend(fontsize=12)
plt.savefig('ans0601b.png')
plt.show()

