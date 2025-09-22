import matplotlib.pyplot as plt

A, B = 1, 3

tmax, h = 30, 0.01

x0, y0 = 1, 1
t, x, y = 0.0, x0, y0

tt, xx, yy = [], [], []

while t <= tmax:
    tt.append(t)
    xx.append(x)
    yy.append(y)
    t += h
    x += ( A - (B+1) * x + x * x * y) * h
    y += ( B * x - x * x * y) * h

plt.plot(tt, xx, label='[X]')
plt.plot(tt, yy, label='[Y]')

plt.title(f'X$_0$=Y$_0$={x0}, A={A}, B={B}')
plt.xlabel('time')
plt.ylabel('[X], [Y]')
plt.legend()
plt.show()

plt.plot(xx, yy, label=f'X$_0$={x0}, Y$_0$={y0}')
plt.title(f'A={A}, B={B}')
plt.xlabel('[X]')
plt.ylabel('[Y]')
plt.legend()
plt.show()

