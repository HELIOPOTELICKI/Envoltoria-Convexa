from functools import reduce
from io import BytesIO
from PIL import Image
import requests


def graham(points):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp(
            (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


points = [[4, 6], [2, 5], [4, 3], [0, 0], [2, 2], [5, 4], [4, 0], [0, 5]]
indexes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

print('\nPontos:')
for i in range(0, len(points)):
    print(f'{indexes[i]}: {points[i]}')

print(f'\nEnvoltória Convexa:\n{graham(points)}')

imgUrl = 'https://uploaddeimagens.com.br/images/003/118/011/original/points.png?1615165544'
response = requests.get(imgUrl)
image_bytes = BytesIO(response.content)
img = Image.open(image_bytes)
img.show()