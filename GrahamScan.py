from matplotlib import pyplot as plt
from functools import reduce


def CCW(p1, p2, p3):
    def cmp(a, b):
        return (a > b) - (a < b)

    return cmp(
        (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0]),
        0)


def graham_scan(points):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def keep_left(hull, temp):
        while len(hull) > 1 and CCW(hull[-2], hull[-1], temp) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != temp:
            hull.append(temp)
        return hull

    points = sorted(points)
    sup = reduce(keep_left, points, [])
    inf = reduce(keep_left, reversed(points), [])
    return sup.extend(inf[i] for i in range(1, len(inf) - 1)) or sup


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


#======================================== MAIN ========================================#

points = [[4, 6], [2, 5], [4, 3], [0, 0], [2, 2], [5, 4], [4, 0], [0, 5]]
indexes = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

hull = graham_scan(points)

print('\nPontos:')
for i in range(0, len(points)):
    print(f'{indexes[i]}: {points[i]}')

print(f'\nEnvoltória Convexa:\n{hull}')

scatter_plot(points, hull)