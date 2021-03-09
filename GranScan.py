from matplotlib import pyplot as plt
from functools import reduce


def graham(points):
    TURN_RIGHT = -1

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp(
            (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) == TURN_RIGHT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


def scatter_plot(coords, convex_hull=None):
    xs, ys = zip(*coords)
    plt.scatter(xs, ys)

    if convex_hull != None:
        for i in range(1, len(convex_hull) + 1):
            if i == len(convex_hull): i = 0
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'r')
    plt.show()


points = [[4, 6], [2, 5], [4, 3], [0, 0], [2, 2], [5, 4], [4, 0], [0, 5]]
indexes = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
hull = graham(points)

print('\nPontos:')
for i in range(0, len(points)):
    print(f'{indexes[i]}: {points[i]}')

print(f'\nEnvoltória Convexa:\n{hull}')

scatter_plot(points, hull)