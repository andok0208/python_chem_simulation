import numpy as np


def lotka_euler(pq, tmax, h, a0, b0):
    p1, q1, p2, q2 = pq
    t, a, b = 0.0, a0, b0
    tt, aa, bb = [], [], []
    while t <= tmax:
        tt.append(t)
        aa.append(a)
        bb.append(b)
        t += h
        a += ( p1 - q1 * b) * a * h
        b += (-p2 + q2 * a) * b * h
    return map(np.array, (tt, aa, bb))


def brussel_euler(A, B, tmax, h, x0, y0):
    t, x, y = 0.0, x0, y0
    tt, xx, yy = [], [], []
    while t <= tmax:
        tt.append(t)
        xx.append(x)
        yy.append(y)
        t += h
        x += ( A - (B+1) * x + x * x * y) * h
        y += ( B * x - x * x * y) * h
    return map(np.array, (tt, xx, yy))

