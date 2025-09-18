k, tmax, h = 1.0, 5.0, 0.01
t, a, b = 0.0, 1.0, 0.0
while t <= tmax:
    print(t, a, b, a+b)
    t += h
    v = k*a
    a -= v*h
    b += v*h

