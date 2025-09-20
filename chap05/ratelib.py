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
    return map(np.array, (tt, aa, bb))


def bimol_euler(k, tmax, h, a0, b0, c0):
    t, a, b, c = 0.0, a0, b0, c0
    tt, aa, bb, cc = [], [], [], []
    while t <= tmax:
        tt.append(t)
        aa.append(a)
        bb.append(b)
        cc.append(c)
        t += h
        v = k * a * b
        a -= v * h
        b -= v * h
        c += v * h
    return map(np.array, (tt, aa, bb, cc))


def autocat_euler(k, tmax, h, r0, p0):
    t, r, p = 0.0, r0, p0
    tt, rr, pp = [], [], []
    while t <= tmax:
        tt.append(t)
        rr.append(r)
        pp.append(p)
        t += h
        v = k * r * p
        r -= v * h
        p += v * h
    return map(np.array, (tt, rr, pp))


def conseq_euler(k1, k2, tmax, h, a0, b0, c0):
    t, a, b, c = 0.0, a0, b0, c0
    tt, aa, bb, cc = [], [], [], []
    while t <= tmax:
        tt.append(t)
        aa.append(a)
        bb.append(b)
        cc.append(c)
        t += h
        v1, v2 = k1 * a, k2 * b
        a += -v1 * h
        b += (v1 - v2) * h
        c +=  v2 * h
    return map(np.array, (tt, aa, bb, cc))


def toeq_euler(kf, kb, tmax, h, a0, b0):
    t, a, b = 0.0, a0, b0
    tt, aa, bb = [], [], []
    while t <= tmax:
        tt.append(t)
        aa.append(a)
        bb.append(b)
        t += h
        vf, vb = kf * a, kb * b
        a += (-vf + vb) * h
        b += ( vf - vb) * h
    return map(np.array, (tt, aa, bb))


def preeq_euler(kf, kb, kr, tmax, h, a0, b0, c0):
    t, a, b, c = 0.0, a0, b0, c0
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
    return map(np.array, (tt, aa, bb, cc))

