import numpy as np


def unimol_euler(k, n, tmax, h, a0, b0):
    t, a, b = 0.0, a0, b0
    tt, aa, bb = [], [], []
    while t <= tmax:
        tt.append(t)
        aa.append(a)
        bb.append(b)
        t += h
        v = k * a**n
        a -= v * h
        b += v * h
    tt = np.array(tt)
    aa = np.array(aa)
    bb = np.array(bb)
    return tt, aa, bb
    #return map(np.array, (tt, aa, bb))


def unimol_rk2(k, n, tmax, h, a0, b0):
    t, a, b = 0.0, a0, b0
    tt, aa, bb = [], [], []
    while t <= tmax:
        tt.append(t)
        aa.append(a)
        bb.append(b)
        t += h
        s1 = k * a**n
        s2 = k * (a - s1 * h/2)**n
        v = (s1 + s2)/2
        a -= v * h
        b += v * h
    return map(np.array, (tt, aa, bb))


def unimol_rk4(k, n, tmax, h, a0, b0):
    t, a, b = 0.0, a0, b0
    tt, aa, bb = [], [], []
    while t <= tmax:
        tt.append(t)
        aa.append(a)
        bb.append(b)
        t += h
        s1 = k * a**n
        s2 = k * (a - s1 * h/2)**n
        s3 = k * (a - s2 * h/2)**n
        s4 = k * (a - s3 * h)**n
        v = (s1 + 2*s2 + 2*s3 + s4)/6
        a -= v * h
        b += v * h
    return map(np.array, (tt, aa, bb))

