import matplotlib.pyplot as plt
from oscillator import leapfrog, analytic

k, m = 1.0, 1.0
tmax, h = 30, 0.1
x0, v0 = 1.0, 0.0
tt, xx, vv = leapfrog(k, m, tmax, h, x0, v0)
plt.plot(tt, xx, '+', label='x leapfrog')
plt.plot(tt, vv, '+', label='v leapfrog')

xa, va = analytic(k, m, x0, v0, tt)
plt.plot(tt, xa,      label='x analytic')
plt.plot(tt, va,      label='v analytic')

plt.xlabel('t')
plt.ylabel('x, v')
plt.legend()
plt.show()

plt.plot(xx, vv, '+', label='x-v leapfrog')
plt.plot(xa, va,      label='x-v analytic')
plt.xlabel('x')
plt.ylabel('v')
plt.legend()
plt.show()

ke, pe = 0.5*m*vv**2, 0.5*k*xx**2
ka, pa = 0.5*m*va**2, 0.5*k*xa**2
plt.plot(tt, ke,    '+',  label='ke leapfrog')
plt.plot(tt, pe,    '+',  label='pe leapfrog')
plt.plot(tt, ke+pe, '--', label='ke+pe leapfrog')
plt.plot(tt, ka,          label='ke analytic')
plt.plot(tt, pa,          label='pe analytic')
plt.plot(tt, ka+pa,       label='ke+pe analytic')
plt.xlabel('t')
plt.ylabel('energy')
plt.legend()
plt.show()

