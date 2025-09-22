import matplotlib.pyplot as plt
from matplotlib import animation
from ratelib import lotka_euler

pq = 1.0, 1.0, 1.0, 1.0
tmax, h = 15, 0.05
aabb = []
for (a0, b0) in [(2.0, 1.0), (1.0, 3.0), (3.0, 2.0)]:
    tt, aa, bb = lotka_euler(pq, tmax, h, a0, b0)
    aabb.append((aa, bb))

fig = plt.figure()

lt = ['b--', 'r--', 'g--']
ims = []
for i in range(len(tt)):
    im = []
    for (j, (aa, bb)) in enumerate(aabb):
        im += plt.plot(aa[:i], bb[:i], lt[j])
    ims.append(im)
plt.xlabel('A (prey)')
plt.ylabel('B (predator)')
ani = animation.ArtistAnimation(fig, ims, interval=20)
plt.show()

