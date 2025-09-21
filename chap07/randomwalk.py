import numpy as np

def rw1d(nstep):
    x = 0.0
    xx = []
    for i in range(nstep):
        xx.append(x)
        x += (np.random.random() - 0.5) * 2
    return np.array(xx)


def rw1d_bn(nstep):
    x = 0.0
    xx = []
    for i in range(nstep):
        xx.append(x)
        rn = np.random.random()
        if rn > 0.5: x += 1.0
        else:        x -= 1.0
        #x += np.random.choice([-1.0, 1.0])
    return np.array(xx)

