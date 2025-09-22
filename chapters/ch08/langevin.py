import numpy as np

def maruyama(m, gamma, kBT, tmax, h, x0, v0):
    t, x, v = 0.0, x0, v0
    tt, xx, vv = [], [], []
    while t <= tmax:
        tt.append(t)
        xx.append(x)
        vv.append(v)
        t += h
        x += v * h
        v += - gamma / m * v * h
        v += np.sqrt(2 * kBT * gamma * h) * np.random.normal() / m  # Normal
    return map(np.array, (tt, xx, vv))


def maruyama_uni(m, gamma, kBT, tmax, h, x0, v0):
    t, x, v = 0.0, x0, v0
    tt, xx, vv = [], [], []
    while t <= tmax:
        tt.append(t)
        xx.append(x)
        vv.append(v)
        t += h
        x += v * h
        v += - gamma / m * v * h
        v += np.sqrt(2 * kBT * gamma * 3*h) * (np.random.random() - 0.5) * 2 / m  # Uniform
    return map(np.array, (tt, xx, vv))

