import numpy as np

def leapfrog(k, m, tmax, h, x0, v0):
    t, x, v = 0.0, x0, v0
    tt, xx, vv = [], [], []
    while t <= tmax:
        tt.append(t)
        xx.append(x)
        vv.append(v)
        t += h
        x += v * h * 0.5
        v += - k * x / m * h
        x += v * h * 0.5
    return map(np.array, (tt, xx, vv))


def analytic(k, m, x0, v0, t):
    omega = np.sqrt(k/m)
    xx = v0/omega*np.sin(omega*t) + x0*np.cos(omega*t)
    vv = v0*np.cos(omega*t) - omega*x0*np.sin(omega*t)
    return xx, vv


def euler(k, m, tmax, h, x0, v0):
    t, x, v = 0.0, x0, v0
    tt, xx, vv = [], [], []
    while t <= tmax:
        tt.append(t)
        xx.append(x)
        vv.append(v)
        t += h
        x += v * h
        v += - k * x / m * h
    return map(np.array, (tt, xx, vv))

